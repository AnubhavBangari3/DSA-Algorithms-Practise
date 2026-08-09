# GenAI + Agentic AI — Interview Cheat Sheet

## 1. What is an LLM?

**LLM stands for Large Language Model.**

It is an AI model, usually based on the **Transformer architecture**, trained on large amounts of text to understand and generate language.

Examples:

* GPT
* Gemini
* Claude
* Llama
* Mistral

Basic flow:

```text
Prompt
  ↓
Tokenization
  ↓
Transformer + Attention
  ↓
Next Token Prediction
  ↓
Response
```

**Interview Answer:**

> An LLM is a large neural network, usually based on Transformers, trained on massive text data. It processes text as tokens and generates responses by predicting the next token based on the available context.

---

# 2. What are Tokens?

A **token is a small unit of text processed by an LLM**.

A token can be:

* A word
* Part of a word
* Punctuation

So:

```text
1 token ≠ always 1 word
```

Tokens matter because they affect:

* Context window
* API cost
* Input/output size
* RAG context size

**Interview Answer:**

> Tokens are the basic units of text processed by an LLM. The tokenizer converts text into tokens before sending them to the model, and token count affects context limits and API usage.

---

# 3. What is a Context Window?

The **context window is the maximum amount of tokenized information an LLM can work with at one time.**

It can contain:

```text
System Prompt
+
Conversation History
+
User Question
+
RAG Context
+
Tool Results
```

If we provide too much unnecessary context, it can increase cost and reduce response quality.

**Interview Answer:**

> The context window defines how much information the LLM can consider during a request. It includes prompts, conversation history, retrieved RAG context, and other supplied information, and is measured in tokens.

---

# 4. Temperature

Temperature controls **randomness and creativity**.

### Low Temperature

```text
0.1 – 0.3
```

More focused and predictable.

Useful for:

* RAG
* Factual Q&A
* Extraction
* Code

### Higher Temperature

```text
0.7 – 1.0
```

More varied and creative.

Useful for:

* Stories
* Brainstorming
* Creative content

**Interview Answer:**

> Temperature controls randomness during token generation. Lower temperature gives more predictable output, while higher temperature produces more varied and creative responses.

---

# 5. Top-P

Top-P controls **how much of the token probability distribution is considered during generation**.

Example:

```text
Top-P = 0.9
```

The model considers likely tokens covering roughly 90% of the probability mass.

### Easy Difference

```text
Temperature → Controls randomness

Top-P → Controls probability range considered
```

Usually, I don't aggressively tune both simultaneously unless required.

---

# 6. Hallucination

Hallucination happens when an LLM generates information that sounds correct but is **incorrect or unsupported**.

Example:

Actual policy:

```text
20 annual leaves
```

LLM says:

```text
30 annual leaves
```

### How to reduce hallucination?

* RAG
* Better retrieval
* Grounding prompts
* Reranking
* Tool calling
* Citations
* Allow "I don't know"
* Output validation

Important:

> **RAG reduces hallucination but does not completely eliminate it.**

**Interview Answer:**

> Hallucination is when an LLM generates incorrect or unsupported information. I reduce it using RAG, better retrieval, grounding prompts, tool calling, citations, and by allowing the model to say it doesn't know when information is unavailable.

---

# 7. Prompt Engineering

Prompt engineering means designing clear instructions so the LLM produces the expected response.

A good prompt can contain:

```text
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
```

Example:

```text
You are a settlement analyst.

Analyze the provided trade.

Use only the provided information.

Return:
- Root Cause
- Risk
- Recommendation
```

### Zero-Shot

No examples.

### One-Shot

One example.

### Few-Shot

Multiple examples.

**Interview Answer:**

> Prompt engineering means designing clear instructions, context, constraints, and output formats for an LLM. I can also use zero-shot or few-shot examples and grounding instructions depending on the task.

---

# 8. Structured Output

Structured output means asking the LLM to return a **predefined structure instead of free-form text**.

Usually JSON.

Example:

