# LangChain + LangGraph

---

# 1. LangChain

## What is it?

**LangChain** is a framework for building applications powered by Large Language Models.

Instead of manually connecting an LLM with prompts, APIs, databases, tools, and retrieval systems, LangChain provides reusable components for building these workflows.

Common LangChain components include:

- Prompts
- Models
- Chains
- Tools
- Agents
- Retrievers
- Output parsers

Basic architecture:

```text
User Input
    ↓
Prompt
    ↓
LLM
    ↓
Output
```

For more advanced applications:

```text
User
 ↓
Agent
 ↓
LLM
 ↓
Tool Selection
 ↓
API / DB / Search
 ↓
Result
```

## Why / When is it used?

LangChain is useful when building LLM applications that require more than a simple model call.

For example:

- RAG applications
- Chatbots
- Tool calling
- AI agents
- Document Q&A
- LLM-based workflows

Instead of manually implementing all integrations, LangChain provides abstractions for them.

## Use Case

Suppose I want to build an AI system that answers questions about settlement procedures.

The flow could be:

```text
Question
   ↓
Retriever
   ↓
Relevant Documents
   ↓
Prompt
   ↓
LLM
   ↓
Answer
```

LangChain can connect these components.

## Example

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

response = llm.invoke(
    "Explain settlement failure in simple terms."
)

print(response.content)
```

## Interview Answer

"LangChain is a framework for building LLM-powered applications. It provides reusable components such as prompts, models, tools, agents, and retrievers. I would use LangChain when I need to connect an LLM with external data or capabilities, for example building a RAG system, a tool-calling agent, or an AI workflow."

## Key Points to Remember

- Framework for LLM applications.
- Provides prompts, tools, agents, retrievers, and model integrations.
- Useful for RAG and tool-calling applications.
- LangChain components can also be used inside LangGraph workflows.

---

# 2. Prompts

## What is it?

A **prompt** defines the instructions and context given to an LLM.

Instead of constructing prompt strings manually, LangChain provides prompt templates where dynamic values can be inserted.

Example:

```text
Analyze settlement failure for trade {trade_id}.

Failure reason: {failure_reason}

Return:
- root cause
- recommended action
```

Here, `trade_id` and `failure_reason` are dynamic values.

## Why / When is it used?

Prompt templates are useful when the same LLM instruction needs to be reused with different inputs.

They make prompts:

- Reusable
- Structured
- Easier to maintain
- Easier to test

## Use Case

For every settlement failure, I could use the same RCA prompt but provide different trade details.

```text
Trade 101 → Same Prompt → RCA

Trade 102 → Same Prompt → RCA

Trade 103 → Same Prompt → RCA
```

## Example

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    """
    Analyze this settlement failure.

    Trade ID: {trade_id}
    Failure Reason: {reason}

    Identify the root cause.
    """
)

formatted_prompt = prompt.invoke({
    "trade_id": "TRD101",
    "reason": "Insufficient cash"
})
```

## Interview Answer

"Prompts define the instructions and context provided to an LLM. In LangChain, I can use prompt templates to create reusable prompts with dynamic variables. For example, I can create one root-cause-analysis prompt and dynamically pass different trade IDs and settlement failure details."

## Key Points to Remember

- Prompts control model instructions and context.
- Prompt templates support dynamic variables.
- Templates improve reusability.
- Good prompts should clearly define the expected output.

---

# 3. Chains

## What is it?

A **chain** connects multiple processing components together.

The output of one component becomes the input of another.

Example:

```text
Input
  ↓
Prompt
  ↓
LLM
  ↓
Output Parser
  ↓
Structured Result
```

Modern LangChain commonly uses **LCEL — LangChain Expression Language** to compose these pipelines.

## Why / When is it used?

Chains are useful when the workflow has a predictable sequence of operations.

For example:

```text
Retrieve Documents
        ↓
Create Prompt
        ↓
Call LLM
        ↓
Parse Response
```

This is a deterministic workflow because the order is already known.

## Use Case

Settlement RCA:

```text
Trade Details
     ↓
RCA Prompt
     ↓
LLM
     ↓
Structured Root Cause
```

