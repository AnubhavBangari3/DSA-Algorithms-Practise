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
```

## Q. How would you evaluate a RAG/GenAI application and know whether it is performing well?

### Interview Answer

I would evaluate a RAG or GenAI application at **multiple levels**, because one overall accuracy number is usually not enough.

For a RAG system, I would first separate **retrieval quality** from **generation quality**.

For retrieval, I would check whether the correct document or chunk appears in the Top-K results.

Typical metrics could be:

- Recall@K
- Precision@K
- Hit Rate
- MRR, if ranking order matters

Then I would evaluate the generated answer.

I would check:

- Is the answer correct?
- Is it actually supported by the retrieved context?
- Is it relevant to the user's question?
- Is it complete enough?
- Did the model hallucinate anything?

For this, I can use a **golden evaluation dataset** containing questions, expected answers, and expected source documents.

I can run this dataset whenever I change the model, prompt, chunking, embeddings, or retrieval strategy.

For large-scale evaluation, I can use an **LLM-as-a-judge** for things like faithfulness and relevance, but I would not depend on it alone. I would combine it with deterministic checks and human review.

In production, I would also monitor operational metrics such as:

- latency
- token usage and cost
- failure rate
- fallback rate
- user feedback
- unanswered queries

For a business-critical application, I would also track domain-specific correctness.

For example, if the system extracts settlement status or trade details, I would validate those fields against the actual database.

So I would say a RAG system is performing well when it has:

**good retrieval + faithful answers + low hallucination + acceptable latency/cost + good user or business outcomes.**

### Simple Flow

Evaluation Dataset
↓
Test Retrieval
↓
Was Correct Chunk Retrieved?
↓
Evaluate Generated Answer
↓
Correctness + Faithfulness + Relevance
↓
Check Latency / Cost / Failures
↓
Human + Production Feedback
↓
Improve and Re-test

---

### Follow-up Questions

#### 1. What is Recall@K?

Recall@K checks whether the correct document or chunk appears within the top K retrieved results.

For example, if the correct document appears within the Top 5 results, then that query is successful for Recall@5.

It helps me understand whether the retriever is actually finding the required information.

---

#### 2. What is the difference between correctness and faithfulness?

**Correctness** means the final answer is actually right.

**Faithfulness** means the answer is supported by the retrieved context.

For example, the model might accidentally give a correct answer from its own internal knowledge even though the retrieved documents do not support it.

That answer may be correct, but it is not faithful to the RAG context.

In production RAG, I want both.

---

#### 3. Would you use only automated evaluation?

No.

Automated evaluation is useful because it is fast and scalable, but I would combine it with **human review**, especially for critical use cases.

I would normally use:

- deterministic checks where possible
- automated metrics
- LLM-as-a-judge as an additional signal
- manual review on sampled or high-risk responses

This gives me a more reliable evaluation.

---

#### 4. How would you evaluate a GenAI application that is not using RAG?

Then I would focus more on task-specific output quality.

For example, I could measure:

- correctness
- relevance
- instruction following
- structured output validity
- safety
- consistency
- user satisfaction

If the application generates structured output, I can validate schema and business rules programmatically.

For open-ended tasks, I would use a mix of human evaluation and LLM-based evaluation.

---

### Quick Revision

> Evaluate RAG separately at retrieval and generation levels, then track faithfulness, correctness, hallucination, latency, cost, failures, and real business outcomes.


## Q. LLM response is too slow. How would you reduce latency?

### Interview Answer

I would first identify **where the latency is coming from** instead of assuming the LLM itself is the only problem.

I would break the request into stages:

- API/network time
- retrieval time
- reranking time
- prompt size
- LLM generation time
- post-processing time

Then I would optimize the slowest stage.

If the issue is with the **LLM call**, I would reduce the prompt size, remove unnecessary context, limit the output length, and use a faster model if the use case allows it.

For RAG, I would avoid sending too many chunks to the model. I may retrieve more candidates, rerank them, and then send only the best few chunks.

I would also use **streaming** so the user starts seeing the response immediately instead of waiting for the complete answer.

If the same queries or retrieved results are repeated often, I would use **caching**, for example Redis, for retrieval results or final responses where appropriate.

For independent operations, I can also run them **in parallel**. For example, if I need to call two independent tools or APIs, I would not call them sequentially.

I would also check infrastructure factors such as region, connection pooling, autoscaling, and rate-limit queues.

In production, I would monitor latency stage by stage using metrics like **p50, p95, and p99**, because average latency alone can hide slow requests.

So my approach would be:

**Measure first → reduce tokens/context → optimize retrieval → use faster model if needed → cache repeated work → parallelize independent operations → stream the response.**

The main trade-off is that some latency improvements can reduce answer quality, so I would optimize while keeping accuracy within an acceptable level.

### Simple Flow

User Request
↓
Measure Each Stage
↓
Retrieval / Tools / LLM
↓
Reduce Context + Optimize Calls
↓
Cache / Parallelize Where Possible
↓
Stream Response
↓
Monitor p95 Latency

---

### Follow-up Questions

#### 1. Would you always use a smaller model to reduce latency?

No.

A smaller model is usually faster and cheaper, but it may reduce reasoning or answer quality.

I would first optimize things like prompt size, context size, retrieval, and unnecessary calls.

If latency is still high, I would test a smaller model and compare:

**accuracy vs latency vs cost**

In production, I would choose the smallest model that still meets the quality requirement.

---

#### 2. How does reducing context improve latency?

A larger context means more tokens have to be processed before the model starts generating the answer.

So if I send 15 retrieved chunks when only 3 are relevant, I am increasing both latency and cost.

I would retrieve enough candidates for good recall, rerank them, and then send only the most relevant chunks to the LLM.

That improves both **speed and focus**.

---

#### 3. What would you cache in a GenAI application?

I could cache different layers depending on the use case.

For example:

- embedding results
- retrieval results
- repeated API/tool responses
- final LLM responses for identical or safe-to-reuse queries

Redis can be useful for this.

But I would use proper TTL and cache invalidation, especially when the underlying business data changes frequently.

I would not blindly cache sensitive or highly dynamic responses.

---

#### 4. Does streaming actually reduce LLM processing time?

Not necessarily.

Streaming usually does **not significantly reduce the total generation time**.

What it improves is **perceived latency**.

Instead of waiting 8 seconds and then seeing the full response, the user may start seeing tokens after 1–2 seconds.

So I would distinguish between:

**Time to First Token** and **Total Response Time**.

Both are useful production metrics.

---

### Quick Revision

> Reduce LLM latency by measuring the bottleneck first, shrinking context and output, optimizing retrieval, caching and parallelizing work, using the right model, and streaming for faster perceived response.

## Q. GenAI/LLM API cost is becoming too high. How would you optimize it?

### Interview Answer

First, I would identify **where the cost is coming from** instead of immediately switching models.

I would track things like:

- Number of LLM calls per request
- Input and output tokens
- Model being used
- RAG context size
- Repeated queries
- Agent/tool loops

Usually, the biggest optimization is to **avoid unnecessary LLM calls and unnecessary tokens**.

First, I would reduce the prompt and context size. In RAG, instead of sending many retrieved chunks, I would rerank them and send only the most relevant ones.

Second, I would use **model routing**.

Not every task needs the most powerful model. For example, simple classification, extraction, or summarization can use a smaller and cheaper model, while complex reasoning can go to a stronger model.

Third, I would add **caching** for repeated or reusable results. For example, embeddings, retrieval results, tool/API results, or safe repeated LLM responses can be cached using Redis.

I would also check whether my application is making duplicate calls. In an agentic system, poorly controlled retries or loops can generate a lot of unnecessary API usage, so I would set retry limits and termination conditions.

I would also limit output tokens. If the application only needs a short answer or structured JSON, I would not allow the model to generate a very long response.

For large offline workloads, if the provider supports batch processing at a lower cost, I would consider that as well.

Finally, I would monitor metrics like:

**cost per request, tokens per request, cost per user, and cost per successful task.**

My goal would not simply be to use the cheapest model. It would be to get the **required accuracy at the lowest reasonable cost**.

### Simple Flow

User Request
↓
Can Cache Answer?
↓
Yes → Return Cached Result
↓
No
↓
Choose Appropriate Model
↓
Retrieve Only Relevant Context
↓
LLM with Token Limits
↓
Return Response
↓
Track Cost + Quality

---

### Follow-up Questions

#### 1. Would you always switch to a smaller model to reduce cost?

No.

A smaller model may reduce cost, but it can also reduce accuracy.

I would use **model routing** instead.

For example:

```text
Simple extraction/classification
        ↓