```json
{
  "root_cause": "Insufficient securities",
  "risk": "High",
  "recommendation": "Check securities balance"
}
```

Useful because backend applications can easily:

* Parse it
* Validate it
* Store it
* Pass it to another workflow

**Interview Answer:**

> Structured output means returning the LLM response in a predefined schema such as JSON. It makes the response predictable and easier for backend applications to parse and validate.

---

# 9. Function / Tool Calling

Tool calling allows an LLM to interact with **external functions, APIs, databases, or services**.

Example:

User:

```text
What is the status of trade ABC123?
```

Available tool:

```text
get_trade_status(trade_id)
```

Flow:

```text
User
 ↓
LLM
 ↓
Choose Tool
 ↓
Generate Arguments
 ↓
Application Executes Tool
 ↓
Tool Result
 ↓
LLM
 ↓
Final Answer
```

Important:

> The LLM generally **selects the tool and arguments**. The application actually executes it.

Tools can:

* Query database
* Call REST API
* Search documents
* Create Jira ticket
* Send email
* Perform calculations

**Interview Answer:**

> Tool calling allows an LLM to interact with external systems. The model selects an appropriate tool and generates its arguments, while the application executes the function and returns the result to the LLM.

---

# 10. RAG vs Tool Calling

### RAG

Retrieves knowledge.

Example:

```text
What does our settlement policy say?
```

### Tool Calling

Gets live information or performs an action.

Example:

```text
Check trade ABC123 status.
```

or:

```text
Create a Jira ticket.
```

Remember:

> **RAG = Retrieve Knowledge**

> **Tool Calling = Get live data / Perform Action**

---

# 11. What is an AI Agent?

An AI Agent uses an LLM as a reasoning component but can also:

* Use tools
* Maintain state
* Make decisions
* Perform multiple steps
* Take actions

Basic architecture:

```text
Goal
 ↓
LLM / Agent
 ↓
Decide Action
 ↓
Use Tool
 ↓
Observe Result
 ↓
Decide Next Action
 ↓
Final Result
```

Simple formula:

> **Agent = LLM + Tools + State/Memory + Decision Logic + Actions**

---

# 12. Agent vs LLM

### LLM

```text
Prompt → Response
```

Mainly understands, reasons and generates.

### Agent

```text
Goal
 ↓
Reason
 ↓
Use Tool
 ↓
Observe
 ↓
Take Next Action
 ↓
Complete Goal
```

Example:

LLM:

> Explains possible reasons why settlement failed.

Agent:

```text
Fetch Trade
↓
Check SSI
↓
Check Securities
↓
Check Cash
↓
Find Root Cause
↓
Create Ticket
```

**Interview Answer:**

> An LLM mainly takes a prompt and generates a response. An agent uses an LLM along with tools, state and decision logic to perform multiple steps and complete a goal.

---

# 13. Agent vs RAG

### RAG

```text
Question
 ↓
Retrieve Knowledge
 ↓
LLM
 ↓
Answer
```

Main purpose:

**Grounded knowledge retrieval**

### Agent

```text
Goal
 ↓
Reason
 ↓
Use Tools
 ↓
Take Actions
 ↓
Complete Goal
```

Main purpose:

**Task execution**

Example:

RAG:

```text
What does the settlement policy say?
```

Agent:

```text
Investigate trade ABC123 and create a ticket if required.
```

Important:

> **An Agent can use RAG as one of its tools.**

**Interview Answer:**

> RAG mainly retrieves knowledge and provides it to an LLM, while an agent performs multi-step tasks using reasoning, tools and actions. An agent can also use RAG whenever it needs knowledge from documents.

---

# 14. Tools in Agentic AI

Tools are external capabilities available to the agent.

Examples:

```text
Database
REST API
RAG Retriever
Search
Calculator
Jira
Email
Teams
```

Example:

```text
Agent
 ↓
get_trade()
 ↓
check_balance()
 ↓
create_ticket()
 ↓
send_notification()
```

**Interview Answer:**