## Example

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "Explain the root cause of this settlement failure: {failure}"
)

llm = ChatOpenAI()

chain = prompt | llm | StrOutputParser()

result = chain.invoke({
    "failure": "Insufficient cash"
})
```

The `|` operator connects the components.

## Interview Answer

"A chain is a sequence of components where the output of one step becomes the input of the next. For example, I can create a chain consisting of a prompt, an LLM, and an output parser. Chains are useful when the execution flow is predictable and mostly sequential."

## Key Points to Remember

- Chains connect multiple components.
- Good for predictable workflows.
- LCEL uses the `|` operator for composition.
- Complex stateful workflows are better suited to LangGraph.

---

# 4. Tools

## What is it?

A **tool** is a function or external capability that an LLM-powered agent can call.

Examples:

```text
Database Tool
API Tool
Search Tool
Calculator
Jira Tool
Email Tool
```

The LLM decides that it needs a capability, while the actual tool performs the operation.

## Why / When is it used?

LLMs cannot independently access your database or internal APIs.

Tools allow the agent to interact with real systems.

## Use Case

A settlement agent could have tools such as:

```text
get_trade_details()
check_cash_balance()
check_security_position()
check_ssi()
create_jira_ticket()
send_email()
```

The agent can select the appropriate tool based on the problem.

## Example

```python
from langchain_core.tools import tool

@tool
def check_cash_balance(account_id: str) -> str:
    """Check available cash balance for an account."""

    return f"Cash balance retrieved for {account_id}"
```

This function can then be provided to an agent.

## Interview Answer

"Tools allow an LLM or agent to interact with external systems. A tool can wrap a Python function, REST API, database operation, search system, or business service. For example, my settlement agent could use tools for checking cash balances, retrieving trade information, or creating a Jira ticket."

## Key Points to Remember

- Tools provide external capabilities.
- Clearly define tool descriptions and input schemas.
- Validate tool inputs and outputs.
- Sensitive tools should have controlled permissions.

---

# 5. Agents

## What is it?

An **agent** uses an LLM to dynamically decide which actions or tools should be used to achieve a goal.

Unlike a fixed chain:

```text
Chain:

A → B → C → D
```

an agent can dynamically decide:

```text
Input
  ↓
LLM
  ↓
Which tool should I use?
  ↓
Tool
  ↓
Observe result
  ↓
Need another tool?
  ↓
Final Answer
```

## Why / When is it used?

Agents are useful when the execution path cannot always be determined beforehand.

Use them when:

- Different requests require different tools.
- Decisions depend on intermediate results.
- The workflow requires dynamic reasoning.

## Use Case

A settlement agent receives:

```text
Investigate Trade T101
```

The agent may decide:

```text
Get Trade Details
        ↓
Failure = CASH
        ↓
Check Cash Balance
        ↓
Determine Root Cause
        ↓
Create Jira Ticket
```

For another trade, it may choose a different path.

## Example

Conceptually:

```python
tools = [
    get_trade_details,
    check_cash_balance,
    check_ssi
]

agent = create_agent(
    model=llm,
    tools=tools
)

agent.invoke({
    "messages": [
        {"role": "user", "content": "Investigate trade T101"}
    ]
})
```

The exact agent API can vary by LangChain version, but the concept remains the same.

## Interview Answer

"An agent uses an LLM to dynamically decide which tools or actions should be used. Unlike a fixed chain, the execution path can change depending on intermediate results. For example, a settlement agent might first retrieve trade details and then decide whether to check cash, security positions, or settlement instructions."

## Key Points to Remember

- Agents dynamically select actions.
- Agents can call multiple tools.
- Useful for non-deterministic workflows.
- Add limits and guardrails to prevent uncontrolled execution.

---

# 6. Retrievers

## What is it?

A **retriever** finds relevant information from an external knowledge source based on a query.

Retrievers are commonly used in **RAG — Retrieval-Augmented Generation**.

Basic flow:

```text
User Question
     ↓
Retriever
     ↓
Relevant Documents
     ↓
LLM
     ↓
