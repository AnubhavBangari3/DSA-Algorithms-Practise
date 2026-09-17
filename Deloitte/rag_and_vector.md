# RAG + Vector Database

---

# 1. RAG (Retrieval-Augmented Generation)

## What is it?

**RAG stands for Retrieval-Augmented Generation.**

RAG is an architecture where we first retrieve relevant information from an external knowledge source and then provide that information to an LLM as context before asking it to generate an answer.

Instead of depending only on the LLM's trained knowledge:

```text
Question
   ↓
LLM
   ↓
Answer
```

RAG works like:

```text
Question
   ↓
Retrieve Relevant Information
   ↓
Add Retrieved Context to Prompt
   ↓
LLM
   ↓
Grounded Answer
```

The two main stages are:

1. **Retrieval** — Find relevant information.
2. **Generation** — LLM generates an answer using that information.

## Why / When is it used?

RAG is useful when the LLM needs access to:

- Private company documents
- Internal knowledge bases
- Frequently updated information
- Domain-specific documents
- Large collections of PDFs or text

It also helps reduce hallucination because the LLM receives relevant source information.

## Use Case

Suppose a company has internal settlement procedure documents.

A user asks:

```text
What should we do when a trade fails because of incorrect SSI?
```

Instead of relying only on the LLM:

```text
Question
   ↓
Search Settlement Documents
   ↓
Retrieve SSI Procedure
   ↓
Provide Procedure + Question to LLM
   ↓
Generate Answer
```

## Example

```python
question = "How do we resolve an SSI settlement failure?"

documents = retriever.invoke(question)

context = "\n".join(
    doc.page_content for doc in documents
)

prompt = f"""
Answer the question using the provided context.

Context:
{context}

Question:
{question}
"""

response = llm.invoke(prompt)
```

## Interview Answer

"RAG stands for Retrieval-Augmented Generation. Instead of asking an LLM to answer only from its trained knowledge, RAG first retrieves relevant information from an external knowledge source and provides that information to the LLM as context. For example, I can retrieve settlement procedures from an internal knowledge base and use them to generate a more grounded answer."

## Key Points to Remember

- RAG = Retrieval + Generation.
- Gives LLM access to external knowledge.
- Useful for private and frequently changing information.
- Helps reduce unsupported or hallucinated answers.

---

# 2. RAG Architecture End-to-End

## What is it?

A typical RAG architecture has two major pipelines:

### Indexing Pipeline

Documents are prepared and stored.

```text
Documents
   ↓
Load Documents
   ↓
Clean / Process
   ↓
Chunk Documents
   ↓
Generate Embeddings
   ↓
Store in Vector DB
```

### Query Pipeline

The stored knowledge is retrieved when a user asks a question.

```text
User Question
      ↓
Generate Query Embedding
      ↓
Similarity Search
      ↓
Retrieve Top-K Chunks
      ↓
Optional Metadata Filtering
      ↓
Optional Reranking
      ↓
Build Prompt
      ↓
LLM
      ↓
Final Answer
```

## Why / When is it used?

Understanding the complete architecture is important because RAG quality depends on much more than just the LLM.

Poor:

- Chunking
- Embeddings
- Retrieval
- Ranking

can all produce poor answers even if the LLM itself is good.

## Use Case

Settlement knowledge base:

```text
SWIFT Documents
Settlement Procedures
SSI Guidelines
Operations Manuals
        ↓
      Chunk
        ↓
    Embeddings
        ↓
    Vector DB
```

Then:

```text
"Why did this SSI fail?"
        ↓
Query Embedding
        ↓
Vector Search
        ↓
Relevant SSI Documents
        ↓
LLM
        ↓
Answer
```

## Example

```python
# Indexing

documents = load_documents()

chunks = text_splitter.split_documents(documents)

vector_store.add_documents(chunks)


# Retrieval

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)

docs = retriever.invoke(
    "How do we resolve an SSI mismatch?"
)
```

## Interview Answer

