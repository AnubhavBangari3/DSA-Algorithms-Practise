## Q. Your LLM is hallucinating. How would you reduce it?

### Interview Answer

First, I would identify **where the hallucination is coming from** instead of directly changing the model.

In production, I usually separate it into four areas:

1. **Retrieval problem** – the correct information is not being fetched.
2. **Data/chunking problem** – the knowledge base has poor, outdated, or badly chunked data.
3. **Prompt problem** – the model is not clearly instructed to stay within the provided context.
4. **Generation problem** – the model is still inventing information even when the context is correct.

If it is a knowledge-based application, my preferred production approach would be **RAG with strict grounding**.

I would retrieve relevant documents from a trusted knowledge base, pass only the useful context to the LLM, and explicitly instruct it:

> Answer only from the provided context. If the information is not available, say that you don't know.

Then I would improve retrieval quality using good chunking, embeddings, Top-K tuning, metadata filters, and reranking if required.

I would also keep the **temperature low** for factual use cases because I want consistency rather than creativity.

For important outputs, I would add validation. For example, if the LLM extracts an amount, date, status, or trade ID, I can validate that value against the database or source document before returning it.

I would also return **citations or source references** so the user can see where the answer came from.

If confidence is low or no relevant document is found, I would prefer a safe fallback such as:

"Information is not available in the provided data."

instead of allowing the model to guess.

Finally, I would monitor hallucination cases in production, store failed queries, and continuously improve the retrieval, prompt, and knowledge base.

So my overall approach is:

**Ground the model → improve retrieval → constrain generation → validate critical outputs → monitor failures.**

### Simple Flow

User Query
↓
Retrieve Trusted Context
↓
Check Retrieval Quality
↓
LLM with Strict Grounding Prompt
↓
Validate Critical Information
↓
Return Answer + Source
↓
Fallback if Confidence is Low

### Follow-up Questions

1. What would you do if the retrieved documents themselves contain incorrect information?
2. How would you measure hallucination in a RAG application?
3. Does lowering temperature completely remove hallucination?
4. What would you do if RAG retrieves the correct document but the LLM still gives the wrong answer?

### Quick Revision

> Reduce hallucination by grounding the LLM with trusted context, improving retrieval, constraining the prompt, validating important outputs, and using a safe fallback instead of guessing.