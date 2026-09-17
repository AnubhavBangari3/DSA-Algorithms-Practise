# Agentic AI + Multi-Agent Systems

---

# 1. AI Agent vs LLM

## What is it?

An **LLM (Large Language Model)** mainly takes input and generates an output based on its trained knowledge and provided context.

An **AI Agent** uses an LLM as its reasoning component but can also take actions using tools, maintain state, make decisions, and execute multiple steps to achieve a goal.

A simple way to remember it:

**LLM = Think/Generate**

**AI Agent = Think + Decide + Act + Observe**

An agent typically follows:

`Goal → Reason → Choose Tool/Action → Execute → Observe Result → Continue/Stop`

## Why / When is it used?

Use an LLM when the task mainly requires text generation, summarization, extraction, classification, or question answering.

Use an AI Agent when the system needs to perform actions or dynamically decide what to do next.

## Use Case

In a settlement-failure system:

An LLM can analyze settlement data and explain why a trade may have failed.

An AI Agent can:

1. Read the failed trade.
2. Analyze the reason.
3. Query settlement data.
4. Identify the responsible team.
5. Create a Jira ticket.
6. Send a notification.
7. Store the result.

## Example

```python
# LLM
response = llm.invoke("Explain why this trade failed")

# Agent
result = agent.invoke({
    "goal": "Investigate this failed trade and take corrective action"
})
```

The agent may internally decide which tools it needs.

## Interview Answer

"An LLM primarily generates responses based on the input context, whereas an AI agent uses an LLM as its reasoning engine and adds capabilities like tools, state, memory, planning, and action execution. For example, an LLM can explain why a settlement failed, while an agent can investigate the failure, query data, create a Jira ticket, notify the relevant team, and track the result."

## Key Points to Remember

- LLM generates; agent can generate and act.
- Agents use tools/APIs to interact with external systems.
- Agents can execute multi-step workflows.
- An LLM is often the reasoning component inside an agent.

---

# 2. Agentic AI

## What is it?

**Agentic AI** refers to AI systems that can work toward a goal with some level of autonomy.

Instead of requiring every step to be explicitly programmed, the system can determine what actions are required, use available tools, observe results, and decide the next step.

Typical loop:

`Goal → Plan → Act → Observe → Re-plan → Complete`

## Why / When is it used?

Agentic AI is useful when workflows involve:

- Multiple steps
- Dynamic decisions
- External tools/APIs
- Changing conditions
- Tasks where the next step depends on the previous result

It is less useful for simple deterministic workflows where normal code is sufficient.

## Use Case

Suppose a settlement transaction fails.

Instead of hardcoding every possible scenario, an agent can:

`Settlement Failure`

↓

`Analyze Failure`

↓

`Determine Category`

↓

`Choose Investigation Tool`

↓

`Find Root Cause`

↓

`Take Corrective Action`

↓

`Notify Team`

## Example

```python
while not task_completed:
    decision = agent.reason(current_state)

    result = execute_tool(decision.tool)

    current_state.update(result)

    task_completed = decision.is_complete
```

This represents the basic agentic loop.

## Interview Answer

"Agentic AI is an AI architecture where the system can pursue a goal by reasoning, planning, using tools, observing results, and dynamically deciding the next action. Unlike a fixed workflow, an agentic system can adapt its execution path based on intermediate results. I would use it for complex workflows such as investigating settlement failures where different failures may require different tools and actions."

## Key Points to Remember

- Agentic AI is goal-oriented.
- It combines reasoning with actions.
- Agents interact with tools and external systems.
- Not every workflow needs an agent; deterministic tasks are often better handled by normal code.

---

# 3. Tools in AI Agents

## What is it?

**Tools** are functions, APIs, databases, or external services that an AI agent can call to perform actions or retrieve information.

The LLM itself cannot directly interact with most external systems.

Tools provide that capability.

Examples:

- Database query
- REST API
- Search API
- Jira API
- Email service
- Calculator
- Python function
- Retrieval system

## Why / When is it used?

Tools are used when the agent needs information or capabilities outside the LLM.

For example, the LLM should not guess the current status of a transaction. It should call a database or API tool.

## Use Case

A settlement investigation agent may have:

```text
get_trade_details()
get_cash_balance()
get_security_position()
check_ssi()
create_jira_ticket()
send_notification()
```

The agent chooses the appropriate tool depending on the situation.

## Example

```python
def get_trade_details(trade_id):
    return database.get_trade(trade_id)

def create_jira_ticket(issue):
    return jira_api.create_issue(issue)
```

The tools can then be registered with an agent.

```python
tools = [
    get_trade_details,
    create_jira_ticket
]
```