Answer
```

The retriever could search:

- Vector databases
- Document stores
- Search indexes
- Knowledge bases

## Why / When is it used?

LLMs may not know:

- Internal company documents
- Recent information
- Organization-specific procedures
- Private domain knowledge

Retrievers provide relevant external context before the LLM generates an answer.

## Use Case

Suppose the organization has settlement procedure documents.

A user asks:

```text
What should we do when settlement fails because of incorrect SSI?
```

Retriever:

```text
Question
   ↓
Search Knowledge Base
   ↓
Retrieve SSI Procedure
   ↓
Provide Context to LLM
   ↓
Generate Answer
```

## Example

```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

documents = retriever.invoke(
    "How should an SSI settlement failure be resolved?"
)
```

## Interview Answer

"A retriever fetches relevant information from an external knowledge source and is commonly used in RAG systems. Instead of asking the LLM to answer only from its trained knowledge, I retrieve relevant internal documents and provide them as context. This helps produce more grounded and domain-specific responses."

## Key Points to Remember

- Retriever fetches relevant context.
- Common component of RAG.
- Often backed by vector search.
- Helps reduce unsupported answers.

---

# 7. LangGraph

## What is it?

**LangGraph** is a framework for building stateful, multi-step, and agentic workflows using a graph-based architecture.

Instead of representing the application only as a sequence:

```text
A → B → C
```

LangGraph represents the workflow as:

```text
        A
        |
        B
       / \
      C   D
       \ /
        E
```

The workflow consists primarily of:

- State
- Nodes
- Edges
- Conditional routing
- Checkpoints

It can also support:

- Cycles
- Human-in-the-loop
- Persistent execution

## Why / When is it used?

LangGraph is useful for complex workflows requiring:

- Branching
- State management
- Agent loops
- Multi-agent orchestration
- Recovery
- Human approval
- Long-running workflows

## Use Case

Settlement investigation:

```text
START
  ↓
Parse Trade
  ↓
Classify Failure
  ↓
Route
 / | \
Cash SSI Security
 \ | /
  RCA
   ↓
Approval
   ↓
Action
   ↓
END
```

This workflow is naturally represented as a graph.

## Example

```python
from langgraph.graph import StateGraph

graph = StateGraph(TradeState)

graph.add_node("classify", classify_failure)
graph.add_node("cash", investigate_cash)
graph.add_node("ssi", investigate_ssi)

graph.set_entry_point("classify")

app = graph.compile()
```

## Interview Answer

"LangGraph is designed for building stateful and complex agentic workflows using nodes, edges, shared state, and conditional routing. I would use it when the workflow requires branching, loops, checkpoints, human approval, or multiple agents. For example, settlement failures can be classified and routed to different investigation nodes while maintaining the same workflow state."

## Key Points to Remember

- Graph-based workflow framework.
- Built for stateful agentic applications.
- Supports branching and cycles.
- Strong fit for multi-agent orchestration.

---

# 8. State in LangGraph

## What is it?

**State** is the shared data that moves through a LangGraph workflow.

Each node can read from the state and return updates to it.

Example:

```python
class TradeState(TypedDict):
    trade_id: str
    failure_type: str
    root_cause: str
    status: str
```

Workflow:

```text
Node A
  ↓
Update State
  ↓
Node B
  ↓
Read State
  ↓
Update State
```

## Why / When is it used?

State allows different nodes and agents to share information without losing workflow context.

## Use Case

Settlement workflow state:

```python
{
    "trade_id": "T101",
    "failure_type": "CASH",
    "root_cause": "INSUFFICIENT_CASH",
    "status": "INVESTIGATED"
}
```

The classification node may set `failure_type`.

The investigation node may set `root_cause`.

The action node may update `status`.

## Example

```python
from typing import TypedDict

class TradeState(TypedDict):
    trade_id: str
    failure_type: str
    root_cause: str


def investigate_cash(state: TradeState):

    return {
        "root_cause": "INSUFFICIENT_CASH"
    }
