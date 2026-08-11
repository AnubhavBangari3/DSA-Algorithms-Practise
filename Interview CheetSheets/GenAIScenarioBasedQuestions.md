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

## Q. RAG is retrieving irrelevant documents. How would you improve it?

### Interview Answer

If RAG is retrieving irrelevant documents, I would treat it primarily as a **retrieval problem** and debug the pipeline step by step.

First, I would check whether the issue is with the **data or chunking**.

If chunks are too large, they may contain too much unrelated information. If they are too small, they may lose important context. So I would test a better chunk size and overlap based on the document type.

Second, I would check the **embedding model**. The embedding model should match the type of data and queries I have. If semantic similarity is poor, even good documents may rank incorrectly.

Third, I would tune **Top-K retrieval**. If I retrieve too many chunks, I may send noisy context to the LLM. If I retrieve too few, I may miss the correct answer.

Then I would add **metadata filtering** where possible.

For example, if the user asks about settlement messages, I can filter by document type, client, date, module, or message category before vector search.

If pure vector search is still weak, I would use **hybrid search**, combining semantic search with keyword/BM25 search. This is especially useful for exact terms like trade IDs, product names, error codes, or SWIFT message types.

After retrieval, I would add a **reranker** so that the initially retrieved chunks are reordered based on how relevant they are to the exact query.

I would also test **query rewriting** if user queries are short or ambiguous.

Finally, I would evaluate retrieval separately using a dataset where I know which document should be retrieved for each question.

So my production approach would be:

**Fix chunking → check embeddings → tune Top-K → use metadata filters → hybrid search → rerank → evaluate retrieval quality.**

### Simple Flow

User Query
↓
Query Rewrite if Needed
↓
Metadata Filter
↓
Hybrid / Vector Search
↓
Top-K Candidates
↓
Reranker
↓
Best Relevant Chunks
↓
LLM

---

### Follow-up Questions

#### 1. How would you know whether the problem is retrieval or generation?

I would inspect the retrieved chunks before looking at the final LLM answer.

If the correct information is **not present in the retrieved context**, then it is a retrieval problem.

If the correct information is already present but the LLM still gives the wrong answer, then it is mainly a generation or prompt problem.

So I always evaluate retrieval independently from generation.

---

#### 2. What is hybrid search and why would you use it?

Hybrid search combines:

- **Semantic/vector search** for meaning
- **Keyword/BM25 search** for exact text matches

I would use it when the knowledge base contains both natural-language information and exact identifiers.

For example, vector search may understand:

`Why did this settlement fail?`

But keyword search may be better for:

`MT548`, `Trade12345`, or a specific error code.

Combining both usually gives more reliable retrieval.

---

#### 3. What is reranking?

Reranking means I first retrieve a larger set of candidate chunks and then use a stronger relevance model to reorder them.

For example:

Vector Search → Top 20 chunks  
Reranker → Best 5 chunks

The first retrieval stage is fast, while the reranker is more accurate but more expensive.

So in production, I would use reranking when retrieval quality is important enough to justify the additional latency and cost.

---

#### 4. How would you choose the right chunk size?

I would not choose chunk size randomly.

I would start based on the document structure and then evaluate it using real questions.

For example, a FAQ may work well with smaller chunks, while technical documentation may need larger chunks so related information stays together.

I would test:

- different chunk sizes
- different overlaps
- semantic or heading-based chunking

Then I would measure whether the expected chunk appears in the top retrieval results.

The correct chunk size is the one that gives the best retrieval quality for my data, not simply the largest or smallest value.

---

### Quick Revision

> Irrelevant RAG retrieval = check chunking and embeddings first, then tune Top-K, filters, hybrid search, reranking, and evaluate retrieval separately.

## Q. Correct information exists in the documents, but RAG still gives the wrong answer. What would you check?

### Interview Answer

If the correct information exists in the documents but RAG still gives the wrong answer, I would debug the pipeline in stages instead of assuming the LLM is the problem.

First, I would check **whether the correct chunk is actually being retrieved**.

If it is not being retrieved, then I would investigate:
- chunking
- embeddings
- Top-K
- metadata filters
- hybrid search
- reranking

That means the issue is mainly a **retrieval or data/chunking problem**.

If the correct chunk is being retrieved, then I would check whether the chunk contains **enough surrounding context**. Sometimes the exact answer is present, but important information is split across two chunks.