"RAG has two main phases: indexing and retrieval. During indexing, documents are loaded, cleaned, divided into chunks, converted into embeddings, and stored in a vector database. During query time, the user's question is converted into an embedding, relevant chunks are retrieved using similarity search, optionally filtered or reranked, and then provided to the LLM as context for generating the final answer."

## Key Points to Remember

- Indexing happens before querying.
- Documents are chunked and embedded.
- Retrieval finds relevant chunks.
- Retrieved context is passed to the LLM.

---

# 3. Embeddings

## What is it?

An **embedding** is a numerical vector representation of data such as text.

It converts text into numbers that capture semantic meaning.

For example:

```text
"Trade failed because cash was insufficient"

        ↓ Embedding Model

[0.12, -0.45, 0.78, 0.21, ...]
```

Texts with similar meanings should generally have embeddings that are closer in vector space.

Example:

```text
"Insufficient cash caused settlement failure"

"Trade failed because there was not enough cash"
```

These sentences use different words but have similar meanings, so their vectors should be relatively close.

## Why / When is it used?

Traditional keyword search mainly compares words.

Embeddings allow us to perform **semantic search**, where meaning matters more than exact keyword matches.

## Use Case

User asks:

```text
Why did settlement fail because there wasn't enough money?
```

The document may say:

```text
Settlement failure caused by insufficient cash balance.
```

Even though the wording differs, embedding similarity can retrieve the relevant document.

## Example

Conceptually:

```python
embedding = embedding_model.embed_query(
    "Settlement failed because of insufficient cash"
)

print(embedding)

# [0.12, -0.45, 0.78, ...]
```

## Interview Answer

"Embeddings are numerical vector representations of text that capture semantic meaning. In RAG, I generate embeddings for document chunks and store them in a vector database. When a user asks a question, I generate an embedding for the query and compare it with stored vectors to find semantically similar content."

## Key Points to Remember

- Embeddings represent meaning numerically.
- Similar meaning → vectors closer together.
- Used for semantic search.
- Both documents and queries are embedded.

---

# 4. Vector Database

## What is it?

A **vector database** is a database designed to store embeddings and efficiently search for similar vectors.

Typical stored information:

```text
Vector
Document Text
Metadata
Document ID
```

Example:

```json
{
    "vector": [0.12, 0.44, -0.18],
    "text": "SSI mismatch can cause settlement failure.",
    "metadata": {
        "category": "SSI",
        "document": "settlement_manual.pdf"
    }
}
```

Popular vector stores/databases include:

- Pinecone
- Weaviate
- Milvus
- Qdrant
- Chroma
- FAISS for local vector search
- PostgreSQL with pgvector

## Why / When is it used?

Normal databases are optimized for exact values and structured queries.

Vector databases are optimized for finding semantically similar vectors efficiently.

## Use Case

Store thousands of settlement procedure chunks as embeddings.

When the user asks:

```text
How should an SSI mismatch be resolved?
```

the vector DB retrieves chunks semantically related to SSI mismatch.

## Example

```python
vector_store.add_documents(chunks)

results = vector_store.similarity_search(
    "How do I resolve an SSI mismatch?",
    k=5
)
```

## Interview Answer

"A vector database stores embeddings and supports efficient similarity search. In a RAG application, document chunks are converted into embeddings and stored along with their text and metadata. At query time, the query embedding is compared against stored vectors to retrieve semantically relevant chunks."

## Key Points to Remember

- Stores embeddings.
- Optimized for similarity search.
- Usually stores metadata with vectors.
- Core retrieval component in many RAG systems.

---

# 5. Similarity Search

## What is it?

**Similarity search** finds vectors that are closest to the query vector.

Basic flow:

```text
Question
   ↓
Query Embedding
   ↓
Compare with Stored Embeddings
   ↓
Find Most Similar Vectors
   ↓
Return Relevant Chunks
```

Common similarity/distance methods include:

- Cosine similarity
- Dot product
- Euclidean distance

Cosine similarity is commonly used for text embeddings.

