# LangChain + LangGraph + MCP — Interview Notes

## 1. LangChain

**LangChain is a framework for building LLM applications by connecting LLMs with prompts, retrievers, vector databases, tools, and external systems.**

Common uses:
- RAG
- Prompt templates
- LLM integration
- Retrievers
- Tool calling
- Structured output

Simple Flow:

User Question
↓
Retriever
↓
Relevant Context
↓
Prompt
↓
LLM
↓
Answer

**Interview Answer:**

"LangChain provides building blocks for LLM applications such as prompts, models, retrievers, vector databases, and tools. I can use it to build RAG pipelines and tool-enabled LLM applications."

---

## 2. LangGraph

**LangGraph is used to build stateful, multi-step AI agent workflows using a graph-based architecture.**

It is useful when we need:

- Multiple steps
- Conditional decisions
- Loops
- Shared state
- Tool calling
- Human-in-the-loop

Simple Flow:

START
↓
Fetch Trade
↓
Check SSI
↓
SSI Valid?
├── Yes → Check Securities
└── No → Generate RCA
↓
END

**Interview Answer:**

"LangGraph is used for building stateful multi-step agent workflows. It represents tasks as nodes and connects them using edges. It supports conditional routing, cycles, state management, and human-in-the-loop."

---

## 3. LangChain vs LangGraph

**LangChain**
→ Provides LLM application components.

**LangGraph**
→ Orchestrates complex workflows using those components.

Easy way to remember:

LangChain = Components

LangGraph = Workflow

Example:

LangChain:
Prompt + LLM + Retriever + Tools

LangGraph:
Controls when and in what order those components execute.

---

## 4. Chains vs Graphs

### Chain

A chain normally follows a mostly linear sequence.

Input
↓
Retriever
↓
LLM
↓
Output

Best when workflow is predictable.

### Graph

A graph supports:

- Branching
- Conditions
- Loops
- Multiple paths

Example:

Check SSI
↓
SSI Valid?
├── No → RCA
└── Yes → Check Securities

**Remember:**

Chain = Mostly Linear

Graph = Dynamic Workflow

---

## 5. State

**State is the shared information that moves through a LangGraph workflow.**

Example:

trade_id = ABC123
ssi_status = passed
cash_status = passed
security_status = failed
root_cause = insufficient securities

Different nodes can read and update this state.

**Interview Answer:**

"State stores the current workflow information and allows different nodes to share and update data."

---

## 6. Nodes

**A node represents a task or function in LangGraph.**

Examples:

- Fetch Trade
- Check SSI
- Check Cash
- Check Securities
- Call LLM
- Generate RCA
- Create Ticket

Example:

Fetch Trade Node
↓
SSI Validation Node
↓
Cash Check Node

**Interview Answer:**

"A node is a unit of work in LangGraph. It usually reads the current state, performs some task, and returns updated state."

---

## 7. Edges

**Edges define how execution moves from one node to another.**

Example:

Fetch Trade
↓
Validate SSI

The connection between these two nodes is an edge.

**Interview Answer:**

"Edges define transitions between nodes in the workflow."

---

## 8. Conditional Edges

**Conditional edges dynamically decide which node should execute next based on the current state.**

Example:

Check SSI
↓
SSI Valid?
├── Yes → Check Securities
└── No → Generate RCA

Logic:

if SSI failed:
    go to Generate RCA
else:
    go to Check Securities

**Interview Answer:**

"Conditional edges allow dynamic routing in LangGraph. The next node is selected based on the current state or previous node result."

---

## 9. Cycles

**A cycle allows the workflow to return to a previous node and repeat a step.**

Example:

Generate Answer
↓
Validate Answer
↓
Answer Valid?
├── Yes → END
└── No → Generate Again

Cycles are useful for:

- Retry logic
- Validation
- Agent loops
- Tool retry
- Human feedback

**Interview Answer:**

"Cycles allow the graph to repeat previous steps until a particular condition is satisfied."

---

## 10. Design a LangGraph for a Condition

Interview Question:

"Design an agent to investigate settlement failure."

Answer:

START
↓
Fetch Trade
↓
Validate SSI
↓
SSI Failed?
├── Yes → Generate RCA
└── No
      ↓
Check Securities
↓
Securities Insufficient?
├── Yes → Generate RCA
└── No
      ↓
Check Cash
↓
Cash Insufficient?
├── Yes → Generate RCA
└── No → Manual Investigation
↓
Generate Recommendation
↓
Risk High?
├── Yes → Human Approval
└── No → Complete
↓
END

**Interview Explanation:**

"I would create separate nodes for trade fetching, SSI validation, securities checking, cash checking, and RCA. I would store all results in state and use conditional edges to determine the next step. For high-risk cases, I would add human-in-the-loop approval."

---

# MCP

## 11. What is MCP?

**MCP stands for Model Context Protocol.**

It is an open standard that allows AI applications to connect with external tools and data sources through a common interface.

Simple Flow:

AI Application
↓
MCP Client
↓
MCP Server
↓
External System

External systems could include:

- Database
- File system
- GitHub
- Jira
- APIs
- Internal services

**Interview Answer:**

"MCP is a standardized protocol that allows AI applications to connect with external tools and data sources."