Small Model

Complex reasoning
        ↓
Stronger Model

```

## Q. When would you use RAG vs fine-tuning?

### Interview Answer

I would choose between RAG and fine-tuning based on **what I am trying to change: the model's knowledge or its behavior**.

I would use **RAG when the model needs access to external, private, or frequently changing information**.

For example, if I am building an assistant that answers questions about company policies, trade data, product documentation, or support knowledge, I would use RAG.

The documents can change regularly, so I can update the knowledge base without retraining the model.

RAG also allows me to provide **citations and source references**, which is important for factual applications.

I would use **fine-tuning when I want to change how the model behaves**, rather than continuously update its knowledge.

For example, if I want the model to consistently produce a specific response format, follow a particular writing style, classify domain-specific inputs, or perform a specialized task repeatedly, fine-tuning can be useful.

A simple way I remember it is:

**RAG = give the model the right knowledge at runtime.**  
**Fine-tuning = teach the model a better behavior or task pattern.**

For most enterprise knowledge assistants, I would start with **RAG**, because company data changes and needs to remain traceable.

If necessary, I can also combine both.

For example, I could fine-tune a model for a specialized task or behavior and still use RAG to provide current business information.

So they are not necessarily competing approaches.

---

### Simple Flow

```text
Need current/private knowledge?
        ↓
       RAG

