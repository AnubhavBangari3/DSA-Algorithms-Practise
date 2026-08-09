# RAG — Interview Cheat Sheet

## 1. What is RAG?

**RAG stands for Retrieval-Augmented Generation.**

It retrieves relevant information from an external knowledge base and gives that information as context to the LLM before generating the answer.

```text
User Question
      ↓
Retrieve Relevant Data
      ↓
Give Context to LLM
      ↓
Generate Answer
```

**Interview Answer:**

> RAG combines retrieval with LLM generation. Instead of depending only on the LLM's training knowledge, we retrieve relevant information from our documents and provide it as context to generate a more accurate and grounded answer.

---

# 2. Why Do We Use RAG?

Main reasons:

* Use private/company data
* Use latest information
* Reduce hallucination
* Improve domain-specific answers
* No need to retrain the LLM when documents change
* Can provide source citations

**Example:**

If an HR document says:

```text
Employees receive 20 annual leaves.
```

The LLM may not know this private information.

RAG retrieves this policy and gives it to the LLM before answering.

**Interview Answer:**

> I use RAG when the LLM needs access to private, domain-specific, or frequently updated information. It helps ground the answer using actual documents and reduces hallucination without retraining the model.

---

# 3. RAG Architecture

RAG has two major flows:

### A. Indexing / Ingestion

```text
Documents
   ↓
Clean
   ↓
Chunk
   ↓
Create Embeddings
   ↓
Store in Vector DB
```

### B. Retrieval / Generation

```text
User Question
   ↓
Query Embedding
   ↓
Search Vector DB
   ↓
Retrieve Top-K Chunks
   ↓
Optional Reranking
   ↓
Question + Context
   ↓
LLM
   ↓
Answer
```

**Interview Answer:**

> First, I load and clean the documents, split them into chunks, create embeddings and store them in a vector database. When the user asks a question, I create its embedding, retrieve the Top-K similar chunks, optionally rerank them, and send the relevant context with the question to the LLM.

---

# 4. What are Embeddings?

Embeddings are **numerical vector representations of text that capture semantic meaning**.

```text
"How many leaves do I get?"
        ↓
Embedding Model
        ↓
[0.21, -0.45, 0.78, ...]
```

They allow us to compare text based on **meaning**, not only exact words.

Example:

```text
"annual leave"
"vacation days"
```

Different words, but similar meaning → embeddings should be close.

**Interview Answer:**

> Embeddings convert text into numerical vectors representing semantic meaning. In RAG, I create embeddings for document chunks and the user query, then compare them to find relevant chunks.

---

# 5. What is a Vector Database?

A Vector DB stores embeddings and performs fast similarity search.

Examples:

* Qdrant
* Pinecone
* Chroma
* Weaviate
* FAISS
* Azure AI Search

Usually we store:

```text
Embedding
+
Original Chunk
+
Metadata
```

Example metadata:

```text
document_name
page_number
category
date
```

**Interview Answer:**

> A vector database stores document embeddings and allows us to quickly retrieve vectors that are most similar to the user's query embedding.

---

# 6. What is Chunking?

Chunking means dividing large documents into smaller pieces before creating embeddings.

```text
Large PDF
   ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
   ↓
Embeddings
```

### Why chunk?

* Better retrieval
* More focused embeddings
* Less unnecessary context
* Lower token usage
* Fits LLM context window

---

# 7. Chunk Size and Overlap

### Chunk Size

Amount of text inside one chunk.

Example:

```text
Chunk Size = 500 tokens
```

### Chunk Overlap

Some text from the previous chunk is repeated in the next chunk.

Example:

```text
Chunk Size = 500
Overlap = 50
```

Why overlap?

It prevents context from being lost when important information lies between two chunks.

**Interview Answer:**

> Chunk size controls how much text each chunk contains, while overlap keeps some shared text between consecutive chunks so context is not lost at chunk boundaries.

There is **no universal best chunk size**. It should be tested based on document type and retrieval quality.

---

# 8. Types of Chunking

## Fixed-Size Chunking

Split after a fixed number of tokens or characters.

```text
500 tokens
500 tokens
500 tokens
```

**Pros:** Simple and fast.

**Cons:** Can split sentences or topics incorrectly.

---

## Recursive Chunking

Tries to split using natural separators such as:

```text
Paragraph
↓
Sentence
↓
Word
```

It preserves document structure better than simple fixed splitting.

**Interview Answer:**

> Recursive chunking tries larger natural boundaries like paragraphs first and moves to smaller separators if required.

---

## Semantic Chunking

Splits text when the **meaning/topic changes**.

Example:

```text
Leave Policy
-----------
one chunk

Salary Policy
-----------
another chunk
```

**Pros:** Better semantic grouping.

**Cons:** More expensive and complex.