> Tools allow an agent to interact with external systems. The agent can select the required tool based on the current goal and use its result to decide the next step.

---

# 15. State

State stores information about the **current workflow execution**.

Example:

```text
Trade ID = ABC123

SSI Check = Passed
Cash Check = Passed
Securities Check = Failed

Current Step = RCA
```

The agent uses state to understand:

```text
What happened?
What is the current step?
What should happen next?
```

**Interview Answer:**

> State contains information required during the current agent workflow, such as previous tool results, current step and intermediate outputs.

---

# 16. Memory

Memory stores information that can be reused across interactions or workflows.

Examples:

* Previous conversation
* User preferences
* Previous investigation
* Important historical information

### Easy Difference

```text
State
= Current workflow information

Memory
= Information remembered for future interactions
```

---

# 17. Planning

Planning means deciding **which steps are required to achieve a goal**.

Example:

Goal:

```text
Investigate settlement failure
```

Plan:

```text
1. Fetch Trade
2. Validate SSI
3. Check Securities
4. Check Cash
5. Find Root Cause
6. Generate Recommendation
7. Escalate if required
```

An agent can also change its next action based on previous results.

**Interview Answer:**

> Planning is the agent's ability to break a goal into smaller steps and decide which actions or tools should be executed to complete the task.

---

# 18. Orchestration

Orchestration means **coordinating multiple steps, tools and decisions in the correct order**.

Example:

```text
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
```

Orchestration manages:

* Execution order
* State passing
* Conditional logic
* Tool calls
* Error handling
* Workflow transitions

Frameworks can include:

* LangGraph
* LangChain
* Semantic Kernel

**Interview Answer:**

> Orchestration means coordinating the complete AI workflow, including tools, execution order, state passing, conditional decisions and error handling.

---

# 19. Human-in-the-Loop (HITL)

Human-in-the-loop means adding **human approval or review before important actions**.

Example:

```text
Agent Finds High Risk
       ↓
Generate Recommendation
       ↓
Pause Workflow
       ↓
Human Approval
     ↙     ↘
 Approve   Reject
    ↓
Continue
```

Useful for:

* Financial decisions
* Production changes
* Legal workflows
* High-risk actions
* Sensitive approvals

**Interview Answer:**

> Human-in-the-loop means adding human review or approval at important stages. For example, an AI agent can pause before escalating a high-risk settlement issue and continue only after analyst approval.

---

# 20. Gemini

**Gemini is Google's family of multimodal generative AI models.**

Depending on the model, it can work with:

* Text
* Images
* Audio
* Video
* Code

For enterprise applications, Gemini can be integrated through **Vertex AI**.

Example:

```text
Django
 ↓
Vertex AI
 ↓
Gemini
 ↓
Structured Response
```

**Interview Answer:**

> Gemini is Google's family of multimodal generative AI models. It can handle text and other modalities depending on the model, and I can integrate it into enterprise applications through Vertex AI.

---

# 21. Azure OpenAI

Azure OpenAI provides access to **OpenAI models through Microsoft Azure**.

Can be used for:

* Text generation
* Embeddings
* RAG
* Tool calling
* Structured output

Example RAG architecture:

```text
Application
     ↓
Azure AI Search
     ↓
Relevant Documents
     ↓
Azure OpenAI
     ↓
Answer
```

Benefits:

* Azure ecosystem integration
* Enterprise security/governance
* Identity/access control
* Cloud monitoring
* Integration with other Azure services

**Interview Answer:**

> Azure OpenAI provides OpenAI models through Microsoft's Azure platform. I can use it for generation, embeddings, RAG and tool calling while integrating it with Azure services such as Azure AI Search and App Service.

---

# 22. Ollama

Ollama makes it easy to run supported LLMs **locally**.

Examples:

* Llama
* Mistral
* Gemma
* Qwen

Architecture:

```text
Django / Python
      ↓
Ollama
      ↓
Local LLM
      ↓
Response
```

### Advantages

* Local development
* Data can stay locally
* No per-request hosted model API charge
* Good for experimenting