Need specialized behavior/style/task?
        ↓
   Fine-Tuning

Need both?
        ↓
Fine-Tuned Model + RAG

```

## Q. When would you use an AI Agent instead of normal RAG/LLM?

### Interview Answer

I would use an **AI Agent when the system needs to make decisions, use tools, and perform multiple steps dynamically**, instead of only generating an answer.

A normal **LLM** is enough when I need tasks like summarization, generation, extraction, or classification.

I would use **RAG** when the main requirement is to retrieve external or private knowledge and answer questions based on that information.

But I would use an **Agent** when the workflow is:

**Understand the goal → decide what to do → choose a tool → execute it → check the result → decide the next step.**

For example, suppose the user says:

> "Investigate why Trade 123 failed and create a support ticket if action is required."

Here, the system may need to:

1. Get trade details from the database.
2. Check the latest settlement status through an API.
3. Use RAG to retrieve relevant settlement documentation.
4. Analyze the failure reason.
5. Decide whether a ticket is required.
6. Create the ticket using an API.
7. Return the RCA and ticket ID.

Since the next step depends on the result of the previous step, an **agentic workflow makes sense**.

In production, I would give the agent only controlled tools, maintain state between steps, define retries and termination conditions, and validate important actions.

For sensitive actions such as payments, deleting data, or sending important communications, I would add **human approval before execution**.

I would not use an agent for every GenAI problem because agents introduce additional **latency, cost, complexity, and failure points**.

So my simple rule is:

**LLM = generate or understand.**  
**RAG = retrieve knowledge and answer.**  
**Agent = decide, use tools, and take actions.**

### Simple Flow

```text
User Request
     ↓
   Agent
     ↓
Understand Goal
     ↓
Decide Next Action
     ↓
Choose Tool
     ↓
┌─────────────────┐
│ RAG             │
│ Database        │
│ API             │
│ External Tools  │
└─────────────────┘
     ↓
Execute Tool
     ↓
Observe Result
     ↓
Need Another Action?
   ↙           ↘
 Yes           No
  ↓             ↓
Next Step    Final Response
```

---

### Follow-up Questions

#### 1. What is the difference between an Agent and RAG?

RAG is mainly used to **retrieve external knowledge and give that context to an LLM**.

```text
Question
↓
Retrieve Documents
↓
LLM
↓
Answer
```

An Agent can **make decisions and perform actions using different tools**.

```text
Goal
↓
Decide Action
↓
Choose Tool
↓
Execute
↓
Observe Result
↓
Decide Next Action
```

An important point is that an agent can actually use **RAG as one of its tools**.

So RAG provides knowledge, while an agent orchestrates decisions and actions.

---

#### 2. What components would you normally have in an AI Agent?

For a production agent, I would normally consider:

- **LLM** – understands the request and helps decide actions.
- **Tools** – APIs, databases, RAG, search, etc.
- **State** – stores information between workflow steps.
- **Conditional decisions** – decides the next step based on previous results.
- **Retries and error handling** – handles temporary failures.
- **Termination conditions** – prevents infinite loops.
- **Human-in-the-loop** – approval for sensitive actions.

For example, the state could contain:

```text
trade_id = 123
status = "FAILED"
reason = "Insufficient Securities"
ticket_created = false
```

The agent uses this state while moving through the workflow.

---

#### 3. How would you prevent an Agent from running forever?

I would never allow an unrestricted agent loop in production.

I would define controls such as:

- Maximum number of steps
- Maximum retries
- Tool timeouts
- Overall workflow timeout
- Clear success and failure termination conditions

For example:

```text
Maximum Steps = 10
Tool Retries = 2
Overall Timeout = 30 seconds
```

If the agent still cannot complete the task, I would terminate the workflow and return a controlled fallback or send it for human review.

This also prevents unnecessary LLM API cost.

---

#### 4. When would you NOT use an Agent?

I would not use an agent when the workflow is **simple or deterministic**.

For example:

> "Summarize this document."

A normal LLM is enough.

Or:

> "What does our settlement failure policy say?"

RAG is enough.

I don't need an agent with planning and multiple tool calls for these cases.

Agents introduce additional:

- Latency
- Cost
- Complexity
- Failure points

So I would use an agent only when the application genuinely requires **dynamic decisions, multiple tools, or actions**.

---

### Quick Revision

> LLM generates, RAG retrieves knowledge and answers, while an Agent dynamically decides what to do, uses tools, maintains state, and takes multi-step actions.

```

