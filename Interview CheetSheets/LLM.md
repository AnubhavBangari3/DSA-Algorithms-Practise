# LLM Basics — Interview Notes

## What is an LLM?

**LLM stands for Large Language Model.**

An LLM is an AI model trained on a very large amount of text data to understand and generate human-like language.

Examples:

- GPT
- Gemini
- Claude
- Llama
- Mistral

In simple terms:

> **An LLM takes text as input, understands the context, and predicts/generates the most appropriate sequence of tokens as output.**

---

# How Does an LLM Work?

At a high level:

User Prompt
    ↓
Tokenization
    ↓
Tokens
    ↓
Embeddings
    ↓
Transformer
    ↓
Attention
    ↓
Predict Next Token
    ↓
Repeat
    ↓
Final Response

Example:

Input:

"The capital of India is"

The model may predict:

"New"

Then:

"Delhi"

So the output becomes:

"The capital of India is New Delhi."

The important point is:

> **LLMs generate text token by token by predicting the next likely token based on the previous context.**

---

# 1. Tokens

LLMs don't directly process complete sentences as humans do.

Text is first divided into smaller units called **tokens**.

Example:

"Artificial Intelligence is powerful"

could conceptually become:

Artificial | Intelligence | is | powerful

But tokens are not always complete words.

A word may sometimes be divided into multiple tokens.

Example:

"unbelievable"

could be represented as smaller token pieces depending on the tokenizer.

So:

Text
 ↓
Tokenizer
 ↓
Tokens
 ↓
LLM

---

# 2. Tokenization

**Tokenization is the process of converting input text into tokens that the model can process.**

Example:

Input:

"I love Python programming"

Tokenization:

"I"  
"love"  
"Python"  
"programming"

The exact tokenization depends on the model.

Tokens matter because:

- Context windows are measured in tokens
- API usage/cost is often related to token usage
- More tokens require more computation

---

# 3. Embeddings

After tokenization, tokens are converted into numerical representations called **embeddings**.

Conceptually:

"Python"

↓

[0.23, -0.41, 0.78, ...]

These vectors allow the neural network to mathematically process language.

Important distinction:

In an LLM, token embeddings are part of how the model represents input internally.

In RAG, embedding models are also used to create vectors for **semantic retrieval**.

---

# 4. Transformer

Most modern LLMs are based on the **Transformer architecture**.

The Transformer is designed to understand relationships between tokens in a sequence.

One of its most important components is:

**Attention**

More specifically:

**Self-Attention**

---

# 5. What is Attention?

Attention allows the model to determine which parts of the input are important when processing a particular token.

Example:

"The developer couldn't deploy the application because it had a configuration error."

To understand what "it" refers to, the model needs to consider other words in the sentence.

Attention helps the model understand these relationships.

Simple idea:

> **Attention helps the model focus on relevant parts of the context.**

---

# 6. What is Self-Attention?

**Self-attention allows tokens in a sequence to consider other tokens in the same sequence when building their representations.**

Example:

"The bank rejected the transaction because the account had insufficient funds."

When understanding:

"rejected"

the model can consider:

"transaction"

"account"

"insufficient funds"

This helps the model understand context and relationships.

---

# 7. Next-Token Prediction

The basic generation process of many LLMs is:

> **Predict the next token based on previous tokens.**

Example:

Input:

"Python is a popular"

Possible predictions:

programming → high probability  
language → high probability  
banana → very low probability

The model chooses a token based on the generated probability distribution and decoding settings.

Then it repeats the process.

Example:

Python
↓
Python is
↓
Python is a
↓
Python is a popular
↓
Python is a popular programming
↓
Python is a popular programming language

---

# 8. Parameters

LLMs contain a large number of learned **parameters or weights**.

These parameters are learned during training.

They help the model capture patterns related to:

- Language
- Grammar
- Relationships
- Concepts
- Reasoning patterns
- Code
- General knowledge

When people say:

"7B model"

it generally means approximately:

7 billion parameters.

Similarly:

13B → approximately 13 billion parameters

The number of parameters alone does not determine model quality.

Training data, architecture, training process, inference techniques, and other factors also matter.

---

# 9. Training an LLM

At a simplified level, training works like this:

Large Text Dataset
      ↓
Tokenization
      ↓
Model receives tokens
      ↓
Predict next token
      ↓
Compare prediction with actual token
      ↓
Calculate loss
      ↓
Update model weights
      ↓
Repeat many times

Over time, the model learns patterns from the training data.

---

# 10. Pretraining

**Pretraining** is the initial large-scale training of an LLM on massive amounts of data.

It teaches the model general capabilities such as:

- Language understanding
- Grammar
- General knowledge
- Coding patterns
- Reasoning patterns

After pretraining, additional techniques can be used to make the model more useful for specific applications.

---

# 11. Fine-Tuning

**Fine-tuning means taking an already trained model and training it further on specialized examples.**

Example:

Base LLM
   ↓
Customer Support Dataset
   ↓
Fine-Tuning
   ↓
Customized Model

Fine-tuning can help adapt:

- Behavior
- Style
- Output format
- Specialized tasks

---

# 12. Inference

**Inference is when we actually use the trained model to generate a response.**

Training:

Model learns.

Inference:

Model answers.

Example:

User Prompt
    ↓
Trained LLM
    ↓
Generated Response

---

# 13. Prompt

A **prompt** is the input/instruction we provide to an LLM.

Example:

"Explain Django middleware in simple terms."

A better prompt might be:

"Explain Django middleware in simple terms with one practical example. Keep the answer under 150 words."

Better instructions generally give the model clearer guidance.

---

# 14. System Prompt vs User Prompt

### System Prompt

Defines the model's overall instructions or behavior.

Example:

"You are a Python interview assistant. Give concise answers with examples."

### User Prompt

The actual request from the user.

Example:

"Explain Python decorators."

Conceptually:

System Instructions
       +
User Prompt
       ↓
LLM
       ↓
Response

---

# 15. Context

**Context is the information available to the LLM while generating the current response.**

It can include:

- System instructions
- User question
- Conversation history
- Retrieved RAG documents
- Tool outputs
- Other supplied information

The LLM uses this information to generate its response.

---

# 16. Context Window

The **context window** is the maximum amount of tokenized information the model can process in a request/context.

Conceptually:

Context Window
      ↓
System Prompt
+
Conversation
+
RAG Context
+
User Question
+
Generated Output

The exact limits depend on the model.

This is important in RAG because we should not blindly send hundreds of retrieved chunks to the LLM.

Instead:

Retrieve relevant chunks
       ↓
Select useful context
       ↓
Send to LLM

---

# 17. Temperature

**Temperature controls the randomness of generated responses.**

### Lower Temperature

More predictable and focused.

Useful for:

- RAG Q&A
- Factual answers
- Code generation
- Structured extraction

Conceptually:

Temperature = 0.1

→ More deterministic/focused

### Higher Temperature

More varied and creative.

Useful for:

- Story generation
- Brainstorming
- Creative writing

Conceptually:

Temperature = 0.8

→ More variation/creativity

Important:

> **Temperature doesn't add knowledge to the model. It changes how the model samples from possible outputs.**

---

# 18. Top-P

**Top-P is another sampling parameter used to control output diversity.**

Instead of considering every possible next token, the model considers a set of tokens whose cumulative probability reaches the chosen Top-P value.

Example:

Top-P = 0.9

The model considers likely tokens covering approximately 90% of the probability mass.

For interviews, remember:

> **Temperature controls randomness, while Top-P controls the probability mass considered during token selection.**

---

# 19. Hallucination

**Hallucination is when an LLM generates information that sounds correct but is actually incorrect or unsupported.**

Example:

User asks about a company policy that the model doesn't know.

The model invents:

"Employees receive 30 annual leaves."

even though the actual policy says:

"20 annual leaves."

Ways to reduce hallucination include:

- RAG
- Grounding
- Better prompts
- Citations
- Tool usage
- Allowing the model to say "I don't know"

---

# 20. LLM vs RAG

An LLM generates answers mainly using:

- Learned model parameters
- Current prompt/context

RAG adds an external retrieval step.

Without RAG:

User
 ↓
LLM
 ↓
Answer

With RAG:

User
 ↓
Retrieve Relevant Documents
 ↓
Add Context
 ↓
LLM
 ↓
Grounded Answer

So:

> **LLM = Generation**

> **RAG = Retrieval + LLM Generation**

---

# Simple LLM Example

User asks:

"Explain Python decorators."

Flow:

User Prompt
    ↓
Tokenizer
    ↓
Tokens
    ↓
Embeddings
    ↓
Transformer
    ↓
Self-Attention
    ↓
Next-Token Prediction
    ↓
Generated Tokens
    ↓
Final Response

---

# Interview Answer — What is an LLM?

**"LLM stands for Large Language Model. It is a neural network, usually based on the Transformer architecture, trained on very large amounts of text data.**

**When we provide a prompt, the text is tokenized and converted into numerical representations. The Transformer processes these tokens using mechanisms such as self-attention to understand relationships within the context.**

**For text generation, the model predicts the next token based on the previous context and repeats this process until it generates the response.**

**LLMs can perform tasks such as question answering, summarization, code generation, extraction, translation, and content generation."**

---

# Interview Answer — How Does an LLM Generate Text?

**"An LLM generates text using next-token prediction. The input is first tokenized, and the Transformer processes those tokens using attention. The model calculates a probability distribution for the next possible token, selects a token according to its decoding strategy, adds it to the sequence, and repeats this process until the response is complete."**

---

# Quick Interview Revision

LLM
→ Large Language Model

Token
→ Small unit of text processed by model

Tokenization
→ Text to tokens

Embedding
→ Numerical representation

Transformer
→ Main architecture behind most modern LLMs

Self-Attention
→ Understand relationships between tokens

Parameters
→ Learned model weights

Pretraining
→ Large-scale initial training

Fine-Tuning
→ Additional training for specialized behavior/tasks

Inference
→ Using trained model to generate responses

Prompt
→ Instruction/input given to model

Context
→ Information available during generation

Context Window
→ Maximum tokenized context model can process

Temperature
→ Controls randomness

Top-P
→ Controls probability mass considered during sampling

Hallucination
→ Incorrect/unsupported generated information

RAG
→ Retrieves external knowledge before generation

---

# 20-Second Interview Answer

**"An LLM is a large neural network, usually based on the Transformer architecture, trained on massive amounts of text. It processes text as tokens, uses self-attention to understand relationships within the context, and generates responses by repeatedly predicting the next token. Parameters like temperature and Top-P control generation behavior, while the context window determines how much information the model can process at once."**

# Tokens in LLM

## What is a Token?

A **token is a small unit of text that an LLM processes.**

LLMs do not directly process text as complete sentences. Before the text is sent to the model, a **tokenizer converts the text into tokens**.

Simple definition:

> **Token = Small unit of text understood and processed by an LLM.**

---

# Simple Example

Input:

"Python is powerful"

Conceptually, it could be tokenized as:

Python | is | powerful

But a token is **not always one complete word**.

For example:

"unbelievable"

could potentially be split into:

un | believable

or other subword pieces depending on the tokenizer.

Therefore:

> **1 token ≠ always 1 word**

The exact tokenization depends on the model and its tokenizer.

---

# Tokenization Flow

User Text
    ↓
Tokenizer
    ↓
Tokens
    ↓
Token IDs
    ↓
LLM
    ↓
Generated Tokens
    ↓
Text Response

Example:

Input:

"I love Python"

Conceptually:

"I" → Token ID 101

"love" → Token ID 2456

"Python" → Token ID 8912

The actual IDs depend on the tokenizer.

---

# Why Do LLMs Use Tokens?

Neural networks work with numbers, not raw text.

Therefore, text needs to be converted into a numerical form.

The process is roughly:

Text
 ↓
Tokens
 ↓
Token IDs
 ↓
Token Embeddings
 ↓
Transformer
 ↓
Output

---

# Input Tokens and Output Tokens

There are mainly two types of tokens to understand from an API/application perspective.

## Input Tokens

Tokens sent **to the model**.

Example:

"Explain RAG architecture."

These tokens are part of the input.

Input can include:

- System prompt
- User prompt
- Conversation history
- RAG retrieved context
- Tool information

---

## Output Tokens

Tokens generated **by the model**.

Example:

"RAG stands for Retrieval-Augmented Generation..."

These are output tokens.

So:

Input Tokens
     ↓
LLM
     ↓
Output Tokens

---

# Why Are Tokens Important?

Tokens are important because they affect:

1. **Context Window**
2. **API Cost**
3. **Response Length**
4. **Performance**
5. **RAG Context Size**

---

# 1. Tokens and Context Window

LLMs have a limited **context window**.

The context window determines how many tokens the model can process within its active context.

Conceptually:

Context Window
      ↓
System Prompt
+
Conversation History
+
User Question
+
RAG Context
+
Generated Response

