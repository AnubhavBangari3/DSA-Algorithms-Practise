# RAG Architecture

## What is RAG?

**RAG (Retrieval-Augmented Generation)** is an architecture where an LLM first retrieves relevant information from an external knowledge source and then uses that information to generate the final answer.

In simple terms:

> **RAG = Retrieval + LLM Generation**

Instead of depending only on what the LLM learned during training, we provide it with relevant information from our own documents or database.

---

## RAG Architecture

RAG usually has **two main flows**:

1. **Indexing / Ingestion Pipeline** – prepares and stores documents.
2. **Retrieval / Generation Pipeline** – retrieves relevant information and generates an answer.

### Overall Architecture

User Documents
      ↓
Document Loader
      ↓
Text Cleaning
      ↓
Chunking
      ↓
Embedding Model
      ↓
Vector Database
      ↓
      ↓
User Question
      ↓
Embedding Model
      ↓
Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
Prompt = Question + Retrieved Context
      ↓
LLM
      ↓
Final Answer

---

# 1. Indexing / Ingestion Pipeline

This happens before users start asking questions.

## Step 1: Load Documents

First, we collect data from sources such as:

- PDF
- DOCX
- Websites
- Database
- CSV
- APIs
- Internal company documents

Example:

A company may upload its HR policy documents.

---

## Step 2: Clean the Text

We remove unnecessary information such as:

- Extra spaces
- HTML tags
- Broken characters
- Unnecessary headers/footers

This improves the quality of retrieval.

---

## Step 3: Chunking

Large documents cannot be efficiently searched as one big piece.

Therefore, we divide them into smaller pieces called **chunks**.

Example:

Document = 10,000 words

We might divide it into:

Chunk 1 → 500 tokens  
Chunk 2 → 500 tokens  
Chunk 3 → 500 tokens  
...

Usually, we also keep some **overlap** between chunks so that context is not lost.

Example:

Chunk size = 500 tokens  
Overlap = 50 tokens

---

## Step 4: Create Embeddings

Each chunk is converted into a numerical vector using an **embedding model**.

Example:

"Employees get 20 annual leaves"

might become conceptually:

[0.21, -0.42, 0.73, 0.11, ...]

The vector represents the **semantic meaning** of the text.

Embedding models can include:

- OpenAI Embeddings
- Sentence Transformers
- Hugging Face models
- Azure OpenAI Embeddings

---

## Step 5: Store in Vector Database

The embeddings are stored in a **Vector Database** along with the original text and metadata.

Examples:

- Qdrant
- Pinecone
- Chroma
- FAISS
- Weaviate
- Azure AI Search

Conceptually:

Chunk Text
+
Embedding
+
Metadata
      ↓
Vector Database

Metadata could contain:

document_name
page_number
category
created_date

---

# 2. Retrieval + Generation Pipeline

This happens when the user asks a question.

## Step 6: User Asks a Question

Example:

> "How many annual leaves do employees get?"

---

## Step 7: Convert Question into Embedding

The same or compatible embedding model converts the user's question into a vector.

User Question
      ↓
Embedding Model
      ↓
Query Vector

---

## Step 8: Similarity Search

The query vector is compared with vectors stored in the Vector Database.

Usually, similarity algorithms such as **Cosine Similarity** are used.

The system finds chunks whose meaning is closest to the user's question.

---

## Step 9: Retrieve Top-K Chunks

Instead of retrieving the entire database, we retrieve the most relevant chunks.

Example:

Top-K = 3

Result:

Chunk 1 → "Employees receive 20 annual leaves."

Chunk 2 → "Unused leaves can be carried forward."

Chunk 3 → "Leave approval requires manager approval."

---

## Step 10: Build the Prompt

The retrieved chunks are added to the LLM prompt as **context**.

Example:

Context:
Employees receive 20 annual leaves.
Unused leaves can be carried forward.

Question:
How many annual leaves do employees get?

Answer using only the provided context.

---

## Step 11: LLM Generates the Answer

The LLM receives:

**System Instructions + Retrieved Context + User Question**

and generates:

> "Employees receive 20 annual leaves."

The important point is that the LLM is now answering using **retrieved company data**, instead of relying only on its training knowledge.