## Why / When is it used?

Similarity search allows semantic retrieval.

The query and document do not need to contain exactly the same words.

## Use Case

Query:

```text
Trade doesn't have enough money for settlement.
```

Stored document:

```text
Insufficient cash balance may result in settlement failure.
```

Semantic similarity can identify that these statements are related.

## Example

Conceptually:

```python
results = vector_store.similarity_search(
    "Trade failed because cash was unavailable",
    k=3
)

for result in results:
    print(result.page_content)
```

## Interview Answer

"Similarity search compares the embedding of a user query with stored document embeddings and retrieves the closest vectors. This enables semantic search, so documents can be retrieved based on meaning even when they don't contain exactly the same keywords as the query."

## Key Points to Remember

- Query is converted into an embedding.
- Query vector is compared with document vectors.
- Returns semantically similar chunks.
- Cosine similarity is commonly used.

---

# 6. Chunking

## What is it?

**Chunking** means dividing large documents into smaller pieces before creating embeddings.

Instead of embedding an entire 100-page document:

```text
100-page Document
```

we divide it:

```text
Chunk 1
Chunk 2
Chunk 3
...
Chunk N
```

Each chunk gets its own embedding.

## Why / When is it used?

Embedding an entire document can mix multiple unrelated topics into one vector.

Very small chunks may lose important context.

Chunking tries to balance:

```text
Enough Context
+
Precise Retrieval
```

## Use Case

Settlement manual:

```text
Page 1-5   → Introduction
Page 6-10  → Cash Failures
Page 11-15 → SSI Failures
Page 16-20 → Security Failures
```

Instead of retrieving the whole manual, RAG can retrieve only the relevant chunks.

## Example

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)
```

Chunk size should be tuned based on the document type, embedding model, and use case rather than using one universal value.

## Interview Answer

"Chunking means splitting large documents into smaller sections before generating embeddings. This improves retrieval because the system can return the specific section relevant to the user's question instead of an entire document. Chunk size is a tuning parameter: chunks that are too large reduce precision, while chunks that are too small can lose context."

## Key Points to Remember

- Split large documents before embedding.
- Too large → less precise retrieval.
- Too small → context can be lost.
- Chunk size should be tested for the use case.

---

# 7. Chunk Overlap

## What is it?

**Chunk overlap** means repeating some content between adjacent chunks.

Without overlap:

```text
Chunk 1: A B C D

Chunk 2: E F G H
```

With overlap:

```text
Chunk 1: A B C D

Chunk 2: C D E F

Chunk 3: E F G H
```

The repeated section preserves context across chunk boundaries.

## Why / When is it used?

Important information may occur at the boundary between two chunks.

Without overlap, related sentences could be separated.

Overlap helps preserve continuity.

## Use Case

Suppose:

```text
Chunk 1 ends:
"Settlement may fail if the account..."

Chunk 2 starts:
"...does not contain sufficient cash."
```

Bad splitting could separate the meaning.

Overlap helps keep related information together.

## Example

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)
```

Here:

```text
Chunk Size = 800
Overlap = 100
```

## Interview Answer

"Chunk overlap repeats a small amount of content between neighboring chunks. It helps preserve context when important information crosses a chunk boundary. However, too much overlap increases storage and can produce duplicate retrieval results, so it needs to be tuned."

## Key Points to Remember

- Preserves context across boundaries.
- Helps avoid information loss.
- Too much overlap creates duplication.
- Tune chunk size and overlap together.

---

# 8. Top-K Retrieval

## What is it?

**Top-K** specifies how many of the highest-ranked retrieved chunks should be returned.

For example:

```text
k = 3
```

means:

```text
Query
 ↓
Similarity Search
 ↓
Return 3 most relevant chunks
```

## Why / When is it used?

The LLM should receive enough information to answer the question, but not excessive irrelevant context.

Too small `k`:

```text
May miss important information.
```

Too large `k`:

```text
May introduce irrelevant context,
increase tokens,
increase cost,
and confuse the LLM.
```

## Use Case

Suppose there are 1,000 settlement document chunks.

Instead of sending all 1,000 chunks to the LLM:

```text
Retrieve Top 5
      ↓
Provide those 5 to LLM
```

## Example

```python
retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 5
    }
)

docs = retriever.invoke(
    "How do I resolve an SSI failure?"
)
```

## Interview Answer

"Top-K determines how many retrieved chunks are returned from the vector search. If K is too low, important information may be missed. If K is too high, irrelevant context may be added and token usage increases. I would tune K using retrieval evaluation rather than selecting it arbitrarily."

## Key Points to Remember

- K = number of retrieved results.
- Small K may miss context.
- Large K may introduce noise.
- Tune K using evaluation data.

---

# 9. Metadata Filtering

## What is it?

**Metadata filtering** restricts retrieval using structured information associated with documents.

Example metadata:

```json
{
    "department": "settlement",
    "failure_type": "SSI",
    "region": "US",
    "year": 2026
}
```

Instead of searching every document, we can filter first.

```text
Search only:

failure_type = SSI
region = US
```

Then perform semantic search within that subset.

## Why / When is it used?

Semantic similarity alone may return related but inappropriate documents.

Metadata filtering improves retrieval precision.

## Use Case

Question:

```text
What is the current US procedure for SSI failures?
```

Filter:

```text
region = US
category = SSI
status = ACTIVE
```

Then run vector search.

## Example

Conceptually:

```python
results = vector_store.similarity_search(
    "How should an SSI failure be handled?",
    k=5,
    filter={
        "region": "US",
        "category": "SSI"
    }
)
```

Exact filtering syntax depends on the vector database.

## Interview Answer

"Metadata filtering combines structured filtering with semantic retrieval. For example, if the user asks about US SSI settlement procedures, I can first restrict the search to documents where region is US and category is SSI, and then perform similarity search. This reduces irrelevant retrieval."

## Key Points to Remember

- Metadata = structured document attributes.
- Filtering improves retrieval precision.
- Combine filtering with semantic search.
- Useful for region, date, department, document type, or access control.

---

# 10. Reranking

## What is it?

**Reranking** is a second-stage ranking process applied after initial retrieval.

Instead of directly sending vector search results to the LLM:

```text
Query
 ↓
Retrieve Top 20
 ↓
Reranker
 ↓
Best 5
 ↓
LLM
```

The first retrieval stage focuses on quickly finding likely candidates.

The reranker then performs a more detailed relevance comparison.

## Why / When is it used?

Vector similarity does not always produce the best relevance order.

Reranking can improve the quality of the final context.

## Use Case

Initial retrieval:

```text
20 settlement chunks
```

Reranker evaluates them against:

```text
"How do I resolve an SSI mismatch?"
```

and returns:

```text
5 most relevant chunks
```

These are passed to the LLM.

## Example

Conceptually:

```python
candidates = retriever.invoke(query)

reranked = reranker.rank(
    query=query,
    documents=candidates
)

best_docs = reranked[:5]
```

## Interview Answer

"Reranking is a second retrieval stage where I first retrieve a broader set of candidate documents using vector search and then use a stronger relevance model to reorder them. For example, I might retrieve 20 candidates and rerank them to select the best 5 before sending context to the LLM."

## Key Points to Remember

- Retrieval finds candidates.
- Reranking improves ordering.
- Can improve precision.
- Adds some latency and cost.

---

# 11. RAG vs Fine-Tuning

## What is it?

RAG and fine-tuning solve different problems.

### RAG

Provides external knowledge to the model at runtime.

```text
Question
   ↓
Retrieve Knowledge
   ↓
LLM
```

### Fine-Tuning

Adjusts model parameters using training examples.

```text
Training Examples
      ↓
Fine-Tuning
      ↓
Customized Model Behavior
```

A useful distinction:

```text
RAG → Give the model relevant knowledge/context.

Fine-Tuning → Change how the model behaves or responds.
```

