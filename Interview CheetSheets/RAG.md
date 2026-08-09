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