For example, if a model/application has a context limit of:

128,000 tokens

we need to manage the information placed inside that context.

The exact limits depend on the model.

---

# 2. Tokens and API Cost

Many LLM APIs calculate usage based partly on:

- Input tokens
- Output tokens

Conceptually:

More Tokens
    ↓
More Processing
    ↓
Potentially Higher Cost

This is why token optimization can be important in production applications.

---

# 3. Tokens and Response Length

Output length is also measured in tokens.

For example, an application may configure a maximum output-token limit.

This prevents the model from generating unnecessarily long responses.

---

# 4. Tokens in RAG

Tokens are especially important in RAG.

Suppose we retrieve:

Top-K = 20 chunks

and every chunk contains:

1000 tokens

That could mean roughly:

20,000 tokens

of retrieved context before even considering:

- System prompt
- Conversation history
- User question
- Output

Therefore, we should not blindly retrieve and send too much information.

Instead:

User Query
    ↓
Retrieve Relevant Chunks
    ↓
Rerank
    ↓
Select Best Chunks
    ↓
Send Required Context
    ↓
LLM

---

# Tokens and Chunking

Chunk size is commonly measured in **tokens**.

Example:

Chunk Size = 500 tokens

Overlap = 50 tokens

Conceptually:

Document
    ↓
Chunk 1 → 500 tokens
Chunk 2 → 500 tokens
Chunk 3 → 500 tokens
    ↓
Embeddings
    ↓
Vector DB

This helps us control the amount of information contained in each chunk.

---

# Token vs Word

This is a common interview question.

A **word and token are not the same thing**.

Example:

"Artificial Intelligence"

Humans see:

2 words

But the tokenizer may represent it using a different number of tokens.

Some words may be:

- One token
- Multiple tokens

Punctuation and spaces can also affect tokenization.

Therefore:

> **Never assume 1 word = 1 token.**

---

# Token vs Embedding

Another important distinction:

## Token

A unit of text.

Example:

"Python"

## Token ID

Numerical ID representing that token in the tokenizer vocabulary.

Conceptually:

Python → 8912

## Embedding

A vector representation used by the model.

Conceptually:

8912
 ↓
Embedding
 ↓
[0.21, -0.53, 0.78, ...]

So:

Text
 ↓
Token
 ↓
Token ID
 ↓
Embedding Vector
 ↓
Transformer

---

# Example in RAG

Suppose the user asks:

"What causes settlement failure?"

The question is tokenized:

"What"  
"causes"  
"settlement"  
"failure"

Conceptually.

Then the RAG system retrieves relevant chunks.

Example:

"Settlement can fail because of insufficient securities."

The retrieved text also consumes tokens when it is included in the LLM prompt.

Final prompt:

Context:
Settlement can fail because of insufficient securities.

Question:
What causes settlement failure?

This complete prompt consumes **input tokens**.

The generated answer consumes **output tokens**.

---

# How Can We Reduce Token Usage in RAG?

We can:

- Use appropriate chunk sizes
- Tune Top-K
- Use reranking
- Remove irrelevant context
- Remove duplicate chunks
- Summarize long conversation history when appropriate
- Keep prompts concise
- Retrieve only relevant documents

Example:

Instead of:

Retrieve 20 chunks
     ↓
Send everything to LLM

Use:

Retrieve 20
     ↓
Rerank
     ↓
Best 5
     ↓
LLM

---

# Interview Answer

**"A token is a small unit of text that an LLM processes. Before text is given to the model, a tokenizer breaks it into tokens and maps those tokens to numerical IDs, which are then represented internally as embeddings.**

**A token is not necessarily a complete word; one word can consist of one or multiple tokens depending on the tokenizer.**

**Tokens are important because context-window limits and API usage are measured in tokens. In RAG, retrieved document chunks also consume input tokens, so I need to control chunk size, Top-K, and the amount of context sent to the LLM."**

---

# One-Line Interview Answer

> **A token is a small unit of text processed by an LLM, and token count affects the context window, API usage, response length, and RAG context size.**

---

# Quick Revision

Token
→ Small unit of text

Tokenization
→ Text → Tokens

Token ID
→ Numerical identifier for token

Embedding
→ Vector representation of token

Input Tokens
→ Tokens sent to LLM

Output Tokens
→ Tokens generated by LLM

Context Window
→ Maximum amount of tokenized context the model can process

RAG
→ Retrieved chunks also consume tokens

Important:

**1 Token ≠ 1 Word**

---

# 10-Second Answer

**"Tokens are the basic units of text processed by an LLM. A token may be a word, part of a word, or punctuation depending on the tokenizer. Token count is important because it affects the model's context window, API usage, and how much RAG context we can provide."**

# Context Window in LLM

## What is a Context Window?

The **context window is the maximum amount of tokenized information an LLM can consider within its active context while generating a response.**

In simple terms:

> **Context Window = How much information the LLM can work with at one time.**

It is usually measured in **tokens**.

---

# What is Included in the Context Window?

The context can include:

- System instructions
- User prompt
- Conversation history
- RAG retrieved documents
- Tool outputs
- Other information provided to the model
- Generated output, depending on the model/API setup

Conceptually:

```text
Context Window
│
├── System Prompt
├── Conversation History
├── RAG Retrieved Context
├── User Question
└── Generated Response

# Temperature and Top-P in LLM

## What is Temperature?

**Temperature controls the randomness or creativity of an LLM's output.**

In simple terms:

> **Low Temperature = More predictable/focused output**
>
> **High Temperature = More varied/creative output**

When an LLM generates text, it calculates probabilities for possible next tokens.

Example:

```text
Prompt:
"The capital of India is"

Possible next tokens:

New      → 0.70
Delhi    → 0.15
Mumbai   → 0.05
Kolkata  → 0.03
...

# Hallucination in LLM / RAG

## What is Hallucination?

**Hallucination is when an LLM generates information that sounds confident and believable but is actually incorrect, fabricated, or unsupported by the available context.**

Simple definition:

> **Hallucination = LLM confidently generates information that is not actually supported.**

---

# Simple Example

Suppose the actual company document says:

"Employees receive 20 annual paid leaves."

But the LLM answers:

"Employees receive 30 annual paid leaves."

The answer sounds valid, but it is incorrect.

This is **hallucination**.

---

# Why Do LLMs Hallucinate?

LLMs generate responses using **next-token prediction**.

They predict what text is likely to come next based on:

- Training
- Prompt
- Current context

They are not traditional databases that simply look up a guaranteed fact.

So when information is:

- Missing
- Ambiguous
- Outdated
- Not present in context
- Poorly retrieved

the model may still generate a plausible-looking answer.

---

# Common Causes of Hallucination

## 1. Missing Knowledge

The LLM may not know private or company-specific information.

Example:

"What is my company's leave policy?"

If the LLM doesn't have that information, it may generate an incorrect answer.

---

## 2. Outdated Knowledge

The information may have changed after the model's training or may simply not be represented in its learned knowledge.

Example:

Old Policy:

20 leaves

New Policy:

25 leaves

The model may provide outdated information.

---

## 3. Poor Prompt

An unclear question can lead to an incorrect interpretation.

Example:

"Why did it fail?"

The model doesn't know what "it" refers to.

---

## 4. Poor Retrieval in RAG

Suppose the correct answer is in:

Chunk A

But RAG retrieves:

Chunk B  
Chunk C  
Chunk D

The LLM receives the wrong context and may generate the wrong answer.

---

## 5. Too Much Irrelevant Context

If we retrieve too many chunks:

Top-K = 20

the prompt may contain:

Relevant Information
+
Irrelevant Information
+
Conflicting Information

This can make generation less reliable.

---

# Hallucination in RAG

RAG reduces hallucination by giving the LLM relevant external information.

Without RAG:

User Question
     ↓
LLM
     ↓
Answer from model knowledge

With RAG:

User Question
     ↓
Retrieve Relevant Documents
     ↓
Provide Context
     ↓
LLM
     ↓
Grounded Answer

---

# Does RAG Completely Eliminate Hallucination?

**No.**

This is an important interview point.

> **RAG reduces hallucination but does not completely eliminate it.**

There can still be two major problems.

### Retrieval Failure

Wrong / irrelevant chunks
        ↓
Wrong context
        ↓
Potentially wrong answer

### Generation Failure

Correct chunks
       ↓
LLM misunderstands or ignores information
       ↓
Wrong answer

Therefore:

RAG ≠ Zero Hallucination

---

# How to Reduce Hallucination?

## 1. Improve Retrieval

Make sure the correct documents are being retrieved.

Improve:

- Chunking
- Embeddings
- Top-K
- Retrieval strategy

---

## 2. Use Hybrid Search

Combine:

Dense Search
+
BM25

Dense search finds semantic meaning.

BM25 finds exact keywords.

This can improve retrieval quality.

---

## 3. Use Reranking

Instead of:

Retrieve 20
    ↓
Send all 20

Use:

Retrieve 20
    ↓
Reranker
    ↓
Best 5
    ↓
LLM

This reduces irrelevant context.

---

## 4. Tune Top-K

Too small:

May miss important information.

Too large:

May introduce irrelevant information.

Therefore, Top-K should be evaluated and tuned.

---

## 5. Use Metadata Filtering

Example:

country = India

document_type = HR_POLICY

year = 2026

This prevents unrelated documents from being retrieved.

---

## 6. Use Grounding Prompts

Clearly instruct the model to answer only from retrieved information.

Example:

"Answer the question only using the provided context.

If the answer cannot be found in the context, say 'I don't have enough information.'

Do not invent information."

This is called **grounding**.

---

## 7. Allow the Model to Say "I Don't Know"

Do not force the model to always produce an answer.

If the retrieved context doesn't contain enough information:

Good response:

"I don't have enough information in the provided documents."

This is better than generating a fake answer.

---

## 8. Add Citations

Return:

Answer
+
Source

Example:

"Employees receive 20 annual leaves."

Source:
HR_Policy.pdf
Page 12

This allows users to verify the answer.

---

## 9. Remove Conflicting / Outdated Documents

Suppose the knowledge base contains:

Policy_2024.pdf → 20 leaves

Policy_2026.pdf → 25 leaves

If both are retrieved, the LLM may become confused.

We can use:

- Metadata
- Versioning
- Date filters
- Document lifecycle management

to prioritize the latest information.

---

## 10. Evaluate RAG

Create test questions where we already know:

- Correct document
- Correct chunk
- Correct answer

Then evaluate:

### Retrieval

Did we retrieve the correct information?

### Generation

Did the LLM answer correctly using that information?

This helps identify the actual source of hallucination.

---

# Example

Suppose the knowledge base contains:

"Settlement failed because the seller had insufficient securities."

User asks:

"Why did the trade fail?"

Good RAG flow:

User Question
     ↓
Semantic Search
     ↓
Correct Settlement Chunk
     ↓
Reranking
     ↓
Grounded Prompt
     ↓
LLM
     ↓

"Settlement failed because the seller had insufficient securities."

This answer is **grounded in retrieved information**.

---

# Hallucination vs Wrong Retrieval

These are slightly different.

### Wrong Retrieval

The retriever fails to find the correct information.

Retriever Problem.

### Hallucination

The generated answer contains unsupported or fabricated information.

Generation Problem.

In practice, bad retrieval can lead to hallucinated or incorrect answers.

Therefore, when debugging RAG:

Question
   ↓
Did we retrieve the correct chunks?
   ↓
YES → Check LLM generation/prompt
NO  → Fix retrieval

---

# Does Low Temperature Prevent Hallucination?

**No.**

Lower temperature can make the model more consistent and less random.

But:

Low Temperature ≠ Guaranteed Accuracy

If the model has incorrect/missing context, it can still generate a wrong answer.

To reduce hallucination, focus mainly on:

Better Retrieval
+
Relevant Context
+
Grounding
+
Reranking
+
Citations
+
Evaluation

---

# Interview Answer

**"Hallucination is when an LLM generates information that sounds convincing but is incorrect or unsupported by the available context.**

**It happens because LLMs generate text using probabilistic next-token prediction rather than simply retrieving guaranteed facts from a database.**

**RAG helps reduce hallucination by grounding the model with external information, but it doesn't completely eliminate it.**

**To reduce hallucination, I would improve retrieval and chunking, use hybrid search and reranking, tune Top-K, use metadata filtering, provide strong grounding instructions, allow the model to say it doesn't know when information is missing, and provide citations."**

---

# If Interviewer Asks: "How Will You Reduce Hallucination?"

**"First, I would check whether the problem is retrieval or generation. If retrieval is poor, I would improve chunking, embeddings, Top-K, hybrid search, metadata filtering, and reranking. If retrieval is correct but generation is wrong, I would strengthen the grounding prompt, instruct the model to answer only from context, allow it to say it doesn't know, and provide citations. I would also evaluate retrieval and generation separately."**

---

# One-Line Answer