## Q. Agent is choosing the wrong tool. How would you fix it?

### Interview Answer

If an agent is choosing the wrong tool, I would first check **why the tool selection is ambiguous**.

Usually, the problem comes from one of these areas:

- Tool descriptions are unclear or overlapping.
- The prompt does not clearly define when each tool should be used.
- Too many similar tools are exposed to the agent.
- The user query is ambiguous.
- There is no validation before executing the selected tool.

First, I would improve the **tool definitions and descriptions**.

For example, instead of defining a tool as:

```text
get_data()
```

I would define it more clearly as:

```text
get_trade_status(trade_id)

Use only when the user wants the latest trade settlement status.
Do not use this tool for policy or documentation questions.
```

The clearer the tool purpose, inputs, and limitations are, the easier it is for the agent to choose correctly.

Second, I would improve the routing instructions.

For example:

```text
Trade status → Database/API tool
Settlement policy → RAG tool
Create incident → Ticket API
```

If tool selection is business-critical, I would not rely entirely on free-form LLM reasoning.

I could introduce a **routing or classification step** before tool execution.

For example:

```text
User Query
↓
Intent Classification
↓
Select Allowed Tool
↓
Execute
```

I would also validate tool arguments before execution.

For sensitive actions, I would add confirmation or human approval.

Finally, I would collect cases where the wrong tool was selected and add them to an evaluation dataset. Then I could test tool-selection accuracy whenever I change the prompt, model, or tool descriptions.

So my production approach would be:

**Clarify tool descriptions → reduce overlap → improve routing → validate before execution → evaluate failed cases.**

### Simple Flow

```text
User Request
↓
Identify Intent
↓
Select Candidate Tool
↓
Validate Tool + Arguments
↓
Correct Tool?
   ↓
Yes → Execute
   ↓
No → Re-route / Fallback
↓
Observe Result
```

---

### Follow-up Questions

#### 1. Would you let the LLM freely choose from every available tool?

Not always.

If I have only a few simple and clearly different tools, direct tool selection by the LLM may be enough.

But if I have many tools or high-risk actions, I would restrict the available tools based on the current workflow or intent.

For example:

```text
User is asking about trade information
↓
Allowed tools:
- get_trade
- get_settlement_status
- RAG search
```

I would not expose unrelated tools such as:

```text
delete_user
send_payment
create_admin
```

Reducing the tool set improves accuracy and also improves security.

---

#### 2. What if two tools have very similar functionality?

I would either **combine them** or make their responsibilities very clear.

For example, instead of:

```text
search_trade()
find_trade()
get_trade()
```

I would preferably expose one well-defined tool:

```text
get_trade(trade_id)
```

If separate tools are genuinely needed, their descriptions should clearly state when each one should be used.

Overlapping tools create unnecessary ambiguity for the LLM.

---

#### 3. How would you measure whether tool selection improved?

I would create an evaluation dataset containing:

```text
User Query
Expected Tool
Expected Arguments
```

For example:

```text
Query:
"What is the settlement status of Trade 123?"

Expected Tool:
get_settlement_status

Expected Argument:
trade_id = 123
```

Then I would measure:

- Tool-selection accuracy
- Argument accuracy
- Invalid tool-call rate
- Tool execution failure rate

I would also log production cases where the agent selected the wrong tool and add those examples to future evaluations.

---

#### 4. What if the correct tool is selected but wrong arguments are passed?

Then I would treat it as an **argument extraction and validation problem** rather than a tool-selection problem.

I would use structured schemas for tool inputs.

For example:

```json
{
  "trade_id": "string",
  "date": "YYYY-MM-DD"
}
```

Before executing the tool, I would validate:

- Required fields
- Data types
- Allowed values
- Permissions

If important information is missing, I would ask for clarification instead of guessing.

---

### Quick Revision

> Wrong tool selection is usually fixed by clearer tool descriptions, fewer overlapping tools, explicit routing, input validation, and testing tool-selection accuracy with real examples.