## Why / When is it used?

Use **RAG** when:

- Knowledge changes frequently.
- You have private documents.
- Answers should be grounded in source documents.
- Documents need to be updated easily.

Use **fine-tuning** when:

- You want consistent style or behavior.
- You want specialized response patterns.
- You have high-quality training examples.

They can also be combined.

## Use Case

Settlement procedures change regularly.

Using fine-tuning for every procedure update would be inefficient.

Instead:

```text
Updated Settlement Document
       ↓
Re-index Document
       ↓
Immediately Available to RAG
```

Fine-tuning might instead be useful for teaching a model a consistent classification format or domain-specific response behavior.

## Example

```text
Need latest internal procedures?

→ RAG

Need consistent specialized model behavior?

→ Fine-Tuning

Need both?

→ Fine-Tuned Model + RAG
```

## Interview Answer

"RAG and fine-tuning solve different problems. RAG provides external knowledge to the model at runtime, while fine-tuning modifies the model's behavior using training examples. For frequently changing internal knowledge such as settlement procedures, I would prefer RAG because documents can be updated without retraining the model. Fine-tuning is more appropriate when I need consistent specialized behavior or output patterns."

## Key Points to Remember

- RAG changes the context.
- Fine-tuning changes model behavior.
- RAG is good for changing/private knowledge.
- They can be used together.

---

# 12. Reducing Bad Retrieval

## What is it?

**Bad retrieval** happens when the RAG system retrieves irrelevant, incomplete, outdated, or misleading chunks.

Example:

```text
Question:
How do I resolve an SSI mismatch?

Bad Retrieval:
Cash management procedure
Security lending document
Old SSI document
```

If retrieval is poor, the LLM receives bad context and may generate a poor answer.

This is often summarized as:

```text
Bad Retrieval
      ↓
Bad Context
      ↓
Bad Answer
```

## Why / When is it used?

Improving retrieval is one of the most important parts of improving a RAG system.

Common techniques include:

1. Better chunking
2. Appropriate chunk overlap
3. Better embedding models
4. Metadata filtering
5. Top-K tuning
6. Reranking
7. Query rewriting
8. Hybrid search
9. Removing duplicate/outdated documents
10. Evaluating retrieval quality

## Use Case

Suppose the query is:

```text
Current US procedure for SSI mismatch
```

Instead of searching everything:

```text
Query
  ↓
Query Rewrite
  ↓
Metadata Filter:
Region = US
Category = SSI
Status = ACTIVE
  ↓
Hybrid / Vector Search
  ↓
Retrieve Candidates
  ↓
Rerank
  ↓
Best Context
  ↓
LLM
```

## Example

```python
retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 10,
        "filter": {
            "category": "SSI",
            "status": "ACTIVE"
        }
    }
)

candidates = retriever.invoke(query)

best_docs = reranker.rank(
    query,
    candidates
)[:5]
```

Another useful approach is **hybrid search**:

```text
Keyword Search
      +
Vector Search
      ↓
Combined Results
      ↓
Reranking
```

Keyword search helps with exact identifiers and terminology, while vector search helps with semantic meaning.

## Interview Answer

"If RAG is giving poor answers, I would first check retrieval quality rather than immediately changing the LLM. I would evaluate whether the correct chunks are being retrieved and then tune chunking, overlap, embeddings, Top-K, and metadata filters. For more difficult cases I can use query rewriting, hybrid search, and reranking. I would also remove duplicate or outdated documents and measure retrieval using a test dataset."

## Key Points to Remember

- Always inspect retrieval before blaming the LLM.
- Improve chunking, embeddings, filtering, and Top-K.
- Use reranking or hybrid search when necessary.
- Maintain clean and current source documents.

---

# 13. Hybrid Search

## What is it?

**Hybrid search** combines keyword-based search with semantic vector search.

```text
               Query
                 |
        +--------+--------+
        |                 |
        v                 v
 Keyword Search      Vector Search
        |                 |
        +--------+--------+
                 |
           Merge / Rank
                 |
                 v
             Results
```