```

## Interview Answer

"State is the shared data structure that moves through a LangGraph workflow. Every node can read relevant state and return updates. For example, one node may classify a settlement failure, another may add the root cause, and another may update the resolution status."

## Key Points to Remember

- State is shared across nodes.
- Nodes read and update state.
- State makes workflows context-aware.
- Define state schemas clearly.

---

# 9. Nodes

## What is it?

A **node** represents a unit of work in a LangGraph workflow.

A node is generally a function that:

```text
Receives State
     ↓
Performs Task
     ↓
Returns State Update
```

A node could represent:

- LLM call
- Agent
- Tool execution
- API call
- Database operation
- Business logic

## Why / When is it used?

Nodes divide complex workflows into smaller reusable steps.

## Use Case

Settlement workflow:

```text
parse_trade
     ↓
classify_failure
     ↓
investigate_failure
     ↓
generate_rca
     ↓
take_action
```

Each step can be implemented as a separate node.

## Example

```python
def classify_failure(state):

    failure_type = detect_failure(
        state["trade_id"]
    )

    return {
        "failure_type": failure_type
    }
```

## Interview Answer

"A node is an individual processing step in a LangGraph workflow. It receives the current state, performs some operation, and returns updates to the state. A node could contain an LLM call, API call, agent, tool execution, or normal Python business logic."

## Key Points to Remember

- Node = unit of work.
- Nodes operate on state.
- Keep nodes focused on specific responsibilities.
- Nodes do not necessarily need an LLM.

---

# 10. Edges

## What is it?

**Edges** define how execution moves between nodes.

Example:

```text
Node A
   |
 Edge
   |
Node B
```

In LangGraph:

```python
graph.add_edge(
    "parse_trade",
    "classify_failure"
)
```

This means after `parse_trade`, execute `classify_failure`.

## Why / When is it used?

Edges define the workflow structure and execution order.

## Use Case

```text
Parse Trade
    ↓
Classify Failure
    ↓
Generate RCA
    ↓
Take Action
```

Edges connect these processing steps.

## Example

```python
graph.add_edge(
    "parse",
    "classify"
)

graph.add_edge(
    "generate_rca",
    "action"
)
```

## Interview Answer

"Edges define the transition between nodes in LangGraph. They determine which step executes after another step. Normal edges represent fixed transitions, while conditional edges allow the next node to be selected dynamically."

## Key Points to Remember

- Edges connect nodes.
- They define execution flow.
- Normal edges are deterministic.
- Conditional edges support dynamic routing.

---

# 11. Conditional Routing

## What is it?

Conditional routing allows LangGraph to choose the next node based on the current state.

Instead of:

```text
A → B
```

we can have:

```text
           CASH → Cash Node
          /
Classify → SSI → SSI Node
          \
           SECURITY → Security Node
```

## Why / When is it used?

Conditional routing is required when different situations need different processing paths.

## Use Case

Settlement failure:

```text
Classify Failure
      ↓
 failure_type
      ↓
 ┌────┼────────┐
Cash SSI Security
```

## Example

```python
def route_failure(state):

    return state["failure_type"]


graph.add_conditional_edges(
    "classify",
    route_failure,
    {
        "CASH": "cash_agent",
        "SSI": "ssi_agent",
        "SECURITY": "security_agent"
    }
)
```

## Interview Answer

"Conditional routing allows the next LangGraph node to be selected dynamically based on workflow state. For example, after classifying a settlement failure, I can route CASH failures to a cash investigation node, SSI failures to an SSI node, and security failures to a security node."

## Key Points to Remember

- Enables dynamic branching.
- Routing usually depends on state.
- Useful for agent orchestration.
- Deterministic routing is preferable for known business rules.

---

# 12. Checkpoints

## What is it?

A **checkpoint** saves the state of a LangGraph workflow during execution.

Conceptually:

```text
Node A
  ↓
Checkpoint
  ↓
Node B
  ↓
Checkpoint
  ↓
Node C
```

If execution is interrupted, the workflow can resume using the saved state rather than starting from zero.

## Why / When is it used?

Checkpoints are useful for:

- Long-running workflows
- Failure recovery
- Human-in-the-loop
- Persistent conversations
- Resuming interrupted workflows

## Use Case

Suppose:

```text
Trade Investigation
      ↓
RCA Generated
      ↓
CHECKPOINT
      ↓