> **Hallucination is when an LLM generates incorrect or unsupported information that appears believable.**

---

# Quick Revision

Hallucination
→ Incorrect / fabricated / unsupported answer

Main Causes:
→ Missing knowledge
→ Outdated information
→ Poor retrieval
→ Bad prompt
→ Irrelevant/conflicting context

RAG
→ Reduces hallucination
→ Does NOT completely eliminate it

Reduce Hallucination:

Better Chunking
↓
Better Retrieval
↓
Hybrid Search
↓
Tune Top-K
↓
Reranking
↓
Metadata Filtering
↓
Grounding Prompt
↓
"I Don't Know"
↓
Citations
↓
Evaluation

---

# 10-Second Interview Answer

**"Hallucination is when an LLM generates confident but incorrect or unsupported information. RAG reduces it by grounding the model with retrieved documents, and we can further reduce it using better retrieval, reranking, grounding prompts, citations, and allowing the model to say it doesn't know when context is insufficient."**

# Prompt Engineering in LLM / GenAI

## What is Prompt Engineering?

**Prompt engineering is the process of designing and improving instructions given to an LLM so that it produces more accurate, relevant, and structured responses.**

Simple definition:

> **Prompt Engineering = Giving clear instructions + context + constraints + expected output to the LLM.**

---

# Simple Example

### Poor Prompt

"Explain Python."

This is very broad.

### Better Prompt

"You are a Python interviewer.

Explain Python decorators in simple language for a developer with 3 years of experience.

Include:
1. Definition
2. Simple code example
3. Real-world use case

Keep the answer under 200 words."

The second prompt gives the LLM much clearer instructions.

---

# Basic Structure of a Good Prompt

A useful prompt can contain:

Role
+
Task
+
Context
+
Constraints
+
Output Format
+
Examples

Conceptually:

"You are a Python expert."          → Role

"Explain decorators."              → Task

"For a 3-year developer."          → Context

"Keep it under 200 words."         → Constraint

"Return bullet points."            → Output Format

---

# 1. Role

Tell the LLM what role it should perform.

Example:

"You are a senior Python developer."

or

"You are a financial settlement analyst."

This gives the model useful context about the expected perspective.

---

# 2. Clear Task

Clearly specify what you want.

Poor:

"Tell me about settlement."

Better:

"Explain the trade settlement lifecycle from trade execution to final settlement."

---

# 3. Provide Context

Give the model information required to answer correctly.

Example:

"Context:

The settlement failed because the seller had insufficient securities.

Question:

Why did the settlement fail?"

The LLM now has specific information to work with.

---

# 4. Add Constraints

Constraints control the response.

Examples:

"Keep the answer under 150 words."

"Do not use technical jargon."

"Answer only using the provided context."

"Do not generate information that is not present in the documents."

---

# 5. Specify Output Format

Tell the model exactly how the response should look.

Example:

"Return the response as JSON:

{
  'root_cause': '',
  'severity': '',
  'recommendation': ''
}"

This is useful when the output will be consumed by another application.

---

# 6. Provide Examples

Providing examples can help the LLM understand the expected behavior.

Example:

Input:
"ERR-101"

Output:
{
  "category": "Database Error"
}

Input:
"ERR-202"

Output:
{
  "category": "Authentication Error"
}

Now classify:

"ERR-303"

This is called **few-shot prompting**.

---

# Zero-Shot Prompting

**Zero-shot prompting means asking the model to perform a task without giving examples.**

Example:

"Classify the following customer review as Positive, Negative, or Neutral:

'The application is very easy to use.'"

No examples were provided.

Therefore:

Zero-Shot
→ Instructions only
→ No examples

---

# One-Shot Prompting

**One-shot prompting means providing one example before asking the model to perform the task.**

Example:

Example:

"The product is excellent."

Output:
Positive

Now classify:

"The application keeps crashing."

One example was provided.

---

# Few-Shot Prompting

**Few-shot prompting means providing multiple examples before asking the model to perform a task.**

Example:

Example 1:

"I love this product."
→ Positive

Example 2:

"This application is terrible."
→ Negative

Example 3:

"The product is okay."
→ Neutral

Now classify:

"The application works perfectly."

The examples help the model understand the expected pattern.

---

# Zero-Shot vs Few-Shot

Zero-Shot:

Instruction
    ↓
LLM
    ↓
Answer

Few-Shot:

Instruction
+
Examples
    ↓
LLM
    ↓
Answer

Few-shot prompting can be useful when:

- Output format is important
- Classification labels are unusual
- Task behavior needs clarification
- The model needs examples of expected responses

---

# Chain-of-Thought / Reasoning Prompts

For complex problems, prompts can encourage the model to perform structured reasoning.

For production applications, instead of depending on the model to expose detailed internal reasoning, it is often better to request a concise explanation or structured result.

Example:

"Analyze the settlement failure using the provided information.

Return:

Root Cause:
Evidence:
Recommended Action:"

This provides useful reasoning structure without requiring unnecessary internal details.

---

# Prompt Engineering in RAG

Prompt engineering is very important in RAG.

The prompt normally contains:

System Instructions
+
Retrieved Context
+
User Question
+
Output Instructions

Example:

"You are an assistant answering questions from company documents.

Use only the provided context.

Context:
{retrieved_context}

Question:
{user_question}

If the answer cannot be found in the context, say:
'I don't have enough information.'

Do not invent information.

Provide the source if available."

---

# RAG Prompt Flow

User Question
      ↓
Retrieve Relevant Chunks
      ↓
Build Prompt

System Instructions
+
Retrieved Context
+
Question
+
Constraints
      ↓
LLM
      ↓
Grounded Answer

---

# Prompt Engineering to Reduce Hallucination

Instead of:

"Answer this question:
{question}"

Use:

"Answer the question using only the provided context.

If the context does not contain enough information, say that you don't have enough information.

Do not invent facts.

Context:
{context}

Question:
{question}"

This helps **ground** the LLM.

---

# System Prompt vs User Prompt

## System Prompt

Defines overall behavior and rules.

Example:

"You are a capital markets settlement assistant.

Answer questions using only verified settlement information.

Do not invent transaction details."

## User Prompt

Contains the actual request.

Example:

"Why did trade ABC123 fail?"

So:

System Prompt
+
User Prompt
+
Context
      ↓
LLM

---

# Prompt Engineering for Structured Output

Suppose an AI system performs Root Cause Analysis.

Instead of:

"Analyze this settlement."

Use:

"Analyze the following settlement failure.

Return the result in JSON format:

{
  'root_cause': '',
  'risk_level': '',
  'explanation': '',
  'recommended_action': ''
}

Settlement Data:
{settlement_data}"

This makes the output easier for the backend to process.

---

# Prompt Engineering for RAG Example

Suppose retrieved context says:

"Trade ABC123 failed because the seller had insufficient securities."

Prompt:

"You are a settlement investigation assistant.

Use only the provided context.

Context:
Trade ABC123 failed because the seller had insufficient securities.

Question:
Why did trade ABC123 fail?

Return:

Root Cause:
Explanation:
Recommended Action:

If the information is unavailable, say 'Insufficient information'."

Possible output:

Root Cause:
Insufficient securities

Explanation:
The seller did not have enough securities available to complete settlement.

Recommended Action:
Verify the seller's securities position and arrange the required securities before retrying settlement.

---

# Common Prompt Engineering Techniques

## 1. Clear Instructions

Clearly explain the task.

## 2. Role Prompting

Assign a relevant role.

Example:

"You are a settlement analyst."

## 3. Context Injection

Provide relevant information.

## 4. Zero-Shot Prompting

Give instructions without examples.

## 5. One-Shot Prompting

Provide one example.

## 6. Few-Shot Prompting

Provide multiple examples.

## 7. Structured Output

Request JSON or another specific schema.

## 8. Constraints

Specify what the model should and should not do.

## 9. Grounding

Tell the model to answer using provided information.

## 10. Output Validation

Validate the generated response in the application instead of blindly trusting it.

---

# Bad Prompt vs Good Prompt

## Bad

"Analyze settlement."

Problems:

- No context
- No expected output
- No constraints
- No role

## Better

"You are a capital markets settlement analyst.

Analyze the following settlement failure.

Use only the provided information.

Return:

1. Root Cause
2. Risk Level
3. Explanation
4. Recommended Action

If the root cause cannot be determined, return:
'Insufficient information.'

Settlement:
{settlement_data}"

This prompt is much more controlled.

---

# Does Prompt Engineering Eliminate Hallucination?

No.

Prompt engineering can **reduce hallucination**, but it cannot guarantee that hallucinations never occur.

For production RAG systems, combine:

Good Prompt
+
Good Retrieval
+
Reranking
+
Relevant Context
+
Structured Output
+
Validation
+
Citations

---

# Interview Answer

**"Prompt engineering is the process of designing and optimizing instructions given to an LLM so that it produces more accurate, relevant, and structured responses.**

**A good prompt usually contains a clear task, relevant context, constraints, expected output format, and examples when necessary.**

**Common techniques include zero-shot prompting, few-shot prompting, role prompting, grounding, and structured output.**

**In RAG, I use prompt engineering to provide the retrieved context to the LLM and instruct it to answer only from that context. If the information is unavailable, I can instruct the model to say it doesn't have enough information instead of inventing an answer."**

---

# If Interviewer Asks: How Do You Write a Good Prompt?

**"I usually define the role and task clearly, provide only the relevant context, specify constraints, define the expected output format, and provide examples if the task is difficult or format-sensitive. For RAG, I also add grounding instructions and tell the model not to generate unsupported information."**

---

# One-Line Answer

> **Prompt engineering is the process of designing clear instructions, context, constraints, and output formats to guide an LLM toward the desired response.**

---

# Quick Revision

Prompt Engineering
        ↓
Role
+
Clear Task
+
Context
+
Constraints
+
Output Format
+
Examples
        ↓
Better LLM Response

Zero-Shot
→ No examples

One-Shot
→ One example

Few-Shot
→ Multiple examples

Grounding
→ Answer using provided context

Structured Output
→ JSON / defined schema

RAG Prompt
→ Instructions + Retrieved Context + Question

---

# 10-Second Interview Answer

**"Prompt engineering means designing effective instructions for an LLM. I define the role, task, context, constraints, and expected output format, and use zero-shot or few-shot examples when required. In RAG, I also ground the model by instructing it to answer only from retrieved context."**

# Structured Output in LLM

## What is Structured Output?

**Structured output means making an LLM return its response in a predefined format, usually JSON or a specific schema, instead of normal free-form text.**

### Example

Instead of:

"The trade failed because of insufficient securities and the risk is high."

We return:

{
  "root_cause": "Insufficient securities",
  "risk_level": "High",
  "recommended_action": "Check securities balance"
}

## Why Use Structured Output?

- Makes LLM responses predictable
- Easy for backend code to parse
- Easy to validate
- Useful for APIs and databases
- Useful in AI workflows where one step's output becomes another step's input

### Simple Flow

LLM
↓
Structured JSON
↓
Django / FastAPI
↓
Database / Frontend / Next Workflow Step

## Interview Answer

"Structured output means getting the LLM response in a predefined format such as JSON instead of free-form text. It is useful when the response needs to be processed by another application. For example, in a settlement RCA system, instead of returning a paragraph, I can return root cause, risk level, and recommendation as JSON. In production, I prefer schema-based structured output when supported because it makes the response easier to validate and process."

## Remember

Structured Output = **LLM Response in JSON / Schema**

Main benefit = **Predictable + Easy to Parse + Easy to Validate**

# Function Calling / Tool Calling in LLM

## What is Function / Tool Calling?

**Tool calling allows an LLM to interact with external functions, APIs, databases, or services instead of only generating text.**

The LLM decides **which tool to call and what arguments to provide**, while the application actually executes the tool.

### Simple Flow

User Question
↓
LLM
↓
Select Tool + Arguments
↓
Application Executes Tool
↓
Tool Result
↓
LLM
↓
Final Answer

## Example

User asks:

"What is the status of trade ABC123?"

Available tool:

get_trade_status(trade_id)

The LLM can generate a tool call like:

get_trade_status("ABC123")

The backend executes it and returns:

{
  "trade_id": "ABC123",
  "status": "Failed",
  "reason": "Insufficient securities"
}

The result is provided back to the LLM, which answers:

"Trade ABC123 failed because of insufficient securities."

## Why Use Tool Calling?

- Access real-time information
- Query databases
- Call external APIs
- Perform calculations
- Create tickets
- Send notifications
- Execute business workflows

## Tool Calling vs RAG

**RAG**
→ Retrieves information from a knowledge base.

**Tool Calling**
→ Executes a function/API/action.

Example:

"Explain our settlement failure policy."
→ RAG

"Check the current status of trade ABC123."
→ Tool Calling

"Create a Jira ticket for trade ABC123."
→ Tool Calling

## Important Interview Point

The **LLM does not directly execute the function**.