---

## 12. MCP Client and Server

### MCP Client

The **MCP client connects the AI application with an MCP server.**

Example:

AI Agent
↓
MCP Client
↓
MCP Server

### MCP Server

The **MCP server exposes capabilities that AI applications can use.**

It can expose:

- Tools
- Resources
- Prompts

Example:

Agent
↓
MCP Client
↓
Trade MCP Server
↓
Trade Database

---

## 13. MCP Tools

**Tools are functions/actions that the AI application can execute.**

Examples:

get_trade_status(trade_id)

get_cash_balance(account)

create_ticket(issue)

send_notification(message)

Simple meaning:

**Tools = Actions**

---

## 14. MCP Resources

**Resources represent data that an AI application can read/access through MCP.**

Examples:

- Documents
- Files
- Database records
- Configuration
- Knowledge

Simple meaning:

**Resources = Data**

---

## 15. MCP Prompts

**Prompts are reusable prompt templates that an MCP server can expose.**

Example:

settlement_rca_prompt

It could contain instructions for performing settlement Root Cause Analysis.

Simple meaning:

**Prompts = Reusable Instructions**

---

## 16. MCP Server Example

Suppose we create:

Trade MCP Server

It could expose:

Tools:
- get_trade()
- get_cash_balance()
- get_security_holding()
- create_ticket()

Resources:
- settlement_policy
- trade_information

Prompts:
- settlement_rca_prompt

Then an AI agent can discover and use these capabilities through MCP.

---

## 17. MCP vs API

An **API is a general mechanism for communication between software applications.**

Example:

Frontend
↓
REST API
↓
Backend

MCP is designed specifically to standardize how AI applications interact with tools and contextual data.

Example:

AI Agent
↓
MCP Server
↓
REST API
↓
Backend System

So MCP does NOT replace APIs.

An MCP server can internally call existing REST APIs.

### Difference

API
→ General software communication

MCP
→ Standardized AI-to-tool/data integration

**Interview Answer:**

"MCP doesn't replace APIs. APIs expose backend functionality, while MCP provides an AI-friendly standardized interface that can expose those APIs as tools or resources."

---

## 18. MCP vs Function Calling

These are related but different.

### Function Calling

Function calling allows the LLM to decide:

- Which tool/function to use
- What arguments to provide

Example:

User:

"Check trade ABC123."

LLM decides:

get_trade_status("ABC123")

### MCP

MCP provides a standardized mechanism through which tools and resources can be exposed to AI applications.

Simple difference:

**Function Calling**
→ LLM chooses which tool to call.

**MCP**
→ Standardizes how tools/resources are exposed and accessed.

Example:

User
↓
LLM
↓
Decides to call get_trade()
↓
Tool available through MCP
↓
MCP Server
↓
Trade System
↓
Result
↓
LLM
↓
Answer

**Interview Answer:**

"Function calling is the model capability to select a tool and generate its arguments. MCP is a protocol that standardizes how tools and resources are exposed to AI applications."

---

# LangChain + LangGraph + MCP Together

A complete architecture can look like:

User
↓
LangGraph
↓
Workflow + State + Decisions
↓
LangChain Components
├── LLM
├── Prompt
├── Retriever
└── RAG
↓
MCP Client
↓
MCP Server
├── Tools
├── Resources
└── Prompts
↓
External Systems
├── Database
├── APIs
├── Jira
└── Files
↓
Final Result

---

# Final Interview Answer

"LangChain provides building blocks for LLM applications such as prompts, models, retrievers, RAG, and tools.

LangGraph is used for orchestrating stateful multi-step workflows. It uses nodes for tasks, edges for transitions, state for shared data, conditional edges for decisions, and cycles for repeated execution.

MCP, or Model Context Protocol, provides a standardized way for AI applications to connect with external tools and data. An MCP server can expose tools, resources, and prompts that an MCP client can access.

MCP does not replace APIs or function calling. APIs provide backend functionality, function calling allows the LLM to select a tool and its arguments, while MCP standardizes how tools and resources are exposed to AI applications."

---

# Quick Revision

LangChain
→ LLM application components

LangGraph
→ Agent workflow orchestration

Chain
→ Linear workflow

Graph
→ Dynamic workflow

State
→ Shared workflow data

Node
→ Task / Function

Edge
→ Connection between nodes

Conditional Edge
→ Decision / Dynamic routing

Cycle
→ Repeat previous step

MCP
→ Model Context Protocol

MCP Client
→ Connects AI app to MCP server

MCP Server
→ Exposes capabilities

Tools
→ Actions

Resources
→ Data

Prompts
→ Reusable instructions

API
→ General software communication

Function Calling
→ LLM chooses tool + arguments

MCP
→ Standardizes how AI tools/data are exposed

---

# Easiest Way to Remember

**LangChain = Components**

**LangGraph = Workflow**

**Node = Task**

**Edge = Connection**

**State = Data**

**Conditional Edge = Decision**

**Cycle = Repeat**

**MCP = Connectivity Standard**

**Tools = Actions**

**Resources = Data**

**Prompts = Instructions**

**API = Backend Communication**

**Function Calling = LLM Chooses Tool**