Waiting for Human Approval
```

The workflow may wait for approval and continue later using the persisted state.

## Example

Conceptually:

```python
checkpointer = SomeCheckpointer()

app = graph.compile(
    checkpointer=checkpointer
)

app.invoke(
    input_data,
    config={
        "configurable": {
            "thread_id": "trade-T101"
        }
    }
)
```

The thread ID identifies the workflow execution.

## Interview Answer

"Checkpoints persist workflow state during LangGraph execution. They are useful for long-running workflows, failure recovery, persistent conversations, and human approval. For example, I can save the state after generating an RCA, pause for human approval, and later resume the same workflow without restarting it."

## Key Points to Remember

- Checkpoints persist state.
- Enable pause and resume.
- Important for HITL workflows.
- Useful for recovery after interruptions.

---

# 13. Cycles

## What is it?

A **cycle** allows the workflow to return to a previous node.

Traditional workflow:

```text
A → B → C → END
```

Cyclic workflow:

```text
A → B → C
    ↑     |
    └─────┘
```

Cycles are especially useful for agentic systems because an agent may need to repeatedly:

```text
Reason
 ↓
Use Tool
 ↓
Observe
 ↓
Reason Again
```

## Why / When is it used?

Cycles are useful for:

- Agent reasoning loops
- Retrying tasks
- Re-evaluating results
- Iterative refinement

## Use Case

```text
Analyze Failure
      ↓
Use Investigation Tool
      ↓
Enough Information?
   /          \
 Yes          No
  ↓            |
 RCA      Analyze Again
               |
               └───────→
```

## Example

Conceptually:

```python
def should_continue(state):

    if state["resolved"]:
        return "end"

    return "investigate_again"
```

The conditional edge can send execution back to an earlier node.

## Interview Answer

"Cycles allow LangGraph workflows to revisit previous nodes. This is useful for agentic workflows where the system may need to repeatedly reason, call tools, and observe results until a condition is satisfied. However, I would always add maximum-step or retry limits to prevent infinite loops."

## Key Points to Remember

- Cycles enable iterative workflows.
- Important for agent loops.
- Always define exit conditions.
- Add maximum iteration limits.

---

# 14. Human-in-the-Loop (HITL)

## What is it?

**Human-in-the-loop** means pausing an AI workflow so that a human can review, approve, modify, or reject an action before execution continues.

Example:

```text
AI Generates Action
       ↓
     PAUSE
       ↓
 Human Approval
    /       \
Approve    Reject
  ↓          ↓
Execute    Modify
```

## Why / When is it used?

HITL is important when AI actions have significant business impact.

Examples:

- Financial transactions
- Production changes
- Customer communication
- Compliance decisions
- High-risk actions

## Use Case

Settlement agent determines:

```text
Root Cause:
Incorrect SSI

Recommended Action:
Update settlement instructions
```

Instead of automatically changing production data:

```text
Agent Recommendation
        ↓
Human Approval
        ↓
Execute Change
```

## Example

Conceptually:

```python
if state["requires_approval"]:

    interrupt({
        "action": state["recommended_action"],
        "reason": state["root_cause"]
    })
```

After approval, execution can resume from the persisted workflow state.

## Interview Answer

"Human-in-the-loop allows an agentic workflow to pause before a critical action and wait for human approval or modification. This is important in finance because I would not allow an LLM to independently perform high-risk actions such as modifying settlement instructions. LangGraph checkpoints and interrupts can be used to pause and later resume the workflow."

## Key Points to Remember

- HITL adds human control.
- Important for high-risk actions.
- Workflow can pause and resume.
- Combine HITL with checkpoints.

---

# 15. LangChain vs LangGraph

## What is it?

LangChain and LangGraph solve related but different problems.

**LangChain** provides reusable building blocks for LLM applications.

Examples:

```text
Prompts
Models
Tools
Agents
Retrievers
Output Parsers
```

**LangGraph** provides orchestration for complex stateful and agentic workflows.

Examples:

```text
State
Nodes
Edges
Conditional Routing
Cycles
Checkpoints
HITL
```

They are not necessarily competitors.

LangChain components can be used inside LangGraph nodes.

## Why / When is it used?

Use **LangChain** when you mainly need:

- Prompt + LLM pipelines
- RAG
- Tool calling
- Simple agents
- Straightforward LLM workflows

Use **LangGraph** when you need:

- Complex agent workflows
- State management
- Branching
- Multi-agent orchestration
- Cycles
- Persistence
- Human approval

## Use Case

Simple RAG:

```text
Question
   ↓