```

## Q. Agent is choosing the wrong tool. How would you fix it?

### Interview Answer

If an agent is choosing the wrong tool, I would first identify **why the tool choice is ambiguous**.

Usually, the issue is one of these:

- Tool descriptions are unclear.
- Multiple tools have overlapping responsibilities.
- The prompt does not clearly say when each tool should be used.
- Too many tools are exposed at once.
- Tool arguments are not being validated.

First, I would improve the **tool descriptions**.

For example, instead of:

```text
get_data()
```

I would define:

```text
get_trade_status(trade_id)

Use this tool only to get the latest settlement status of a trade.
Do not use it for policy or documentation questions.
```

This makes the decision boundary much clearer for the model.

Second, I would reduce overlapping tools.

For example, if I have:

```text
search_trade()
find_trade()
get_trade()
```

I would either combine them or clearly separate their responsibilities.

Third, if I have many tools, I would add a **routing step** before execution.

For example:

```text
Trade status question → Trade API
Policy question → RAG
Create support ticket → Ticket API
```

For important workflows, I would also validate the selected tool and its arguments before actually executing it.

If the action is sensitive, I would add a human approval step.

Finally, I would log incorrect tool selections and create an evaluation dataset like:

```text
User Query
Expected Tool
Expected Arguments
```

Then I can measure whether changes to the prompt, tool descriptions, or model actually improved tool-selection accuracy.

So my production approach would be:

**Clear tool descriptions → remove overlap → restrict available tools → validate selection and arguments → evaluate failed cases.**

### Simple Flow

```text
User Request
↓
Understand Intent
↓
Filter Relevant Tools
↓
Choose Tool
↓
Validate Tool + Arguments
↓
Execute
↓
Check Result
↓
Retry / Fallback if Needed
```

---

### Follow-up Questions

#### 1. Would you let the LLM see every tool available in the system?

No, not always.

If there are only a few clearly different tools, that may be fine.

But if I have many tools, I would expose only the tools relevant to the current intent or workflow.

For example:

```text
User asks about settlement status

Allowed tools:
- get_trade
- get_settlement_status
- search_settlement_docs
```

I would not expose unrelated tools.

This improves tool-selection accuracy and also reduces security risk.

---

#### 2. What if two tools are very similar?

I would first check whether I actually need both.

If possible, I would combine them into one clear tool.

For example:

```text
search_trade()
find_trade()
get_trade()
```

could become:

```text
get_trade(trade_id)
```

If both tools are required, I would make the descriptions and input conditions clearly different.

The model should understand exactly when to use each one.

---

#### 3. What if the agent chooses the correct tool but passes wrong arguments?

Then I would treat that as an **argument validation problem**.

I would define a strict schema.

For example:

```json
{
  "trade_id": "string",
  "date": "YYYY-MM-DD"
}
```

Before tool execution, I would validate:

- required fields
- data types
- allowed values
- permissions

If something important is missing, I would ask for the missing information rather than allowing the agent to guess.

---

#### 4. How would you measure tool-selection accuracy?

I would create a small test dataset containing:

```text
User Query
Expected Tool
Expected Arguments
```

For example:

```text
Query:
"What is the settlement status of Trade 123?"

Expected Tool:
get_settlement_status

Expected Arguments:
trade_id = 123
```

Then I would track:

- Tool-selection accuracy
- Argument accuracy
- Invalid tool-call rate
- Tool execution failure rate

I would also add real production failures to this dataset so the evaluation keeps improving over time.

---

### Quick Revision

> Fix wrong tool selection by making tool boundaries clear, reducing overlapping tools, restricting the available tool set, validating arguments, and testing against real tool-routing examples.

```

## Q. Agent gets stuck in a loop or repeatedly calls tools. How would you handle it?

### Interview Answer

If an agent gets stuck in a loop, I would first identify **why it keeps repeating the same action**.

Common reasons could be:

- No clear termination condition.
- The tool keeps failing and the agent keeps retrying.
- The agent is not maintaining state properly.
- The tool result is unclear, so the agent thinks it needs to call it again.
- There is no maximum step or retry limit.

First, I would define **clear termination conditions**.

The agent should know exactly when the task is successful, when it has failed, and when it should stop.

Second, I would add hard safety limits such as:

```text
Maximum agent steps = 10
Maximum retries per tool = 2
Tool timeout = 10 seconds
Overall workflow timeout = 30 seconds
```

These values would be tuned for the actual use case.

Third, I would maintain **state and tool-call history**.

Before calling a tool, the agent can check whether the same tool has already been called with the same arguments and whether anything has changed.

For example:

```text
get_trade_status(trade_id=123)
↓
Already called with same input
↓
No new information available
↓
Do not call again
```

For tool failures, I would use controlled retries, preferably with **backoff** for temporary failures.

If the same tool keeps failing, I would stop retrying and use a fallback instead of allowing an infinite loop.

For example:

```text
API fails
↓
Retry 1
↓
Retry 2
↓
Still fails
↓
Stop → Fallback / Human Review
```

I would also log the full agent trace — tool calls, arguments, results, retries, and termination reason — so I can understand why loops are happening in production.

So my production approach would be:

**Clear termination conditions → step limits → retry limits → state/history → duplicate-call detection → timeout → fallback.**

### Simple Flow

```text
Agent Starts
↓
Choose Action
↓
Has Same Action Already Been Tried?
↓
Yes → Re-evaluate / Choose Another Action
↓
No
↓
Execute Tool
↓
Success?
├── Yes → Update State → Goal Completed?
│                         ├── Yes → STOP
│                         └── No → Next Step
│
└── No → Retry Limit Reached?
          ├── No → Retry with Backoff
          └── Yes → Fallback / Human Review
```

---

### Follow-up Questions

#### 1. What is a termination condition in an AI Agent?

A termination condition defines **when the agent should stop executing**.

For example:

```text
Goal:
Investigate failed trade and create ticket.

Termination conditions:

Success:
RCA generated AND ticket created

Failure:
Required trade information unavailable

Safety:
Maximum 10 agent steps reached
```

Without clear termination conditions, the model may continue trying different actions even though the workflow is already finished or cannot be completed.

---

#### 2. How would you detect repeated tool calls?

I would maintain the **tool-call history in the agent state**.

For example:

```json
{
  "tool": "get_trade_status",
  "arguments": {
    "trade_id": "123"
  },
  "result": "FAILED"
}
```

Before executing another call, I can check:

```text
Same Tool + Same Arguments + No State Change?
↓
Yes
↓
Don't Execute Again
```

The agent can then choose another action or terminate.

This also saves latency and LLM/tool cost.

---

#### 3. When should an Agent retry a failed tool?

I would retry mainly for **temporary failures**.

For example:

```text
Timeout
503 Service Unavailable
Temporary network failure
Rate limit
```

I could retry these with controlled backoff.

But if the error is permanent, such as:

```text
Invalid trade ID
Permission denied
Invalid request
```

repeating the same call will not help.

I would stop and either request corrected information or return a controlled failure.

---

#### 4. What would you do if the maximum agent steps are reached?

I would immediately terminate the workflow instead of allowing additional execution.

Then depending on the use case, I could:

- Return a safe fallback.
- Ask the user for additional information.
- Escalate to human review.
- Store the execution trace for debugging.

For example:

```text
Maximum Steps Reached
↓
Stop Agent
↓
Save Trace
↓
Fallback / Human Review
```

I would never let the agent continue indefinitely because that can create **high cost, latency, and potentially unsafe actions**.

---

### Quick Revision

> Prevent agent loops using clear termination conditions, state and tool history, duplicate-call detection, retry and step limits, timeouts, and a safe fallback.

```
## Q. How would you design a workflow where the AI takes different actions based on conditions?

### Interview Answer

I would design it as a **stateful workflow with clear conditional branches**.

First, I would define the shared **state** that moves through the workflow.

For example:

```text
trade_id
trade_status
failure_reason
ticket_required
ticket_id
```

Then I would break the workflow into small steps or nodes.

For example:

```text
Get Trade Details
↓
Check Status
↓
Analyze Failure
↓
Decide Next Action
```

The next step would depend on the current state.

For example:

```text
If status = SETTLED
→ Return success

If status = FAILED
→ Analyze failure

If failure needs manual action
→ Create ticket

If information is missing
→ Ask for input or send for human review
```

For conditions that are simple and deterministic, I would use normal Python logic.

For example:

```python
if trade_status == "SETTLED":
    return "complete"
elif trade_status == "FAILED":
    return "investigate"
```

I would use the LLM only where reasoning is actually needed, such as understanding an unstructured error message or generating a root-cause summary.

For a workflow with multiple branches, retries, and state, I could use **LangGraph** because it supports nodes, edges, conditional routing, loops, and state management.

In production, I would also add:

- Retry limits
- Timeouts
- Fallback paths
- Termination conditions
- Human approval for sensitive actions

So my preferred approach is:

**State → condition check → choose branch → execute action → update state → validate → stop when the goal is complete.**

### Simple Flow

```text
User Request
↓
Initialize State
↓
Get Trade Details
↓
Check Status
↓
      ┌──────────────────────┐
      │                      │
   SETTLED                 FAILED
      │                      │
