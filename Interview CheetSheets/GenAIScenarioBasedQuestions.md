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