### Limitations

* Requires local RAM/GPU/CPU
* Performance depends on hardware
* Scaling is harder than managed cloud APIs

**Interview Answer:**

> Ollama is a tool for running supported LLMs locally. It is useful for development, experimentation and privacy-sensitive use cases, but performance and scalability depend on the available hardware.

---

# 23. Cloud LLM vs Local LLM

### Cloud

Examples:

```text
Gemini / Vertex AI
Azure OpenAI
```

Advantages:

* Easy scaling
* Managed infrastructure
* Powerful models
* Enterprise integrations

Disadvantages:

* API cost
* Network dependency
* Data/governance considerations

### Local

Example:

```text
Ollama + Llama
```

Advantages:

* More control
* Local data processing
* Useful for development
* No hosted API cost per request

Disadvantages:

* Hardware required
* Harder scaling
* Infrastructure management

---

# 24. Complete Agentic AI Architecture

```text
                User Goal
                    ↓
               AI Agent / LLM
                    ↓
                 Planning
                    ↓
                  State
                    ↓
             Choose Next Tool
                    ↓
       ┌────────────┼─────────────┐
       ↓            ↓             ↓
      RAG       Database/API    External Tool
       ↓            ↓             ↓
       └────────────┼─────────────┘
                    ↓
               Tool Result
                    ↓
               Update State
                    ↓
             Conditional Decision
                    ↓
          Human Approval if Needed
                    ↓
              Next Action / Tool
                    ↓
                Final Result
```

---

# 25. Rapid-Fire Interview Revision

### What is LLM?

> Transformer-based model trained on large amounts of data that generates text using next-token prediction.

### Token?

> Small unit of text processed by an LLM.

### Context Window?

> Maximum tokenized information the model can consider at one time.

### Temperature?

> Controls randomness and creativity.

### Top-P?

> Controls the probability mass considered during token selection.

### Hallucination?

> Incorrect or unsupported information generated by an LLM.

### Prompt Engineering?

> Designing clear instructions, context, constraints and output format for an LLM.

### Structured Output?

> Returning output in a predefined format such as JSON/schema.

### Tool Calling?

> Allows an LLM to select external functions/APIs and provide arguments for execution.

### LLM vs Agent?

> LLM generates/reasons; agent uses LLM + tools + state + actions to complete goals.

### RAG vs Agent?

> RAG retrieves knowledge; an agent performs multi-step tasks and actions.

### Tools?

> External capabilities such as APIs, DBs, RAG, Jira or email.

### State?

> Information about the current workflow execution.

### Memory?

> Information retained for reuse across interactions.

### Planning?

> Deciding which steps/actions are required to achieve a goal.

### Orchestration?

> Coordinating tools, steps, state and conditional workflow execution.

### Human-in-the-Loop?

> Human approval/review before important AI actions.

### Gemini?

> Google's multimodal generative AI model family.

### Azure OpenAI?

> OpenAI models available through Microsoft's Azure platform.

### Ollama?

> Tool for running supported LLMs locally.

---

# 30-Second Agentic AI Answer

> An AI agent uses an LLM as its reasoning engine along with tools, state, memory and decision logic to achieve a goal. Instead of simply answering a prompt, the agent can plan multiple steps, call APIs or databases, observe the results and decide what action to perform next. We can orchestrate these steps using frameworks such as LangGraph or Semantic Kernel and add human-in-the-loop approval for sensitive actions.

---

# Final Memory Lines

```text
LLM = Prompt → Response

RAG = Retrieve Knowledge → LLM → Answer

Tool Calling = LLM → Tool/API → Result

Agent = LLM + Tools + State + Decision Making + Actions
```

```text
Temperature = Randomness

Top-P = Probability Mass

State = Current Workflow

Memory = Remembered Information

Planning = What Should I Do?

Orchestration = In What Order?

HITL = Does Human Approval Matter?
```

```text
Gemini = Google GenAI

Azure OpenAI = OpenAI Models via Azure

Ollama = Run LLMs Locally
```