Return Success         Analyze Failure
                             ↓
                     Ticket Required?
                       ↙          ↘
                     Yes          No
                      ↓            ↓
                Create Ticket    Return RCA
                      ↓
                   Validate
                      ↓
                     STOP
```

---

### Follow-up Questions

#### 1. Why would you use LangGraph here?

I would use LangGraph when the workflow is not simply linear.

For example:

```text
Step A
↓
Check Condition
↙          ↘
Step B    Step C
```

LangGraph is useful because it supports:

- Shared state
- Conditional edges
- Multiple branches
- Retries
- Cycles
- Termination conditions

For a very simple fixed workflow, normal Python or a simple chain would be enough.

---

#### 2. Should the LLM decide every condition?

No.

If the condition is deterministic, I would use normal code.

For example:

```python
if amount > 10000:
    require_approval = True
```

This is faster, cheaper, and more reliable than asking an LLM to decide it.

I would use the LLM only for conditions that need semantic understanding or reasoning.

---

#### 3. How would you maintain state in this workflow?

I would keep a structured state object and update it after every step.

For example:

```json
{
  "trade_id": "TR123",
  "status": "FAILED",
  "failure_reason": "Insufficient securities",
  "ticket_required": true,
  "ticket_id": null
}
```

Each node reads what it needs from the state and updates the relevant fields.

For long-running workflows, I could persist the state using a database or checkpoint mechanism so the workflow can resume after failure.

---

#### 4. What if one branch fails?

I would define error handling at that step.

For temporary failures:

```text
Tool Failure
↓
Retry with Limit
```

For permanent failures:

```text
Invalid Data / Permission Error
↓
Fallback / Human Review
```

I would also preserve the current state and execution trace so I can debug the failure without restarting the full workflow.

---

### Quick Revision

> Use shared state and conditional branches, keep simple decisions deterministic, use the LLM only for reasoning, and add retries, fallbacks, and clear termination conditions.

```
## Q. LLM output must always follow a specific JSON/schema. How would you guarantee it?

### Interview Answer

If the output must always follow a specific schema, I would **not rely only on prompt instructions**.

My production approach would be:

**Define schema → use structured output/function calling → validate programmatically → retry or fallback if invalid.**

First, I would define the expected schema clearly.

For example:

```json
{
  "trade_id": "string",
  "status": "string",
  "reason": "string",
  "confidence": "number"
}
```

Then, if the model/provider supports **structured output or function/tool calling with a schema**, I would use that instead of asking:

```text
"Please return valid JSON."
```

That gives much stronger control over the response format.

After receiving the output, I would still validate it in the application.

For example, in Python I could use **Pydantic** or JSON Schema validation to check:

- Required fields
- Data types
- Allowed values
- Missing fields
- Extra fields if they are not allowed

For example, if status must only be:

```text
PENDING
FAILED
SETTLED
```

I would validate that rather than accepting any random string.

If validation fails, I could do one controlled retry with the validation error included.

If it still fails, I would return a safe fallback instead of passing malformed data further into the system.

For critical workflows, I would also validate the **business meaning**, not just the JSON structure.

For example, valid JSON does not mean the information itself is correct.

So my production approach is:

**Structured generation + schema validation + business validation + limited retry + fallback.**

### Simple Flow

```text
User/Input
↓
LLM with Structured Output Schema
↓
JSON Response
↓
Schema Validation
↓
Valid?
├── Yes → Business Validation → Use Output
│
└── No → Retry Once
            ↓
         Still Invalid?
            ↓
         Fallback / Error
```

---

### Follow-up Questions

#### 1. Is asking the LLM to "return JSON only" enough?

No.

That can work in simple cases, but it does not guarantee that the response will always be valid.

The model could still return:

```text
Here is your JSON:

{
  ...
}
```

or generate missing fields or wrong data types.

So in production, I would prefer **native structured output/function calling** plus programmatic schema validation.

---

#### 2. What would you use in Python to validate the schema?

I would commonly use **Pydantic**.

For example:

```python
from pydantic import BaseModel
from typing import Literal

class TradeResult(BaseModel):
    trade_id: str
    status: Literal["PENDING", "FAILED", "SETTLED"]
    reason: str
    confidence: float
```

Then I can validate the LLM response before using it.

This protects the rest of the application from malformed or unexpected output.

---

#### 3. What if the JSON is valid but the information inside it is wrong?

Then schema validation alone is not enough.

For example:

```json
{
  "trade_id": "TR123",
  "status": "SETTLED"
}
```

This may be perfectly valid JSON, but the actual database may say the trade is `FAILED`.

