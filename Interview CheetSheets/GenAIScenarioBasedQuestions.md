## Q. Your LLM is hallucinating. How would you reduce it?

### Interview Answer

First, I would identify **where the hallucination is coming from** instead of immediately changing the model.

I would normally check four areas:

1. **Retrieval problem** – the correct information is not being retrieved.
2. **Data/chunking problem** – the knowledge base may contain outdated data or poor chunks.
3. **Prompt problem** – the model is not clearly instructed to stay within the provided context.
4. **Generation problem** – the context is correct, but the LLM is still generating unsupported information.

For a knowledge-based application, my preferred production approach would be **RAG with strict grounding**.

I would retrieve information from trusted sources and instruct the LLM to answer only from that context. If the answer is not present, the model should say that the information is unavailable instead of guessing.

Then I would improve retrieval using proper chunking, good embeddings, Top-K tuning, metadata filtering, and reranking if required.

For factual applications, I would also use a **lower temperature** because I want predictable answers rather than creative ones.

For critical information such as amounts, dates, IDs, or transaction statuses, I would validate the LLM output against the source document, database, or API.

I would also provide **citations/source references** wherever possible.

Finally, if retrieval confidence is low or no relevant information is found, I would use a safe fallback rather than allowing the model to generate an unsupported answer.

So my approach would be:

**Ground the model → improve retrieval → constrain generation → validate critical outputs → monitor hallucinations.**

### Simple Flow

User Query
↓
Retrieve Trusted Context
↓
Check Retrieval Quality
↓
LLM with Grounding Instructions
↓
Validate Critical Information
↓
Answer + Source
↓
Fallback if Evidence is Insufficient

---

### Follow-up Questions

#### 1. What would you do if the retrieved documents themselves contain incorrect information?

Then it is mainly a **data-quality problem, not an LLM problem**.

I would validate the knowledge base before ingestion, remove outdated or duplicate documents, and maintain metadata such as document version, source, and last-updated date.

If multiple sources conflict, I would prioritize an authoritative source such as the production database or approved business documentation.

For critical applications, I would also introduce human approval for updating the knowledge base.

**Key point:** RAG can ground an LLM, but if the source itself is wrong, the grounded answer can still be wrong.

---

#### 2. How would you measure hallucination in a RAG application?

I would create an **evaluation dataset** containing questions with known expected answers and source documents.

Then I would measure two things separately:

- **Retrieval quality** – did we retrieve the document containing the correct answer?
- **Answer faithfulness** – is the generated answer actually supported by the retrieved context?

I would also track production metrics such as unsupported-answer rate, fallback rate, user feedback, and failed queries.

For important systems, I would periodically manually review a sample of responses as well.

This helps identify whether the issue is with **retrieval or generation** instead of treating everything as an LLM problem.

---

#### 3. Does lowering temperature completely remove hallucination?

No.

Lower temperature makes the output **more deterministic and less creative**, but it does not guarantee correctness.

For example, if the model receives incorrect context, it can confidently produce the same incorrect answer every time even with temperature set very low.

So I would use low temperature for factual tasks, but combine it with:

**trusted context + grounding + retrieval quality + validation + fallback.**

Temperature is only one control, not the complete solution.

---

#### 4. What would you do if RAG retrieves the correct document but the LLM still gives the wrong answer?

Then I know that retrieval is probably working, so I would investigate the **generation side**.

First, I would check whether the retrieved chunk actually contains enough surrounding context.

Then I would improve the prompt and explicitly tell the model to answer only from the retrieved context.

I might also reduce irrelevant context because too much information can confuse the model.

For structured information, I would ask for structured output and validate the result programmatically.

If necessary, I could also test a stronger model.

So I would troubleshoot it as:

Correct retrieval
↓
Check chunk/context
↓
Improve grounding prompt
↓
Reduce irrelevant context
↓
Validate output
↓
Evaluate model if still incorrect

---

### Quick Revision

> Hallucination reduction = trusted data + strong retrieval + grounded prompt + low creativity + output validation + safe fallback.

## Q. How would you verify the correctness of an LLM response?

### Interview Answer

I would **not trust the LLM response directly**, especially for factual or business-critical use cases.

I would verify correctness at multiple levels depending on the type of response.

First, if I am using **RAG**, I would check whether the answer is actually supported by the retrieved documents. This helps me separate two problems:

- **Retrieval correctness** – did we retrieve the right information?
- **Generation correctness** – did the LLM correctly use that information?

Second, wherever possible, I would use **deterministic validation** instead of another LLM.

For example, if the LLM returns a trade ID, amount, settlement status, or customer information, I can verify it directly against the database, API, or business rules.

For structured responses, I would also validate the **schema and data types**. For example, if I expect JSON containing `trade_id`, `status`, and `amount`, I can validate that before accepting the response.

For testing, I would maintain a **golden or reference dataset** containing questions, expected answers, and expected source documents. I can run the LLM against this dataset whenever I change the model, prompt, embedding model, or retrieval configuration.

I can measure things like:

- Retrieval accuracy
- Answer correctness
- Faithfulness to the context
- Invalid/unsupported answer rate

An **LLM-as-a-judge** can also help evaluate large numbers of responses, but I would use it as an additional signal, not as the only source of truth, because another LLM can also make mistakes.

For high-risk decisions, I would add **human review**.

So in production, my preferred approach is:

**Source verification + deterministic checks + automated evaluation + human review for critical cases.**

### Simple Flow

User Query
↓
Retrieve Source
↓
LLM Generates Response
↓
Check Response Against Source
↓
Business Rule / Database / Schema Validation
↓
Confidence / Evaluation
↓
Return Response

For critical cases:

Validation Fails
↓
Fallback / Human Review

---

### Follow-up Questions

#### 1. What is a golden dataset?

A golden dataset is a **small, high-quality evaluation dataset where I already know the correct answers**.

For example:

Question:
"What is the settlement status of Trade 123?"

Expected Answer:
"Pending"

Expected Source:
Trade record/document containing that status.

Whenever I change the prompt, model, chunking, or retrieval configuration, I run the same test cases again.

This helps me detect whether the new version improved the system or introduced regressions.

---

#### 2. What is faithfulness in RAG?

Faithfulness means:

**Is the generated answer actually supported by the retrieved context?**

For example, suppose the retrieved document says:

`Settlement Status: Pending`

but the LLM answers:

`The trade has successfully settled.`

The answer may sound convincing, but it is **not faithful to the context**.

So correctness and faithfulness are related, but faithfulness specifically checks whether the LLM stayed grounded in the provided evidence.

---

#### 3. Would you use another LLM to verify the response?

Yes, but I would **not depend on it as the only validator**.

An LLM-as-a-judge is useful when evaluating thousands of responses for things like relevance, faithfulness, or answer quality.

But because the judge itself is an LLM, it can also make mistakes.

So my preference would be:

**Deterministic validation when possible → LLM judge as an additional signal → human review for critical cases.**

For example, checking a trade status directly from SQL is much more reliable than asking another LLM whether the status looks correct.

---

#### 4. How would you verify an answer when there is no exact ground truth?

If there is no exact expected answer, I would verify whether the response is **supported by authoritative sources**.

For RAG, I can check whether every important claim is grounded in the retrieved documents.

I can also use business rules, consistency checks, user feedback, and human evaluation.

For open-ended responses, I would evaluate dimensions such as:

- Relevance
- Faithfulness
- Completeness
- Safety

So the validation strategy depends on whether the task is **factual, structured, or open-ended**.

---

### Quick Revision

> Verify LLM responses using trusted sources, deterministic business checks, golden datasets, faithfulness evaluation, and human review for critical cases.