Keyword search is strong when exact terms matter.

Vector search is strong when semantic meaning matters.

## Why / When is it used?

Vector search may struggle with exact values such as:

```text
MT548
TRD-10234
ISIN
Account Number
Error Code E102
```

Keyword search can handle these exact terms well.

Semantic search handles natural-language meaning.

Combining both can improve retrieval.

## Use Case

User asks:

```text
What does MT548 status code PENF mean in our settlement procedure?
```

Keyword search helps locate:

```text
MT548
PENF
```

while semantic search finds relevant explanatory sections.

## Example

Conceptually:

```python
keyword_results = keyword_search(query)

vector_results = vector_search(query)

combined_results = merge_results(
    keyword_results,
    vector_results
)

final_results = rerank(combined_results)
```

## Interview Answer

"Hybrid search combines keyword search with semantic vector search. Vector search is strong at understanding meaning, while keyword search is useful for exact identifiers, codes, and domain terminology. In capital markets, for example, terms like MT548, ISIN, or specific error codes can benefit from keyword matching while vector search retrieves semantically related explanations."

## Key Points to Remember

- Combines keyword and vector search.
- Useful for exact domain terminology.
- Improves both semantic and lexical retrieval.
- Results can be reranked afterward.

---

# Quick Interview Revision

| Concept | Remember This |
|---|---|
| RAG | Retrieve knowledge → Give context to LLM → Generate answer |
| Indexing | Documents → Chunk → Embed → Store |
| Embeddings | Numerical representation of semantic meaning |
| Vector DB | Stores and searches embeddings |
| Similarity Search | Finds semantically similar vectors |
| Chunking | Break documents into smaller sections |
| Chunk Overlap | Preserve context between chunks |
| Top-K | Number of retrieved chunks |
| Metadata Filtering | Restrict retrieval using structured attributes |
| Reranking | Reorder retrieved candidates by relevance |
| Hybrid Search | Keyword Search + Vector Search |
| RAG vs Fine-Tuning | External knowledge vs model behavior |
| Bad Retrieval | Improve retrieval before blaming the LLM |

---

# Complete RAG Architecture

```text
                     OFFLINE / INDEXING

                     Documents
                         |
                         v
                  Document Loader
                         |
                         v
                  Clean / Process
                         |
                         v
                      Chunking
                         |
                         v
                  Embedding Model
                         |
                         v
                    Vector DB
                 + Metadata Store


                     ONLINE / QUERY

                       User
                         |
                         v
                       Query
                         |
                         v
                  Query Embedding
                         |
                         v
              +-----------------------+
              |                       |
              v                       v
         Vector Search          Metadata Filter
              |                       |
              +-----------+-----------+
                          |
                          v
                    Top-K Candidates
                          |
                          v
                       Reranker
                          |
                          v
                  Best Relevant Chunks
                          |
                          v
                     Prompt Builder
                          |
             Question + Retrieved Context
                          |
                          v
                         LLM
                          |
                          v
                    Final Answer
```

---

# 60-Second Combined Interview Answer

"RAG stands for Retrieval-Augmented Generation. It allows an LLM to answer using external knowledge instead of relying only on its trained parameters.

During indexing, I load documents, clean them, divide them into chunks with appropriate overlap, generate embeddings, and store those embeddings along with metadata in a vector database.

At query time, I generate an embedding for the user's question and perform similarity search to retrieve the Top-K relevant chunks. I can apply metadata filtering to restrict the search and reranking to improve the final relevance order. The best chunks are then added to the prompt and provided to the LLM.

If retrieval quality is poor, I would first evaluate chunking, embeddings, Top-K, metadata filters, duplicate or outdated documents, and then consider techniques like query rewriting, hybrid search, and reranking.

For frequently changing internal knowledge, I would generally use RAG rather than fine-tuning because the knowledge can be updated by re-indexing documents without retraining the model."