Retriever
   ↓
Prompt
   ↓
LLM
   ↓
Answer
```

LangChain is sufficient.

Complex settlement system:

```text
                 START
                   ↓
              Parse Trade
                   ↓
            Classify Failure
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
      Cash        SSI      Security
        ↓          ↓          ↓
        └──────────┼──────────┘
                   ↓
                  RCA
                   ↓
             Human Approval
                   ↓
                 Action
                   ↓
                  END
```

LangGraph is more suitable.

## Example

LangChain:

```python
chain = prompt | llm | parser

result = chain.invoke(input)
```

LangGraph:

```python
graph = StateGraph(State)

graph.add_node("classify", classify)
graph.add_node("cash", cash_agent)
graph.add_node("ssi", ssi_agent)

graph.add_conditional_edges(
    "classify",
    route_failure
)

app = graph.compile()
```

## Interview Answer

"I see LangChain and LangGraph as complementary. LangChain provides the building blocks such as prompts, models, tools, agents, and retrievers. LangGraph provides orchestration for stateful and complex workflows using nodes, edges, conditional routing, cycles, checkpoints, and human-in-the-loop. For a simple RAG application I would use LangChain, while for a multi-agent settlement investigation workflow I would use LangGraph and potentially use LangChain components inside its nodes."

## Key Points to Remember

- LangChain = LLM application building blocks.
- LangGraph = stateful workflow orchestration.
- They can be used together.
- Choose architecture based on workflow complexity.

---

# Quick Interview Revision

| Concept | Remember This |
|---|---|
| LangChain | Building blocks for LLM applications |
| Prompt | Instructions/context given to LLM |
| Chain | Fixed sequence of components |
| Tool | External capability used by an agent |
| Agent | Dynamically decides actions/tools |
| Retriever | Fetches relevant external knowledge |
| LangGraph | Stateful graph-based agent orchestration |
| State | Shared workflow data |
| Node | Individual processing step |
| Edge | Connection between nodes |
| Conditional Edge | Dynamically chooses next node |
| Checkpoint | Saves workflow state |
| Cycle | Allows execution to revisit nodes |
| HITL | Human approval/review inside workflow |
| LangChain vs LangGraph | Components vs orchestration |

---

# Most Important Architecture to Remember

```text
                         USER / EVENT
                              |
                              v
                        LANGGRAPH
                              |
                         Shared State
                              |
                              v
                      Supervisor Node
                              |
                       Classify / Route
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
          Cash Agent       SSI Agent     Security Agent
              |               |               |
              |               |               |
         LangChain       LangChain        LangChain
           Tools            Tools            Tools
              |               |               |
              v               v               v
           APIs/DB          APIs/DB          APIs/DB
              |               |               |
              +---------------+---------------+
                              |
                              v
                         Update State
                              |
                              v
                         Generate RCA
                              |
                              v
                         CHECKPOINT
                              |
                              v
                      Human-in-the-Loop
                              |
                        Approve / Reject
                              |
                              v
                         Execute Action
                              |
                              v
                             END
```

# 60-Second Combined Interview Answer

"LangChain provides reusable components for building LLM applications, such as prompts, models, chains, tools, agents, and retrievers. For example, I can use LangChain to build a RAG pipeline or give an agent tools for querying databases and APIs.

LangGraph is useful when the workflow becomes more complex and stateful. It represents the workflow using state, nodes, and edges, and supports conditional routing, cycles, checkpoints, and human-in-the-loop.

For example, in a settlement-failure system, I could use LangGraph to maintain the trade state and route CASH, SSI, or SECURITY failures to different investigation nodes. Inside those nodes, I can use LangChain components and tools. I can then checkpoint the state before a critical action and require human approval before continuing."