---

# Complete RAG Flow

Documents
   ↓
Load
   ↓
Clean
   ↓
Chunk
   ↓
Create Embeddings
   ↓
Store in Vector DB

----------------------------

User Question
   ↓
Create Query Embedding
   ↓
Search Vector DB
   ↓
Retrieve Top-K Chunks
   ↓
Optional Reranking
   ↓
Add Chunks to Prompt
   ↓
LLM
   ↓
Final Answer

---

# Simple Example

Suppose we build a RAG chatbot for a company.

The company has an HR document containing:

> "Employees are entitled to 20 paid annual leaves."

We chunk the document, create embeddings, and store them in a Vector DB.

User asks:

> "How many paid leaves do I get?"

Even though the wording is different, semantic search can retrieve:

> "Employees are entitled to 20 paid annual leaves."

That chunk is passed to the LLM.

The LLM answers:

> "Employees are entitled to 20 paid annual leaves."

---

# Why Do We Use RAG?

RAG helps us:

- Use **private/company-specific data**
- Access information that was not part of LLM training
- Work with **updated information**
- Reduce hallucinations
- Provide more grounded answers
- Update knowledge without retraining the LLM
- Provide source/citation information

---

# Important Components of RAG

| Component | Purpose |
|---|---|
| Document Loader | Loads PDFs, documents, APIs, etc. |
| Chunking | Breaks large documents into smaller pieces |
| Embedding Model | Converts text into vectors |
| Vector Database | Stores and searches vectors |
| Retriever | Finds relevant chunks |
| Similarity Search | Measures relevance between query and chunks |
| Top-K | Number of chunks retrieved |
| Reranker | Reorders retrieved chunks based on relevance |
| Prompt | Combines retrieved context with user question |
| LLM | Generates the final answer |

---

# Interview Answer

**"RAG stands for Retrieval-Augmented Generation. It combines information retrieval with an LLM.**

**The architecture has two main parts: indexing and retrieval-generation.**

**During indexing, I load documents, clean them, divide them into chunks, generate embeddings for those chunks, and store the embeddings in a vector database such as Qdrant or Chroma.**

**When a user asks a question, I generate an embedding for the query and perform similarity search against the vector database. I retrieve the Top-K most relevant chunks and optionally rerank them.**

**Then I combine those retrieved chunks with the user's question and send them as context to the LLM. The LLM generates the final answer based on that retrieved information.**

**The main advantage is that we can provide private or updated knowledge to the LLM without retraining the model, while also reducing hallucination."**

---

# One-Line Interview Answer

> **RAG retrieves relevant information from an external knowledge base and provides it as context to an LLM so that the LLM can generate a more accurate and grounded answer.**

---

# Keywords to Remember

**Documents → Chunking → Embeddings → Vector DB → Query Embedding → Similarity Search → Top-K → Reranking → Context → LLM → Answer**

# Why Do We Use RAG?

## Simple Answer

We use **RAG (Retrieval-Augmented Generation)** because an LLM has some limitations:

- Its training knowledge may be outdated.
- It does not automatically know our private/company data.
- It can hallucinate and give incorrect answers.
- Retraining or fine-tuning the model whenever data changes is expensive.

RAG solves this by **retrieving relevant information from an external knowledge source and providing it to the LLM as context before generating the answer.**

---

## Example

Suppose a company has an internal HR policy:

> "Employees receive 20 paid leaves per year."

The LLM may not know this because this information is private.

With RAG:

User Question  
↓  
"How many paid leaves do employees get?"  
↓  
Search Company Knowledge Base  
↓  
Retrieve: "Employees receive 20 paid leaves per year."  
↓  
Send Question + Retrieved Context to LLM  
↓  
LLM Answer: "Employees receive 20 paid leaves per year."

So, instead of depending only on the LLM's internal knowledge, we **ground the answer using our own data**.

---

# Main Reasons for Using RAG

## 1. Use Private or Domain-Specific Data

LLMs don't automatically know an organization's internal information.

RAG allows us to connect the LLM with:

- Company documents
- Policies
- Product documentation
- Financial documents
- Knowledge bases
- PDFs
- Databases

---

## 2. Reduce Hallucination