So after schema validation, I would apply **business validation**.

For example:

```text
Schema Valid
↓
Check trade_id in database
↓
Verify status/source
↓
Accept Response
```

Structure correctness and factual correctness are two separate checks.

---

#### 4. What would you do if validation keeps failing?

I would use a limited retry strategy.

For example:

```text
LLM Output
↓
Validation Failed
↓
Retry with Validation Error
↓
Still Invalid
↓
Stop
↓
Fallback / Error Handling
```

I would not retry indefinitely because that increases latency and cost.

I would also log these failures so I can improve the prompt, schema, or model configuration later.

---

### Quick Revision

> Don't trust prompt-only JSON: use structured output, validate with a schema like Pydantic, validate business rules too, and retry or fallback when validation fails.


## Q. LLM API fails or becomes unavailable. How would you design the application?

### Interview Answer

I would design the application so that an LLM failure does **not crash the whole user flow**.

First, I would classify the failure.

It could be:

- Timeout
- Rate limit
- Temporary provider issue
- Authentication/configuration issue
- Invalid request
- Complete provider outage

For temporary failures, I would use **limited retries with exponential backoff**.

For example:

```text
Attempt 1
↓
Wait briefly
↓
Attempt 2
↓
Wait longer
↓
Attempt 3
```

But I would not retry every error.

For something like invalid credentials or a bad request, retrying will not help.

Second, I would add **timeouts** so one slow LLM call does not block the request indefinitely.

Then I would add a **fallback strategy**.

Depending on the application, this could mean:

- Use another configured model/provider
- Use a smaller backup model
- Return a cached response
- Return retrieved documents without LLM generation
- Give a controlled message saying the AI service is temporarily unavailable

For example, in a RAG application, even if generation fails, I may still be able to show the user the most relevant source documents.

For critical workflows, I would also make sure that the system can continue using **normal business logic** where possible instead of depending on the LLM for everything.

I would add a **circuit breaker** as well. If the LLM provider is continuously failing, I would temporarily stop sending new requests to it instead of repeatedly wasting time and resources.

Finally, I would monitor:

- LLM error rate
- Timeout rate
- Retry count
- Provider availability
- Fallback usage
- Latency

So my production approach would be:

**Timeout → controlled retry → fallback → circuit breaker → monitoring.**

The main idea is to design the LLM as one dependency of the system, not as a single point of failure.

### Simple Flow

```text
User Request
↓
Call LLM
↓
Success?
├── Yes → Validate → Return Response
│
└── No
     ↓
Temporary Error?
├── Yes → Retry with Backoff
│           ↓
│        Still Fails?
│           ↓
│        Fallback Model / Cached Result
│
└── No → Controlled Fallback
             ↓
       Log + Monitor Failure
```

---

### Follow-up Questions

#### 1. What is exponential backoff?

Exponential backoff means increasing the delay between retries instead of retrying immediately.

For example:

```text
First failure  → wait 1 second
Second failure → wait 2 seconds
Third failure  → wait 4 seconds
```

I would normally also add some randomness, or **jitter**, so many application instances do not retry at exactly the same time.

This is useful for temporary failures such as rate limits or service overload.

---

#### 2. What is a circuit breaker?

A circuit breaker prevents the application from repeatedly calling a dependency that is already failing.

For example:

```text
LLM failures cross threshold
↓
Circuit Opens
↓
Stop calling provider temporarily
↓
Use fallback
↓
After some time, test provider again
↓
Healthy → Resume normal calls
```

This protects the application from increased latency and unnecessary retries during an outage.

---

#### 3. Would you always switch to another LLM provider as a fallback?

No.

A second provider can improve availability, but it also introduces complexity.

Different models may have:

- Different output formats
- Different capabilities
- Different prompts
- Different tool-calling behavior
- Different cost

So I would use multi-provider fallback only when the business availability requirement justifies it.

For a less critical application, a controlled error message or cached response may be enough.

---

#### 4. What if an LLM fails in the middle of an Agent workflow?

I would persist the current **agent state** so I do not lose all previous work.

For example:

```json
{
  "trade_id": "TR123",
  "status_checked": true,
  "failure_reason_found": true,
  "ticket_created": false
}
```

Then I could retry only the failed step instead of restarting the complete workflow.

I would also define retry limits and a fallback path.

For sensitive or important workflows, if the AI step cannot recover, I would send it for **human review** rather than continuing with an uncertain decision.

---

### Quick Revision

> Treat the LLM as a dependency, not a single point of failure: use timeouts, limited retries with backoff, fallbacks, circuit breakers, state recovery, and monitoring.

```