---

# 9. Dense Retrieval

Dense retrieval uses **embeddings**.

```text
Query
 ↓
Embedding
 ↓
Vector Similarity Search
 ↓
Relevant Chunks
```

It searches based on **meaning**.

Example:

```text
Query: "Why did my trade fail?"

Document:
"Settlement was unsuccessful due to insufficient securities."
```

Dense retrieval can understand their semantic similarity.

**Remember:**

> Dense = Embeddings + Meaning

---

# 10. Sparse Retrieval / BM25

Sparse retrieval is mainly **keyword-based retrieval**.

BM25 is a commonly used sparse retrieval algorithm.

Useful for exact terms such as:

```text
MT548
Trade ID
Error Code
Employee ID
Product Name
```

**Interview Answer:**

> BM25 is a keyword-based retrieval algorithm. It is useful when exact words, IDs, codes, or technical terms are important.

**Remember:**

> Sparse/BM25 = Keywords

---

# 11. Semantic Search

Semantic search means searching based on **meaning instead of exact keyword matching**.

Usually:

```text
Embeddings
+
Vector DB
+
Similarity Search
```

Example:

```text
Document:
"Employees receive 20 annual paid leaves."

Query:
"How many vacation days do I get?"
```

Semantic search understands:

```text
vacation days ≈ annual paid leaves
```

**Interview Answer:**

> Semantic search retrieves documents based on meaning using embeddings rather than depending only on exact keyword matches.

---

# 12. Hybrid Search

Hybrid Search combines:

```text
Dense Retrieval + BM25
```

Meaning:

```text
Semantic Search + Keyword Search
```

Example query:

```text
Why did MT548 settlement fail?
```

Dense retrieval understands:

```text
settlement failure
```

BM25 strongly matches:

```text
MT548
```

So hybrid search gives us benefits of both.

```text
             Query
            /     \
           ↓       ↓
       Dense      BM25
           \       /
            ↓     ↓
         Combine Results
               ↓
           Reranking
               ↓
              LLM
```

**Interview Answer:**

> Hybrid search combines dense embedding-based retrieval with sparse keyword retrieval like BM25. Dense search understands meaning, while BM25 handles exact keywords and technical terms.

---

# 13. Cosine Similarity

Cosine similarity measures how similar two vectors are based on their direction.

In RAG:

```text
Query Embedding
      ↓
Compare With
      ↓
Document Embeddings
```

Example:

```text
Chunk A → 0.94
Chunk B → 0.81
Chunk C → 0.30
```

Chunk A is more similar to the query.

**Interview Answer:**

> Cosine similarity is used to measure similarity between the query embedding and document embeddings so we can retrieve semantically relevant chunks.

You usually don't need to memorize the formula for an interview.

---

# 14. What is Top-K?

Top-K means the **number of highest-ranked chunks retrieved**.

Example:

```text
Top-K = 3
```

means retrieve the 3 most relevant chunks.

### K too small

May miss important information.

### K too large

May:

* Add irrelevant information
* Increase tokens
* Increase cost
* Confuse the LLM

**Interview Answer:**

> Top-K controls how many relevant chunks we retrieve. A very small K may miss context, while a very large K can introduce noise, so I tune it based on retrieval performance.

---

# 15. What is Reranking?

Reranking means taking initially retrieved results and ranking them again using a more accurate relevance model.

Example:

```text
Retrieve Top 20
      ↓
Reranker
      ↓
Best 5
      ↓
LLM
```

Why?

Vector search is fast, but the initial ranking may not always be perfect.

**Interview Answer:**

> Reranking is a second retrieval stage. I first retrieve a larger number of candidate chunks and then use a reranker to reorder them based on relevance before sending the best chunks to the LLM.

---

# 16. What is Hallucination?

Hallucination is when an LLM generates information that sounds correct but is **incorrect or unsupported**.

Example:

Document:

```text
Employees receive 20 leaves.
```

LLM:

```text
Employees receive 30 leaves.
```

That is hallucination.

### Does RAG completely remove hallucination?

**No.**

RAG reduces hallucination but cannot completely eliminate it.

Two problems can happen:

```text
Wrong Retrieval
     ↓
Wrong Context
     ↓
Wrong Answer
```

or:

```text
Correct Context
     ↓
LLM ignores/misunderstands it
     ↓
Wrong Answer
```

### How to reduce it?

* Better retrieval
* Better chunking
* Hybrid search
* Reranking
* Correct Top-K
* Strong grounding prompt
* Citations
* Allow "I don't know"

**Interview Answer:**

> Hallucination is when the LLM generates incorrect or unsupported information. RAG reduces it by grounding the LLM with retrieved documents, but we still need good retrieval, reranking and grounding prompts.

---

# 17. RAG vs Fine-Tuning

