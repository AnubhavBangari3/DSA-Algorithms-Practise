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

