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