## Interview Answer

"Tools allow an AI agent to interact with external systems. The LLM handles reasoning, while tools perform actual operations such as querying a database, calling an API, creating a Jira ticket, or sending an email. A key design principle is that the model should use trusted tools for factual or transactional information rather than hallucinating it."

## Key Points to Remember

- Tools connect agents with the outside world.
- Tools can be APIs, functions, databases, or services.
- Tool inputs should be validated.
- Tool permissions should follow least-privilege principles.

---

# 4. Reasoning and Planning

## What is it?

**Reasoning** is how an agent determines what action should be taken based on the current situation.

**Planning** means breaking a larger goal into smaller executable steps.

For example:

```text
Goal:
Resolve settlement failure

Plan:
1. Retrieve trade
2. Analyze failure
3. Check cash/security/SSI
4. Determine root cause
5. Take corrective action
6. Notify team
```

The agent does not necessarily need to expose its internal reasoning. What matters architecturally is that it selects appropriate actions and tracks progress.

## Why / When is it used?

Planning is useful when:

- Tasks involve multiple steps.
- Steps depend on previous results.
- Multiple tools may be required.
- The execution path cannot always be predetermined.

## Use Case

If a settlement fails, the system may first classify the failure.

If the reason is:

```text
CASH
→ Check cash balance

SECURITY
→ Check security position

SSI
→ Validate settlement instructions
```

The next action depends on the previous result.

## Example

```python
if failure_type == "CASH":
    result = check_cash_balance(trade_id)

elif failure_type == "SECURITY":
    result = check_security_position(trade_id)

elif failure_type == "SSI":
    result = check_ssi(trade_id)
```

An agent can dynamically make this selection rather than relying entirely on hardcoded branching.

## Interview Answer

"Reasoning allows an agent to decide what action should happen next, while planning breaks a larger objective into smaller steps. In a settlement investigation, the agent might first classify the failure and then choose different investigation tools for cash, security, SSI, or matching issues. The important part is that the workflow can adapt based on intermediate results."

## Key Points to Remember

- Reasoning = deciding what to do.
- Planning = breaking the goal into steps.
- Plans can change based on observations.
- Keep critical business rules deterministic where possible.

---

# 5. State and Memory

## What is it?

**State** represents information about the current execution of an agent or workflow.

Example:

```python
state = {
    "trade_id": "TRD101",
    "failure_type": "CASH",
    "investigation_status": "IN_PROGRESS",
    "root_cause": None
}
```

**Memory** stores information that can be reused beyond the immediate step or conversation.

Memory may be:

- Short-term memory
- Conversation history
- Long-term memory
- Database-backed memory
- Vector-store memory

## Why / When is it used?

Without state, the agent would lose track of what has already happened during a multi-step workflow.

Memory is useful when information needs to persist across interactions or executions.

## Use Case

During settlement investigation:

```text
Trade ID
↓
Failure Type
↓
Investigation Results
↓
Root Cause
↓
Actions Taken
↓
Final Status
```

All these values can be maintained in workflow state.

Historical resolutions can be stored separately and retrieved when relevant.

## Example

```python
state = {
    "trade_id": "T123",
    "failure_type": None,
    "root_cause": None,
    "actions": []
}

state["failure_type"] = "SSI"
state["actions"].append("Checked settlement instructions")
```

## Interview Answer

"State stores information required during the current workflow execution, such as trade ID, failure type, investigation result, and completed actions. Memory is broader and can persist information across interactions or executions. In production systems I would normally keep important workflow state in a persistent database or checkpoint store rather than relying only on the LLM context."

## Key Points to Remember

- State tracks the current workflow.
- Memory provides reusable historical context.
- Persistent state helps recovery after failures.
- Do not blindly store everything in LLM context.

---

# 6. Single-Agent vs Multi-Agent Systems

## What is it?

A **single-agent system** uses one agent to handle the overall workflow.

```text
User
 ↓
Agent
 ↓
Tools
```

A **multi-agent system** divides responsibilities among specialized agents.

```text
                 Supervisor
                     |
       -----------------------------
       |             |             |
   Cash Agent    SSI Agent    Security Agent
```

Each agent can specialize in a specific task or domain.

## Why / When is it used?

Use a single agent when:

- Workflow is relatively simple.
- Toolset is manageable.
- One agent can handle the context effectively.

Use multiple agents when:

- Domains are clearly separated.
- Different agents require different tools or instructions.
- Tasks can run independently or in parallel.
- A single agent becomes too complex.

## Use Case

Settlement investigation could contain:

```text
Supervisor Agent

├── Cash Agent
├── Security Agent
├── SSI Agent
└── Matching Agent
```