An LLM can sometimes confidently generate incorrect information.

RAG provides relevant documents as context.

Instead of asking:

User Question → LLM → Answer

We do:

User Question
      ↓
Retrieve Relevant Information
      ↓
Question + Context
      ↓
LLM
      ↓
Grounded Answer

This **reduces hallucination**, although it does not completely eliminate it.

---

## 3. Use Updated Information

LLM knowledge is based on its training data and may not contain the latest information.

With RAG, we can update the external knowledge base without retraining the LLM.

Example:

New Company Policy
      ↓
Add Document
      ↓
Create Embeddings
      ↓
Update Vector DB
      ↓
RAG can retrieve the new information

---

## 4. No Need to Retrain the LLM

Without RAG, we might think about fine-tuning or retraining the model when knowledge changes.

That can be expensive and time-consuming.

With RAG:

> **Update the knowledge base instead of retraining the model.**

---

## 5. Better Domain-Specific Answers

RAG is useful when the LLM needs to answer questions from a specific domain.

Examples:

- Banking
- Capital Markets
- Healthcare
- Legal documents
- Company policies
- Technical documentation

The retrieved context helps the LLM generate answers based on the required domain.

---

## 6. Source / Citation Support

Because we know which documents were retrieved, we can also show the source of the answer.

Example:

Answer:
"The settlement cycle is T+1."

Source:
Settlement_Guidelines.pdf, Page 12

This improves **traceability and trust**.

---

# Why RAG Instead of Only an LLM?

### Without RAG

User Question
      ↓
LLM
      ↓
Answer based mainly on model knowledge

Problems:

- May be outdated
- Doesn't know private data
- Higher chance of hallucination

### With RAG

User Question
      ↓
Retrieve Relevant Documents
      ↓
Provide Context
      ↓
LLM
      ↓
Grounded Answer

Benefits:

- Private knowledge
- Updated knowledge
- Better factual grounding
- Source references
- No model retraining for every data update

---

# Interview Answer

**"We use RAG mainly because an LLM alone may not have access to private, domain-specific, or updated information and can also hallucinate.**

**In RAG, we retrieve relevant information from an external knowledge base and provide that information as context to the LLM before generating the answer.**

**This helps us generate more grounded and domain-specific responses, reduce hallucination, use frequently updated data without retraining the model, and also provide source citations.**

**For example, if I'm building an internal company chatbot, instead of expecting the LLM to know company policies, I can store those documents in a knowledge base and retrieve the relevant policy whenever a user asks a question."**

---

# One-Line Answer

> **RAG is used to give an LLM access to private, domain-specific, and up-to-date information so it can generate more accurate and grounded answers without retraining the model.**

---

# Keywords to Remember

**Private Data → Updated Data → Retrieval → Grounding → Reduce Hallucination → No Retraining → Citations**

# Embeddings in RAG

## What are Embeddings?

**Embeddings are numerical representations of text that capture its semantic meaning.**

In simple words:

> **Embedding converts text into a vector (list of numbers) so that a computer can compare the meaning of different texts.**

Example:

"How can I reset my password?"

↓ Embedding Model ↓

[0.21, -0.45, 0.78, 0.12, ...]

The actual embedding can contain hundreds or thousands of numbers.

---

# Why Do We Need Embeddings in RAG?

Computers cannot directly understand the semantic meaning of sentences.

For example:

> "How many paid leaves do employees get?"

and

> "What is the annual vacation allowance?"

These sentences use different words but have a **similar meaning**.

Embeddings place semantically similar text closer together in vector space.

This allows RAG to retrieve relevant information even when the user's exact words are not present in the document.

---

# Where Are Embeddings Used in RAG?

There are two important places.

## 1. Document Embeddings

First, documents are divided into chunks.

Each chunk is converted into an embedding.

Document
   ↓
Chunking
   ↓
Chunk 1 → Embedding → [0.2, 0.5, ...]
Chunk 2 → Embedding → [0.7, 0.1, ...]
Chunk 3 → Embedding → [0.3, 0.8, ...]
   ↓
Vector Database

The vector database stores:

- Original chunk
- Embedding/vector
- Metadata

---

## 2. Query Embedding