Next, I would inspect the **prompt**. I would make sure the LLM is clearly instructed to answer only from the retrieved context and not rely on its own assumptions.

I would also check whether I am passing too much irrelevant context. Even if the correct chunk is present, several noisy chunks can confuse the model.

If retrieval and prompt are both correct, then I would treat it as a **generation problem**. I could reduce temperature, test a stronger model, or ask for structured output if the response follows a fixed format.

For critical fields such as trade status, amount, or ID, I would validate the final answer against the source document or database.

So my debugging order would be:

**Check retrieval → check chunk/context → check prompt → remove noisy context → check generation → validate output.**

### Simple Flow

Correct Answer Exists in Documents
↓
Was Correct Chunk Retrieved?
↓
No → Fix Retrieval / Chunking
↓
Yes
↓
Does Chunk Have Enough Context?
↓
Check Prompt + Remove Noise
↓
LLM Generates Answer
↓
Validate Against Source

---

### Follow-up Questions

#### 1. What if the correct document is retrieved but the correct chunk is not?

Then I would treat it as a **chunking problem**.

The answer may have been split across chunk boundaries, or the chunks may be too large and diluted with unrelated information.

I would experiment with:
- smaller or larger chunk sizes
- chunk overlap
- heading-based chunking
- semantic chunking

Then I would evaluate whether the expected answer-containing chunk appears in the Top-K results.

---

#### 2. What if the correct chunk is in the Top-K but ranked very low?

Then retrieval is partially working, but the **ranking quality is weak**.

I would improve it using:
- a better embedding model
- hybrid search
- query rewriting
- metadata filtering
- a reranker

For example:

Vector Search → Top 20  
Reranker → Best 5  
LLM → Answer

This reduces the chance that irrelevant chunks dominate the context.

---

#### 3. Can too much context cause a wrong answer?

Yes.

More context does not always mean better accuracy.

If I send many irrelevant chunks along with the correct one, the LLM may focus on conflicting or unrelated information.

So I would keep the context focused and pass only the most relevant chunks.

This also helps reduce **latency and token cost**.

---

#### 4. How would you prove that the issue is with generation and not retrieval?

I would inspect the retrieved context manually or through evaluation.

If the correct answer is clearly present in the retrieved chunk, but the LLM still produces something unsupported or incorrect, then retrieval is working and the problem is mainly **prompting or generation**.

At that point, I would test:
- stricter grounding instructions
- lower temperature
- less noisy context
- structured output
- a stronger model

---

### Quick Revision

> If the answer exists but RAG is wrong, check in order: retrieval, chunk context, prompt, context noise, generation, then validate against the source.

## Q. How would you choose chunk size, overlap and chunking strategy?

### Interview Answer

I would choose chunking based on the **type of document and how users ask questions**, not by using one fixed size everywhere.

First, I would look at the document structure.

For example:
- FAQs or short knowledge articles can use smaller chunks.
- Technical documents or policies may need larger chunks so related information stays together.
- Structured documents with headings are usually better split by section or heading instead of only by character count.

For **chunk size**, I would start with a reasonable range and test it against real queries.

If chunks are too small, important context can get separated.

If chunks are too large, retrieval becomes less precise because one chunk may contain multiple unrelated topics.

For **overlap**, I use enough overlap to avoid losing information at chunk boundaries, but not too much because excessive overlap creates duplicate retrieval and increases storage and token cost.

For example, I may start with something like:

`500–800 tokens per chunk`  
`50–100 tokens overlap`

But I would treat these only as starting values, not fixed rules.

For the strategy itself, my production preference would usually be:

**Structure-aware or semantic chunking first, fixed-size chunking as a fallback.**

For example, if I have a settlement guide:

```text
1. Trade Matching
2. Settlement Instructions
3. Failure Handling
4. Reconciliation
```

## Q. How would you prevent the LLM from answering when the required information isn't available?

### Interview Answer

I would prevent guessing by adding a **confidence and evidence check before generation**.

In a RAG system, I would first retrieve the relevant chunks and check whether the retrieval score is good enough and whether the required information is actually present in the context.

If the evidence is weak or missing, I would **not call the LLM for a normal answer**. I would return a controlled fallback such as:

> "I don't have enough information in the available documents to answer this reliably."