The supervisor routes the problem to the relevant specialist.

## Example

```python
if failure_type == "CASH":
    return cash_agent.invoke(state)

elif failure_type == "SSI":
    return ssi_agent.invoke(state)

elif failure_type == "SECURITY":
    return security_agent.invoke(state)
```

## Interview Answer

"A single-agent architecture is simpler and works well when one agent can manage the workflow and tools. Multi-agent architecture is useful when the problem can be divided into specialized domains. For example, in settlement investigation I could have separate cash, security, SSI, and matching agents coordinated by a supervisor. I would not use multiple agents unnecessarily because they add latency, cost, and coordination complexity."

## Key Points to Remember

- Start with a single agent when possible.
- Multi-agent systems provide specialization.
- Multiple agents increase coordination complexity.
- Use multi-agent architecture when responsibilities are clearly separable.

---

# 7. Supervisor / Orchestrator

## What is it?

A **supervisor or orchestrator** coordinates other agents.

It determines:

- Which agent should handle a task.
- What information should be passed.
- What should happen after the agent responds.
- Whether another agent is required.
- When the workflow is complete.

Architecture:

```text
                Supervisor
                    |
      -----------------------------
      |            |              |
  Cash Agent   SSI Agent   Security Agent
      |            |              |
    Tools         Tools          Tools
```

## Why / When is it used?

It is useful in multi-agent systems where multiple specialized agents need centralized coordination.

Without orchestration, agents may:

- Duplicate work.
- Call each other unnecessarily.
- Lose workflow context.
- Create loops.

## Use Case

A supervisor receives:

```text
Trade Failure: T123
```

It determines:

```text
Failure Type = CASH
```

Then routes:

```text
Supervisor → Cash Agent
```

After receiving the investigation result:

```text
Cash Agent → Supervisor → Action/Notification
```

## Example

```python
def supervisor(state):

    failure_type = classify_failure(state)

    if failure_type == "CASH":
        return cash_agent(state)

    if failure_type == "SSI":
        return ssi_agent(state)

    return manual_review(state)
```

## Interview Answer

"The supervisor or orchestrator is responsible for coordinating specialized agents. It decides which agent should handle the current task, maintains workflow control, and determines the next step after receiving the result. For example, a settlement supervisor can route cash failures to a cash agent and SSI failures to an SSI agent, then collect the result and trigger the appropriate action."

## Key Points to Remember

- Supervisor coordinates specialized agents.
- It controls workflow transitions.
- It prevents unnecessary agent-to-agent complexity.
- Orchestration can be deterministic, LLM-driven, or hybrid.

---

# 8. Agent Communication

## What is it?

Agent communication refers to how information is transferred between agents in a multi-agent system.

Agents usually communicate through structured messages or shared state rather than unrestricted natural-language conversations.

Example:

```json
{
  "trade_id": "T123",
  "failure_type": "CASH",
  "status": "INVESTIGATION_REQUIRED"
}
```

## Why / When is it used?

Agents need communication when one agent's output becomes another agent's input.

Structured communication helps maintain consistency and reduces ambiguity.

## Use Case

```text
Supervisor
    ↓
Cash Agent
    ↓
Investigation Result
    ↓
Supervisor
    ↓
Notification Agent
```

Cash Agent may return:

```json
{
  "root_cause": "INSUFFICIENT_CASH",
  "required_amount": 50000,
  "status": "FAILED"
}
```

The supervisor can use this structured output for the next action.

## Example

```python
result = cash_agent.invoke(state)

state["root_cause"] = result["root_cause"]
state["status"] = result["status"]

notification_agent.invoke(state)
```

## Interview Answer

"In a multi-agent architecture, agents need a controlled way to exchange information. I prefer structured messages or shared workflow state instead of unrestricted natural-language communication. For example, a cash investigation agent can return a structured root cause and status to the supervisor, which can then pass the required information to another agent or tool."

## Key Points to Remember

- Prefer structured communication.
- Define clear input/output schemas.
- Avoid unnecessary agent-to-agent conversations.
- Shared state can act as the communication layer.

---

# 9. Routing

## What is it?

**Routing** means deciding which agent, tool, or workflow should handle a request.

Example:

```text
Incoming Failure
      ↓
    Router
      ↓
 ┌────┼─────┬────────┐
Cash SSI Security Matching
```

Routing can be:

1. Rule-based
2. LLM-based
3. Classifier-based
4. Hybrid

## Why / When is it used?

Routing prevents every agent from processing every request.

It improves:

- Specialization
- Efficiency
- Cost
- Control

## Use Case

Settlement failure routing:

```python
if failure_type == "CASH":
    route = "cash_agent"

elif failure_type == "SECURITY":
    route = "security_agent"

elif failure_type == "SSI":
    route = "ssi_agent"

else:
    route = "manual_review"
```

For ambiguous natural-language requests, an LLM may classify the intent first.

## Example

```python
def router(state):

    routes = {
        "CASH": cash_agent,
        "SECURITY": security_agent,
        "SSI": ssi_agent,
        "MATCHING": matching_agent
    }

    agent = routes.get(
        state["failure_type"],
        manual_review
    )

    return agent.invoke(state)
```

## Interview Answer

"Routing determines which agent or tool should process a task. It can be rule-based, classifier-based, LLM-based, or hybrid. For known business categories like CASH, SECURITY, SSI, and MATCHING, I would prefer deterministic routing because it is predictable and easier to audit. LLM-based routing is more useful when the input is unstructured or ambiguous."

## Key Points to Remember

- Routing directs tasks to the correct specialist.
- Rule-based routing is predictable.
- LLM routing handles ambiguous inputs better.
- Production systems often use hybrid routing.

---

# 10. Failure Handling in Agentic Systems

## What is it?

Failure handling defines how the system responds when an agent, tool, model, API, or workflow step fails.

Common failures include:

- API timeout
- Tool failure
- Invalid LLM output
- Rate limits
- Agent loop
- Missing data
- Authentication failure
- Incorrect routing

A robust system should not simply keep retrying indefinitely.

## Why / When is it used?

Agentic systems interact with multiple external components, so failures are expected.

Failure handling makes the workflow reliable and prevents uncontrolled actions.

## Use Case

Suppose the Cash Agent calls:

```text
Cash Balance API
```

and the API times out.

The workflow could:

```text
Call API
   ↓
Timeout
   ↓
Retry
   ↓
Retry Failed
   ↓
Fallback / Manual Review
   ↓
Log Failure
   ↓
Notify Team
```

## Example

```python
MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
    try:
        result = check_cash_balance(trade_id)
        break

    except TimeoutError:
        if attempt == MAX_RETRIES - 1:
            result = {
                "status": "MANUAL_REVIEW",
                "reason": "Cash API unavailable"
            }
```

For agent loops:

```python
if state["steps"] >= MAX_STEPS:
    state["status"] = "MANUAL_REVIEW"
```

## Interview Answer

"Failure handling is very important in agentic systems because agents depend on LLMs, APIs, databases, and external tools. I would use bounded retries with backoff for temporary failures, validate tool and model outputs, define timeouts and maximum agent steps, persist workflow state, and provide fallback or human escalation for unresolved cases. This prevents infinite loops and makes the system reliable and auditable."

## Key Points to Remember

- Use bounded retries, not infinite retries.
- Add timeout and maximum-step limits.
- Validate LLM and tool outputs.
- Persist state for recovery.
- Provide human-in-the-loop escalation for critical failures.

---

# Quick Interview Revision

| Concept | Remember This |
|---|---|
| LLM | Generates/understands content |
| AI Agent | LLM + Tools + State + Actions |
| Agentic AI | Goal → Plan → Act → Observe → Adapt |
| Tools | Connect agents to APIs, DBs and external systems |
| Reasoning | Decide what action to take |
| Planning | Break a goal into executable steps |
| State | Current workflow information |
| Memory | Information retained for future context |
| Single Agent | One agent handles the workflow |
| Multi-Agent | Multiple specialized agents |
| Supervisor | Coordinates and controls agents |
| Communication | Structured information exchange between agents |
| Routing | Select the appropriate agent/tool/workflow |
| Failure Handling | Retry + Validate + Fallback + Escalate |

---

# Complete Agentic AI Flow

```text
                    User / Event
                         |
                         v
                  Supervisor Agent
                         |
                    Classification
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
         Cash Agent   SSI Agent   Security Agent
             |           |           |
             v           v           v
           Tools       Tools       Tools
             |           |           |
             +-----------+-----------+
                         |
                         v
                   Shared State
                         |
                         v
                   Root Cause
                         |
                         v
                 Corrective Action
                         |
             +-----------+-----------+
             |                       |
             v                       v
         Jira / API              Notification
             |                       |
             +-----------+-----------+
                         |
                         v
                    Audit / DB
```

**One-line architecture explanation for interview:**

"I would use a supervisor-based agentic architecture where the supervisor classifies and routes the task to specialized agents. Each agent uses controlled tools to investigate its domain, while shared state maintains workflow context. The supervisor collects the result, triggers the required action, persists the audit trail, and falls back to human review when the system cannot resolve the issue safely."