When the user asks a question, we convert the question into an embedding using the same or a compatible embedding model.

User Question
      ↓
Embedding Model
      ↓
Query Vector
      ↓
Compare with stored vectors
      ↓
Retrieve similar chunks

---

# Simple Example

Suppose our Vector DB contains:

Chunk 1:

> "Employees receive 20 annual paid leaves."

Chunk 2:

> "The company provides health insurance."

Chunk 3:

> "Employees receive laptops during onboarding."

User asks:

> "How many vacation days do I get?"

The words **vacation days** and **annual paid leaves** are different.

But their embeddings should be semantically similar.

Therefore:

User Query
      ↓
Query Embedding
      ↓
Similarity Search
      ↓
Chunk 1 has highest similarity
      ↓
Retrieve Chunk 1
      ↓
Send it to LLM

---

# How Are Embeddings Compared?

A common method is **Cosine Similarity**.

It measures how similar two vectors are based on their direction.

Conceptually:

Query Embedding
      ↓
Compare with
      ↓
Chunk Embeddings
      ↓
Similarity Scores

Example:

Chunk 1 → 0.92  
Chunk 2 → 0.41  
Chunk 3 → 0.25

Chunk 1 has the highest similarity, so it is retrieved.

---

# Embedding Model vs LLM

This is an important interview distinction.

### Embedding Model

Converts:

Text → Vector

Used mainly for:

- Semantic search
- Retrieval
- Similarity comparison

### LLM

Converts:

Prompt + Context → Natural Language Answer

Used mainly for:

- Understanding context
- Reasoning
- Generating responses

So in RAG:

Documents
   ↓
Embedding Model
   ↓
Vector DB

User Query
   ↓
Embedding Model
   ↓
Retrieval
   ↓
Relevant Context
   ↓
LLM
   ↓
Answer

---

# Example Embedding Models

Common embedding models include:

- OpenAI Embeddings
- Azure OpenAI Embeddings
- Hugging Face Sentence Transformers
- `all-MiniLM-L6-v2`
- Google embedding models

For example, `all-MiniLM-L6-v2` produces **384-dimensional embeddings**.

That means every text chunk is represented using a vector containing 384 numbers.

---

# Important Interview Point

We generally use the **same embedding model for documents and user queries**.

Why?

Because both vectors need to exist in the **same vector space** for meaningful similarity comparison.

If you change the embedding model, you will normally need to **re-embed your stored documents**.

---

# Embeddings vs Keywords

Traditional keyword search mainly looks for matching words.

Example:

Document:

> "Employees receive 20 annual leaves."

Query:

> "What is my vacation allowance?"

There may be no exact keyword match.

Embedding-based search understands that:

**vacation allowance ≈ annual leaves**

That is why embeddings are useful for **semantic search**.

---

# Interview Answer

**"Embeddings are numerical vector representations of text that capture semantic meaning.**

**In RAG, after splitting documents into chunks, I pass each chunk through an embedding model and store the generated vectors in a vector database.**

**When the user asks a question, I also convert the query into an embedding. Then I compare the query vector with the stored document vectors using similarity search, commonly cosine similarity, and retrieve the Top-K most relevant chunks.**

**The retrieved chunks are then provided as context to the LLM for generating the final answer.**

**The main advantage of embeddings is that they allow semantic search, so the query and document don't need to contain exactly the same words as long as their meanings are similar."**

---

# One-Line Answer

> **Embeddings convert text into numerical vectors that represent semantic meaning, allowing a RAG system to find relevant document chunks using vector similarity search.**

---

# Keywords to Remember

**Text → Embedding Model → Vector → Vector DB → Query Vector → Cosine Similarity → Top-K → Relevant Chunks → LLM**

# Vector Database in RAG

## What is a Vector Database?

A **Vector Database** is a database designed to store, index, and search **high-dimensional vectors (embeddings)** efficiently.

In RAG, document chunks are converted into embeddings and stored in a Vector DB.

Simple definition:

> **Vector DB stores embeddings and helps us quickly find the most semantically similar chunks for a user's query.**

---

# Why Do We Need a Vector DB?

Suppose we have **1 million document chunks**.