I would also add a strict instruction in the prompt like:

> Answer only from the provided context. If the answer is not present, return `INSUFFICIENT_INFORMATION`.

For important use cases, I would not rely only on the prompt. I would also validate the output programmatically.

For example, if I expect an answer with a source citation, I can check whether the cited source actually contains the supporting information.

So in production, I would use multiple layers:

- Retrieval confidence threshold
- Strict grounding prompt
- Structured fallback response
- Source/citation validation
- Human review for critical cases

The important point is that **the system should be allowed to say "I don't know."**

That is much safer than forcing the LLM to always produce an answer.

### Simple Flow

User Query
↓
Retrieve Relevant Context
↓
Is Evidence Strong Enough?
↓
No → Return Safe Fallback
↓
Yes
↓
LLM Answers Only From Context
↓
Validate Source / Output
↓
Final Response

---

### Follow-up Questions

#### 1. Would you rely only on a similarity-score threshold?

No.

A similarity score is useful, but I would not use it as the only decision factor because a high similarity score does not always mean the chunk contains the exact answer.

I would combine it with things like:

- reranking score
- presence of required information
- metadata filters
- answer/source validation

The threshold should also be tuned using an evaluation dataset rather than chosen randomly.

---

#### 2. What if the LLM ignores the instruction and still answers?

Then I would add **application-level validation** instead of trusting the prompt alone.

For example, I can require structured output such as:

```json
{
  "answerable": false,
  "answer": null
}

```

## Q. How would you improve the accuracy of a production RAG system?

### Interview Answer

I would improve RAG accuracy by optimizing the pipeline in stages instead of only changing the LLM.

First, I would check **data quality**.

The knowledge base should contain correct, updated, non-duplicate documents with proper metadata. If the source data is poor, the final answer will also be poor.

Second, I would improve **chunking** based on the document type. I would use logical or heading-based chunks where possible and tune chunk size and overlap using real queries.

Third, I would improve **retrieval quality**.

I would check:
- embedding model
- Top-K value
- metadata filters
- hybrid search
- query rewriting
- reranking

For production, I would usually prefer **hybrid search + reranking** when the data contains both semantic content and exact keywords or IDs.

Then I would improve the **generation layer**.

I would give the LLM only the most relevant context and use a grounding prompt such as:

> Answer only from the provided context. If the answer is unavailable, say so.

I would also keep temperature low for factual use cases.

After that, I would add **validation and fallback**.

For critical fields, I can validate the answer against a database, API, business rule, or source document. If retrieval confidence is too low, I would return a safe fallback instead of allowing the model to guess.

Finally, I would create an **evaluation dataset** and measure retrieval and generation separately.

For example:

- Did the correct document appear in Top-K?
- Was the answer supported by the context?
- Was the final answer correct?
- How often did the system return unsupported answers?

So my production approach would be:

**Improve data → improve chunking → improve retrieval → rerank → ground the LLM → validate → continuously evaluate.**

### Simple Flow

User Query
↓
Query Processing
↓
Metadata Filter / Hybrid Search
↓
Top-K Results
↓
Reranker
↓
Best Context
↓
Grounded LLM
↓
Validation
↓
Final Answer / Safe Fallback

---

### Follow-up Questions

#### 1. What would you improve first: the model or retrieval?

I would usually improve **retrieval first**.

If the LLM does not receive the correct information, even a stronger model may still give the wrong answer.

So I would first check:

**Did we retrieve the correct document and chunk?**

Only after retrieval is working properly would I consider changing the LLM.

This is also usually more cost-effective than immediately moving to a larger model.

---

#### 2. How would you measure whether the RAG system actually improved?

I would maintain a **golden evaluation dataset** with known questions, expected answers, and expected source documents.

Then I would measure retrieval and generation separately.

For retrieval, I could check:

- Recall@K
- whether the correct chunk appears in Top-K

For generation, I would check:

- answer correctness
- faithfulness
- unsupported answer rate

I would also monitor real production feedback and failed queries.

This lets me compare the system before and after every change.

---

#### 3. Why would you use reranking if vector search already works?

Vector search is good for quickly finding semantically similar documents, but the highest similarity result is not always the most relevant one.

So I might retrieve:

```text
Vector Search → Top 20
Reranker → Best 5
LLM → Answer