### RAG

Provides external information at runtime.

```text
Documents → Retrieve → Context → LLM
```

The model weights are **not changed**.

Best for:

* Private knowledge
* Frequently changing data
* Company documents
* Latest information
* Citations

### Fine-Tuning

Trains the model further on examples and **changes its weights**.

Best for:

* Specific behavior
* Specific style
* Output format
* Specialized repeated tasks

### Easy Difference

> **RAG changes/provides the context.**

> **Fine-tuning changes the model weights.**

Example:

Latest HR policies → **RAG**

Make the model always respond in a specific company style → **Fine-tuning**

They can also be used together.

---

# 18. How Would You Improve RAG?

This is an important interview question.

First identify:

```text
Is it a Retrieval Problem?
        OR
Is it a Generation Problem?
```

Then improve:

### Retrieval

* Clean documents
* Remove duplicates
* Improve chunk size
* Tune overlap
* Better embedding model
* Tune Top-K
* Metadata filtering
* Hybrid search
* Reranking
* Query rewriting

### Generation

* Better prompts
* Strong grounding instructions
* Tell LLM not to invent answers
* Allow "I don't know"
* Add citations

### Evaluation

Test separately:

```text
Did I retrieve the correct chunk?
```

and

```text
Did the LLM answer correctly using that chunk?
```

**Interview Answer:**

> To improve RAG, I first check whether the problem is retrieval or generation. For retrieval, I optimize chunking, embeddings, Top-K, metadata filtering, hybrid search and reranking. For generation, I improve grounding prompts and citations. Finally, I evaluate retrieval and generation separately.

---

# 19. Complete Improved RAG Flow

```text
Documents
   ↓
Clean
   ↓
Chunk
   ↓
Embeddings
   ↓
Vector DB + Metadata
   ↓

User Query
   ↓
Query Rewriting
   ↓
 ┌───────────────┐
 ↓               ↓
Dense           BM25
Search          Search
 ↓               ↓
 └───────┬───────┘
         ↓
   Hybrid Results
         ↓
      Reranker
         ↓
    Best Top-K
         ↓
Question + Context
         ↓
        LLM
         ↓
Answer + Citation
```

---

# 20. Rapid-Fire Interview Revision

### What is RAG?

> Retrieval + LLM generation. It retrieves relevant external information and provides it as context to the LLM.

### Why RAG?

> For private, updated and domain-specific knowledge and to reduce hallucination without retraining the LLM.

### What are embeddings?

> Numerical vectors representing the semantic meaning of text.

### What is a Vector DB?

> A database optimized for storing embeddings and performing similarity search.

### Why chunk documents?

> To improve retrieval accuracy, create focused embeddings and avoid sending complete documents to the LLM.

### What is chunk overlap?

> Repeating some text between consecutive chunks so context isn't lost at boundaries.

### Fixed vs Recursive vs Semantic chunking?

> Fixed splits by size, recursive uses natural separators, and semantic splits based on topic or meaning.

### Dense retrieval?

> Embedding-based semantic retrieval.

### Sparse/BM25?

> Keyword-based retrieval.

### Semantic search?

> Searching by meaning instead of only exact keywords.

### Hybrid search?

> Dense retrieval + BM25.

### Cosine similarity?

> Measures similarity between query and document vectors.

### Top-K?

> Number of highest-ranked chunks retrieved.

### Reranking?

> Reordering retrieved chunks using a more accurate relevance model.

### Hallucination?

> When the LLM generates incorrect or unsupported information.

### Does RAG eliminate hallucination?

> No. It reduces it but does not completely eliminate it.

### RAG vs Fine-Tuning?

> RAG provides external context; fine-tuning changes model weights.

### How do you improve RAG?

> Better data → better chunking → embeddings → hybrid search → Top-K → reranking → metadata filtering → grounding prompt → evaluation.

---

# 30-Second RAG Answer

> RAG stands for Retrieval-Augmented Generation. First, I load documents, divide them into chunks, create embeddings and store them in a vector database. When a user asks a question, I create the query embedding and retrieve the Top-K relevant chunks using similarity search. I can also use hybrid search with BM25 and reranking to improve retrieval. Finally, I provide the retrieved context with the question to the LLM. This allows the LLM to answer using private or updated information and helps reduce hallucination.

---

# Final Memory Line

```text
Documents
→ Chunking
→ Embeddings
→ Vector DB
→ Query
→ Retrieval
→ Top-K
→ Reranking
→ Context
→ LLM
→ Answer
```

**Dense = Meaning**

**Sparse/BM25 = Keywords**

**Hybrid = Dense + BM25**

**Top-K = How many chunks**

**Reranking = Reorder retrieved chunks**

**RAG = External knowledge/context**

**Fine-Tuning = Change model weights**