When a user asks a question, comparing the query embedding manually with all 1 million embeddings would be inefficient.

A Vector DB provides optimized indexing and similarity search to quickly find the most relevant vectors.

So:

User Question
      ↓
Query Embedding
      ↓
Vector Database
      ↓
Similarity Search
      ↓
Top-K Relevant Chunks
      ↓
LLM
      ↓
Answer

---

# What Do We Store in a Vector DB?

Usually, we store three things:

### 1. Embedding

Numerical representation of the chunk.

```text
[0.21, -0.45, 0.78, 0.12, ...]

# Chunking in RAG — Why, Size, and Overlap

## What is Chunking?

**Chunking means dividing a large document into smaller pieces of text before creating embeddings and storing them in the Vector DB.**

Example:

A PDF has 50 pages.

Instead of creating one embedding for the entire PDF:

Document
↓
Split into smaller chunks
↓
Create embedding for each chunk
↓
Store chunks in Vector DB

Example:

Chunk 1 → Introduction  
Chunk 2 → Leave Policy  
Chunk 3 → Work From Home Policy  
Chunk 4 → Insurance Policy

---

# Why Do We Need Chunking?

## 1. Better Retrieval Accuracy

Suppose a 50-page HR document contains information about:

- Salary
- Leave
- Insurance
- Work From Home
- Appraisal

If we create one embedding for the entire document, it represents too many topics.

Instead, if we create smaller chunks:

User asks:

> "How many annual leaves do employees get?"

The system can retrieve only the chunk containing the **leave policy**.

So:

Large Document → Less precise retrieval

Smaller Relevant Chunks → Better retrieval

---

## 2. LLM Context Window

LLMs have a limited context window.

We cannot keep sending complete documents to the LLM for every question.

Instead:

User Question
↓
Retrieve Top-K Relevant Chunks
↓
Send only those chunks to LLM

This saves tokens and reduces cost.

---

## 3. Better Embeddings

Embeddings work better when the text represents a relatively focused meaning.

For example:

### Large Chunk

Contains:

Leave Policy + Salary + Insurance + Appraisal + Remote Work

The embedding represents many concepts.

### Smaller Chunk

Contains:

> "Employees receive 20 annual paid leaves."

The embedding has a much more focused meaning.

This generally improves semantic retrieval.

---

# What is Chunk Size?

**Chunk size is the amount of text we put into one chunk.**

It is commonly measured using:

- Tokens
- Characters
- Words

For LLM applications, **tokens are usually the better measurement**.

Example:

```text
Chunk Size = 500 tokens

# Chunking Types: Fixed, Recursive, Semantic + Dense Retrieval

# 1. Fixed-Size Chunking

**Fixed-size chunking** divides text into chunks of approximately the same size, based on characters, words, or tokens.

Example:

```text
Document = 5000 tokens

Chunk Size = 500 tokens
Overlap = 50 tokens

Chunk 1 → Token 1–500
Chunk 2 → Token 451–950
Chunk 3 → Token 901–1400
...

# Sparse Retrieval / BM25 in RAG

> **Note:** It is **BM25**, not BM2.

# What is Sparse Retrieval?

**Sparse retrieval is a keyword-based retrieval technique that finds documents based mainly on the words present in the user query and documents.**

Unlike dense retrieval, it does **not depend on semantic embeddings** for matching.

Simple way to remember:

> **Dense Retrieval = Meaning / Embeddings**
>
> **Sparse Retrieval = Keywords / Terms**

---

# Simple Example

Suppose our documents contain:

```text
Document 1:
"SWIFT MT548 is used for settlement status."

Document 2:
"Employees receive 20 annual leaves."

Document 3:
"MT103 is used for customer credit transfer."

# Semantic Search in RAG

## What is Semantic Search?

**Semantic search retrieves information based on the meaning of the user's query rather than only matching exact keywords.**

In RAG, semantic search is commonly implemented using:

**Embeddings + Vector Database + Similarity Search**

Simple definition:

> **Semantic Search = Search by meaning, not just exact words.**

---

# Simple Example

Suppose the document contains:

> "Employees receive 20 annual paid leaves."

User asks:

> "How many vacation days do I get?"

There is no exact match between:

```text
vacation days