It generally identifies:

- Which tool to use
- What arguments to pass

The application/tool layer performs the actual execution and returns the result.

## Interview Answer

"Function or tool calling allows an LLM to interact with external systems such as APIs, databases, or application functions. We define the available tools and their parameters, and based on the user's request, the LLM can select the appropriate tool and generate the required arguments. The application executes that tool and sends the result back to the LLM for the final response. For example, an LLM could call a get_trade_status function to retrieve the latest settlement status instead of hallucinating it."

## Remember

Tool Calling:

User
↓
LLM
↓
Choose Tool
↓
Generate Arguments
↓
Execute Tool
↓
Return Result
↓
LLM
↓
Final Answer

**RAG = Retrieve Knowledge**

**Tool Calling = Use Functions/APIs to get data or perform actions**

# Agent vs LLM

## What is an LLM?

An **LLM (Large Language Model)** takes a prompt and generates a response.

Simple flow:

User Prompt
↓
LLM
↓
Response

Example:

User: "Explain why a settlement can fail."

LLM: "A settlement can fail because of insufficient securities, cash shortage, SSI mismatch, etc."

The LLM mainly **understands and generates text**.

---

## What is an AI Agent?

An **AI Agent uses an LLM as its reasoning component but can also use tools, maintain state, make decisions, and perform multiple steps to achieve a goal.**

Simple flow:

User Goal
↓
Agent
↓
LLM decides what to do
↓
Use Tool / API
↓
Check Result
↓
Decide Next Step
↓
Use Another Tool
↓
Final Result

---

## Example

User says:

"Investigate why trade ABC123 failed and create a ticket if required."

### LLM Only

The LLM can explain possible reasons, but it does not automatically know the actual trade status.

### Agent

The agent can:

1. Fetch trade ABC123
2. Check SSI instructions
3. Check securities holdings
4. Check cash balance
5. Identify the root cause
6. Generate RCA using LLM
7. Create a Jira ticket
8. Send a notification

So the agent performs a **multi-step workflow**.

---

## LLM vs Agent

| LLM | Agent |
|---|---|
| Generates responses | Performs tasks |
| Usually prompt → response | Goal → multiple steps |
| No tools required | Can use tools/APIs |
| Limited to provided context | Can fetch external information |
| Doesn't inherently manage workflow | Can maintain state/workflow |
| Mainly generation/reasoning | Reasoning + tools + actions |

---

## Important Relationship

An agent is not a replacement for an LLM.

Usually:

**Agent = LLM + Tools + State/Memory + Decision Logic + Workflow**

The LLM acts like the **reasoning engine**, while the agent architecture allows it to interact with external systems and complete tasks.

---

## Interview Answer

"An LLM mainly takes a prompt and generates a response, whereas an AI agent uses an LLM as a reasoning engine along with tools, state, and decision-making logic to complete a goal. For example, an LLM can explain possible reasons for settlement failure, but an agent can fetch the trade, check SSI, securities and cash balances, identify the root cause, create a Jira ticket, and send a notification. So an LLM generates or reasons, while an agent can reason and take actions."

## Remember

**LLM**
→ Prompt → Response

**Agent**
→ Goal → Reason → Use Tools → Observe Result → Take Next Action → Final Result

**Agent = LLM + Tools + State + Decision Making + Actions**

# Agent vs RAG

## What is RAG?

**RAG (Retrieval-Augmented Generation)** retrieves relevant information from an external knowledge base and provides it to the LLM as context.

### Flow

User Question
↓
Retrieve Relevant Documents
↓
Add Context
↓
LLM
↓
Answer

Example:

User:

"What does our settlement policy say about failed trades?"

RAG retrieves the relevant policy document and the LLM generates an answer from it.

---

## What is an AI Agent?

**An AI Agent uses an LLM with tools, state, and decision-making logic to perform tasks and achieve a goal.**

### Flow

User Goal
↓
Agent
↓
Decide Next Step
↓
Use Tool / API
↓
Observe Result
↓
Decide Next Action
↓
Final Result

Example:

"Investigate trade ABC123 and resolve the settlement failure."

Agent can:

1. Fetch trade details
2. Check SSI
3. Check securities holdings
4. Check cash balance
5. Identify root cause
6. Generate RCA
7. Create Jira ticket
8. Send notification

---

## Agent vs RAG

| RAG | Agent |
|---|---|
| Retrieves knowledge | Performs tasks/actions |
| Mainly retrieval + generation | Reasoning + tools + actions |
| Usually follows a defined retrieval flow | Can decide the next step dynamically |
| Searches documents/knowledge base | Can call APIs, DBs, tools, RAG, etc. |
| Used for grounded Q&A | Used for multi-step workflows |

---

## Can an Agent Use RAG?

**Yes. RAG itself can be one of the tools available to an agent.**

Example:

User Goal
↓
Agent
↓
Check Trade Database
↓
Retrieve Settlement Policy using RAG
↓
Check Securities
↓
Generate RCA
↓
Create Ticket
↓
Final Response

So:

> **RAG gives the agent knowledge, while tools allow the agent to take actions.**

---

## Interview Answer

"RAG and agents solve different problems. RAG retrieves relevant information from a knowledge base and provides it as context to an LLM for grounded answers. An AI agent is designed to achieve a goal by reasoning, using tools, maintaining state, and performing multiple actions. An agent can also use RAG as one of its tools. For example, RAG can retrieve settlement policies, while an agent can additionally check trade data, verify balances, perform RCA, and create a ticket."

## Remember

**RAG**
→ Retrieve Knowledge → Generate Answer

**Agent**
→ Reason → Use Tools → Take Actions → Complete Goal

**Agent can use RAG as a tool.**

# Agentic AI + LLM Interview Notes

## 1. Tools

**Tools are external functions, APIs, databases, or services that an AI agent can use to get information or perform actions.**

Examples:

- Search database
- Call REST API
- Retrieve documents
- Send email
- Create Jira ticket
- Perform calculations

### Flow

User Goal
↓
Agent / LLM
↓
Select Tool
↓
Execute Tool
↓
Get Result
↓
Continue Workflow

### Example

User:

"Check trade ABC123 status."

Agent chooses:

get_trade_status("ABC123")

The backend executes the function and returns the result.

### Interview Answer

"Tools allow an AI agent to interact with external systems. The LLM can decide which tool to use and provide the required arguments, while the application executes the tool and returns the result."

---

# 2. Memory vs State

## State

**State is the information required to track the current workflow or execution.**

Example:

Trade ID = ABC123  
SSI Check = Passed  
Cash Check = Passed  
Securities Check = Failed  
Current Step = RCA

The agent uses this state to know what has already happened and what should happen next.

## Memory

**Memory stores useful information that can be reused across interactions or over a longer period.**

Example:

- Previous user preferences
- Previous conversations
- Previous investigation results

Simple difference:

**State = Current workflow information**

**Memory = Information remembered across interactions/workflows**

### Interview Answer

"State tracks information during the current agent workflow, such as tool results and the current step. Memory is used to retain useful information across interactions. For example, in a settlement investigation, trade details and validation results would be part of the current state."

---

# 3. Planning

**Planning means deciding what steps or actions are required to achieve a goal.**

Example:

Goal:

"Investigate settlement failure."

Plan:

1. Fetch trade
2. Validate SSI
3. Check securities
4. Check cash
5. Determine root cause
6. Generate recommendation
7. Escalate if required

An agent may determine the next action dynamically based on previous results.

### Interview Answer

"Planning is the agent's ability to determine the steps required to achieve a goal. Instead of directly generating an answer, it can break a task into smaller steps and decide what tool or action should be executed next."

---

# 4. Orchestration

**Orchestration means coordinating multiple steps, tools, agents, and workflows in the correct order.**

Example:

Upload SWIFT
↓
Parse Message
↓
Fetch Trade
↓
Validate SSI
↓
Check Holdings
↓
Check Cash
↓
Generate RCA
↓
Create Ticket
↓
Send Notification

An orchestration framework controls:

- What runs next
- What data is passed between steps
- Conditional decisions
- Error handling
- Workflow state

Examples of frameworks:

- LangGraph
- LangChain
- Semantic Kernel

### Interview Answer

"Orchestration means coordinating multiple AI steps and tools as a workflow. It controls execution order, state passing, conditional decisions, and which tool or agent should run next."

---

# 5. Human-in-the-Loop (HITL)

**Human-in-the-loop means requiring human review or approval at important points before the AI continues or performs a sensitive action.**

Example:

Agent detects:

Settlement Risk = HIGH

Instead of automatically creating an escalation:

Agent
↓
Generate Recommendation
↓
Pause
↓
Human Reviews
↓
Approve / Reject
↓
Continue Workflow

Useful for:

- Financial decisions
- High-risk actions
- Production changes
- Legal workflows
- Sensitive approvals

### Interview Answer

"Human-in-the-loop means adding human approval or review at important stages of an AI workflow. For example, if an agent identifies a high-risk settlement issue, it can pause and request analyst approval before taking an escalation action."

---

# 6. Gemini

**Gemini is Google's family of multimodal generative AI models.**

It can work with different types of inputs depending on the model, such as:

- Text
- Images
- Audio
- Video
- Code

Gemini models can be accessed through Google's AI platforms/APIs, including Vertex AI for enterprise cloud applications.

### Example

User Input
↓
Django Backend
↓
Gemini
↓
Generate Structured Content
↓
Return Response

### Interview Answer

"Gemini is Google's family of multimodal generative AI models. I can use it for tasks such as text generation, structured generation, image understanding, and multimodal AI workflows. For enterprise applications, Gemini can be integrated through Vertex AI."

---

# 7. Azure OpenAI

**Azure OpenAI provides access to OpenAI models through Microsoft's Azure cloud platform.**

It allows enterprise applications to integrate capabilities such as:

- LLM generation
- Embeddings
- Structured outputs
- Tool calling
- RAG applications

### Example Architecture

Application
↓
Azure OpenAI
↓
LLM
↓
Generated Response

It can also be combined with:

Azure AI Search
↓
Retrieve Documents
↓
Azure OpenAI
↓
RAG Answer

### Why Use Azure OpenAI?

- Azure ecosystem integration
- Enterprise security/governance features
- Identity and access controls
- Monitoring and cloud deployment integration

### Interview Answer

"Azure OpenAI provides access to OpenAI models through the Azure platform. I can use it for LLM generation, embeddings, tool calling, and RAG applications while integrating with Azure services such as Azure AI Search, App Service, and other enterprise infrastructure."

---

# 8. Ollama

**Ollama is a tool that makes it easy to run supported LLMs locally.**

Examples of models commonly used through Ollama include:

- Llama
- Mistral
- Gemma
- Qwen

### Flow

Application
↓
Ollama
↓
Local LLM
↓
Response

Example:

Django / Python
↓
Ollama API
↓
Llama
↓
Generated Content

### Why Use Ollama?

- Run models locally
- Useful for development/testing
- Data can stay on local infrastructure
- No per-request cloud API charge for the model itself
- Useful for experimenting with open-weight models

### Limitations

- Requires local compute/resources
- Larger models may need significant RAM/GPU
- Performance depends on hardware
- Cloud APIs may provide easier scaling and managed infrastructure

### Interview Answer

"Ollama is a tool for running supported LLMs locally, such as Llama, Mistral, Gemma, or Qwen. It is useful for local development, privacy-sensitive use cases, and experimenting without depending on a hosted LLM API. The trade-off is that inference performance and scalability depend on the available hardware."

---

# Quick Revision

## Tools

**Agent interacts with external systems**

Examples:
API, Database, Search, Jira, Email

## State

**Tracks current workflow**

Example:
Trade → SSI checked → Cash checked → RCA

## Memory

**Stores information for reuse across interactions**

## Planning

**Decides what steps are required**

Goal → Plan → Actions

## Orchestration

**Coordinates the complete workflow**

Tools + Steps + State + Conditions

## Human-in-the-Loop

**Human approval before important actions**

AI Recommendation → Human Approval → Action

## Gemini

**Google's multimodal LLM family**

Common enterprise integration → Vertex AI

## Azure OpenAI

**OpenAI models through Microsoft Azure**

Useful for enterprise GenAI/RAG applications

## Ollama

**Run supported LLMs locally**

Useful for local/private development

---

# Final Agent Architecture

User Goal
↓
Agent / LLM
↓
Planning
↓
State
↓
Choose Tool
↓
Execute Tool
↓
Observe Result
↓
Conditional Decision
↓
Human Approval (if required)
↓
Next Tool / Action
↓
Final Result

### Remember

**Tools = What the agent can use**

**State = What is happening now**

**Memory = What it remembers**

**Planning = What should I do?**

**Orchestration = In what order should everything run?**

**HITL = Should a human approve this?**

**Gemini = Google LLM**

**Azure OpenAI = OpenAI models via Azure**

**Ollama = Run LLMs locally**