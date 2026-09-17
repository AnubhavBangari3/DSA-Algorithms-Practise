# Production AI / Enterprise Design

---

# 1. Human-in-the-Loop (HITL)

## What is it?

**Human-in-the-loop (HITL)** means pausing an AI or agentic workflow and requiring a human to review, approve, reject, or modify an action before execution continues.

Basic flow:

```text
AI Agent
   ↓
Analysis / Recommendation
   ↓
Is Action High Risk?
   ↓
  YES
   ↓
PAUSE
   ↓
Human Review
  /     \
Approve Reject
   ↓      ↓
Execute Modify / Stop
```

## Why / When is it used?

HITL is important when AI actions can have significant:

- Financial impact
- Compliance impact
- Customer impact
- Security impact
- Production impact

The AI can automate investigation while humans retain control over critical decisions.

## Use Case

A settlement agent identifies:

```text
Root Cause:
Incorrect SSI

Recommended Action:
Update settlement instructions
```

Instead of modifying production data automatically:

```text
Agent Recommendation
        ↓
Human Approval
        ↓
Authorized API
        ↓
Update SSI
```

## Example

```python
if action["risk_level"] == "HIGH":

    return {
        "status": "WAITING_FOR_APPROVAL",
        "action": action
    }
```

With a stateful framework such as LangGraph, the workflow can checkpoint its state, pause, and resume after approval.

## Interview Answer

"Human-in-the-loop means adding human approval or review at critical points in an AI workflow. I would allow agents to automate investigation and recommendations, but high-risk actions such as updating settlement instructions or modifying financial records should require human approval before execution."

## Key Points to Remember

- Humans remain responsible for critical decisions.
- Use HITL for high-risk actions.
- Workflow should support pause and resume.
- Record approvals in the audit trail.

---

# 2. Retries and Fallbacks

## What is it?

A **retry** means attempting an operation again after a temporary failure.

A **fallback** means switching to an alternative approach when the primary approach continues to fail.

Example:

```text
Primary API
    ↓
Failure
    ↓
Retry
    ↓
Failure
    ↓
Retry
    ↓
Still Failed
    ↓
Fallback
```

Common temporary failures include:

- API timeout
- Rate limit
- Network failure
- Temporary model failure
- Service unavailable

## Why / When is it used?

Production AI systems depend on multiple external components.

Temporary failures should not immediately crash the entire workflow.

However, retries must be limited because unlimited retries can create loops and increase cost.

## Use Case

An agent calls:

```text
Cash Balance API
```

The API times out.

```text
Attempt 1 → Timeout

Wait

Attempt 2 → Timeout

Wait Longer

Attempt 3 → Timeout

Fallback → Manual Review
```

This is commonly combined with **exponential backoff**.

## Example

```python
import time

MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):

    try:
        result = call_api()
        break

    except TimeoutError:

        if attempt == MAX_RETRIES - 1:
            result = {
                "status": "MANUAL_REVIEW"
            }

        time.sleep(2 ** attempt)
```

## Interview Answer

"I use bounded retries for temporary failures such as network errors, rate limits, or API timeouts, usually with exponential backoff. If retries continue to fail, I use a fallback such as another service, degraded functionality, or manual review. I avoid unlimited retries because they can create loops and unnecessary cost."

## Key Points to Remember

- Retry temporary failures.
- Use bounded retries.
- Exponential backoff prevents aggressive repeated calls.
- Define a fallback after retries are exhausted.

---

# 3. Agent and Tool Failure Handling

## What is it?

Agentic systems can fail at different levels.

Examples:

```text
LLM Failure
Tool Failure
API Failure
Invalid Tool Arguments
Invalid Structured Output
Agent Loop
Authentication Failure
Missing Data
Incorrect Routing
```

Failure handling defines how the system detects, isolates, and recovers from these problems.

## Why / When is it used?

Agents interact with multiple systems, so production applications must assume that individual components can fail.

A single tool failure should not necessarily crash the entire workflow.

## Use Case

```text
Settlement Agent
      ↓
Check SSI Tool
      ↓
Tool Failed
      ↓
Retry
      ↓
Still Failed
      ↓
Record Error
      ↓
Manual Review
```

Another example:

```text
Agent
 ↓
Tool A
 ↓
Result
 ↓
Agent
 ↓
Tool B
 ↓
Agent keeps repeating

Maximum Step Limit
 ↓
Stop Workflow
```

## Example

```python
MAX_AGENT_STEPS = 10

if state["step_count"] >= MAX_AGENT_STEPS:

    state["status"] = "MANUAL_REVIEW"

    state["error"] = "Maximum agent steps exceeded"
```

Tool handling:

```python
try:
    result = check_ssi(trade_id)

except ToolException as error:

    log_error(error)

    return {
        "status": "TOOL_FAILURE",
        "requires_manual_review": True
    }
```

## Interview Answer

"Agentic systems can fail because of model errors, invalid outputs, tool failures, authentication issues, or loops. I handle these using timeouts, bounded retries, structured output validation, maximum agent-step limits, error logging, fallbacks, and human escalation. Critical failures should fail safely rather than allowing the agent to continue uncontrolled."

## Key Points to Remember

- Assume tools will fail.
- Add maximum agent-step limits.
- Validate tool inputs and outputs.
- Fail safely and escalate when necessary.

---

# 4. Logging

## What is it?

**Logging** means recording important information about application execution.

For an AI system, logs may include:

```text
Request ID
Workflow ID
Agent Name
Node Name
Tool Called
Tool Latency
Model Used
Token Usage
Error
Workflow Status
Timestamp
```

Example:

```text
2026-09-18 10:01
workflow_id=WF101
agent=ssi_agent
tool=check_ssi
status=SUCCESS
latency=320ms
```

## Why / When is it used?

Logs help with:

- Debugging
- Production monitoring
- Performance analysis
- Incident investigation
- Cost tracking
- Operational support

## Use Case

A production agent suddenly starts failing.

Using logs:

```text
Workflow Started
       ↓
Classifier Success
       ↓
SSI Agent Started
       ↓
SSI API Timeout
       ↓
Retry 1
       ↓
Retry 2
       ↓
Workflow Failed
```

Developers can quickly identify the failure point.

## Example

```python
import logging

logger = logging.getLogger(__name__)

logger.info(
    "Tool executed",
    extra={
        "workflow_id": workflow_id,
        "tool": "check_ssi",
        "status": "SUCCESS"
    }
)
```

## Interview Answer

"Logging provides operational visibility into the AI workflow. I would log workflow IDs, agent and node execution, tool calls, latency, model usage, errors, retries, and final status. I would use structured logging and correlation IDs so that a complete request can be traced across services, while avoiding sensitive data in logs."

## Key Points to Remember

- Use structured logging.
- Add request/workflow correlation IDs.
- Log errors, latency, and tool execution.
- Never unnecessarily log secrets or sensitive data.

---

# 5. Audit Trail

## What is it?

An **audit trail** is a chronological business record of important decisions and actions performed during a workflow.

Logging and audit trails are related but different.

```text
Logging
→ Mainly operational/debugging information.

Audit Trail
→ Business traceability and accountability.
```

Audit trail may contain:

```text
Who initiated the request?
What agent made the recommendation?
What evidence was used?
What action was recommended?
Who approved it?
What action was executed?
When did it happen?
```

## Why / When is it used?

Audit trails are especially important in enterprise and financial applications because actions need to be traceable.

## Use Case

```text
10:00 → Settlement Failure Received

10:01 → Classified as SSI

10:02 → SSI Agent Started

10:03 → SSI Mismatch Identified

10:04 → RCA Generated

10:10 → Analyst Approved

10:11 → Jira Created

10:12 → Workflow Completed
```

## Example

```python
audit_event = {
    "workflow_id": "WF101",
    "trade_id": "T101",
    "event": "ACTION_APPROVED",
    "approved_by": "operations_user",
    "timestamp": "2026-09-18T10:10:00"
}
```

## Interview Answer

"Logging is mainly for operational monitoring and debugging, while an audit trail records business decisions and actions for traceability. In a finance agentic workflow, I would record agent decisions, evidence, tool actions, human approvals, state transitions, and final outcomes so the workflow can be reconstructed later."

## Key Points to Remember

- Logs and audit trails serve different purposes.
- Audit trails focus on accountability.
- Record human approvals and important actions.
- Audit records should be tamper-resistant and access-controlled.

---

# 6. Security and RBAC

## What is it?

**RBAC stands for Role-Based Access Control.**

RBAC determines what actions users or services can perform based on their assigned roles.

Example:

```text
Viewer
→ Read only

Operations Analyst
→ Investigate + Recommend

Approver
→ Approve actions

Administrator
→ Configure system
```

In an AI system, permissions should also control which tools an agent can execute on behalf of a user or service.

## Why / When is it used?

An AI agent should never gain more access simply because it can reason about an action.

Authorization must be enforced outside the LLM.

## Use Case

Suppose the agent wants to call:

```text
update_settlement_instruction()
```

The application checks:

```text
Does the authenticated identity have permission?

NO
↓
Reject

YES
↓
Additional Approval?
↓
Execute
```

## Example

```python
def execute_tool(user, tool):

    if tool not in user.allowed_tools:
        raise PermissionError(
            "User is not authorized"
        )

    return tool.execute()
```

## Interview Answer

"RBAC controls access based on roles and should be enforced by the application or identity layer, not by the LLM. In an agentic system, I would authenticate users and services, authorize tool calls, apply least privilege, protect secrets, validate inputs, and require additional approval for sensitive operations."

## Key Points to Remember

- RBAC = Role-Based Access Control.
- Authorization belongs outside the LLM.
- Follow least privilege.
- Protect secrets and sensitive data.

---

# 7. Testing LLM Applications

## What is it?

Testing LLM applications requires both traditional software testing and AI-specific evaluation.

Traditional testing:

```text
Unit Tests
Integration Tests
API Tests
Security Tests
Load Tests
```

LLM-specific testing:

```text
Prompt Evaluation
Retrieval Evaluation
Structured Output Validation
Hallucination / Groundedness Checks
Tool Selection Tests
Agent Path Tests
Safety Tests
```

Unlike normal functions, LLM outputs can vary, so exact string comparison is often not appropriate.

## Why / When is it used?

LLM applications can fail because of:

- Prompt changes
- Model changes
- Bad retrieval
- Invalid structured output
- Wrong tool selection
- Agent loops

Therefore, production AI requires systematic evaluation.

## Use Case

For settlement classification, create a test dataset:

```text
Input                         Expected

Insufficient cash             CASH
Incorrect SSI                 SSI
Missing securities            SECURITY
Trade details mismatch        MATCHING
```

Then evaluate model accuracy.

## Example

```python
test_cases = [
    {
        "input": "Insufficient cash",
        "expected": "CASH"
    },
    {
        "input": "Incorrect settlement instructions",
        "expected": "SSI"
    }
]

for case in test_cases:

    result = classify(case["input"])

    assert result in {
        "CASH",
        "SSI",
        "SECURITY",
        "MATCHING"
    }
```

For deterministic components, use normal exact assertions.

## Interview Answer

"I test LLM applications at multiple levels. Normal code and tools use unit and integration tests, while AI components need evaluation datasets for classification accuracy, retrieval relevance, structured output validity, groundedness, tool selection, and agent paths. I also run regression evaluations whenever prompts, models, retrieval settings, or tools change."

## Key Points to Remember

- Combine software tests with AI evaluations.
- Maintain representative evaluation datasets.
- Test retrieval and agents separately.
- Run regression evaluations after changes.

---

# 8. Code Review

## What is it?

**Code review** is the process where another developer reviews changes before they are merged into the main codebase.

For AI applications, review includes normal software concerns plus AI-specific concerns.

Review areas:

```text
Code Quality
Architecture
Error Handling
Security
Prompt Changes
Tool Permissions
RAG Changes
Model Configuration
Logging
Testing
```

## Why / When is it used?

AI systems can contain hidden risks such as:

- Overpowered tools
- Poor validation
- Prompt injection exposure
- Sensitive information in logs
- Missing retry limits
- Missing HITL

Code review helps catch these issues before deployment.

## Use Case

Developer adds:

```python
agent.add_tool(delete_transaction)
```

Reviewer should ask:

```text
Does the agent actually need this tool?

What authorization exists?

Does it require human approval?

Is the action audited?
```

## Example

Code review checklist:

```text
[ ] Inputs validated
[ ] Outputs validated
[ ] Errors handled
[ ] Tool permissions restricted
[ ] No secrets hardcoded
[ ] Tests added
[ ] Logging added
[ ] HITL added where required
```

## Interview Answer

"For AI applications, code review covers normal code quality and architecture, but I also review prompts, tool permissions, output validation, security, retrieval changes, failure handling, and human approval requirements. Any sensitive tool exposed to an agent should receive additional scrutiny."

## Key Points to Remember

- AI code still follows normal engineering practices.
- Review prompts and tool permissions.
- Check security and failure handling.
- Require tests with important changes.

---

# 9. Git and CI/CD

## What is it?

**Git** provides version control for source code.

Typical development flow:

```text
Feature Branch
      ↓
Code Changes
      ↓
Commit
      ↓
Push
      ↓
Pull Request
      ↓
Code Review
      ↓
Merge
```

**CI/CD** stands for:

```text
Continuous Integration
+
Continuous Delivery / Deployment
```

CI automatically validates code changes.

CD automates deployment through environments.

## Why / When is it used?

Production AI applications require controlled and repeatable deployment.

Changes may involve:

- Python code
- Prompts
- Agent graphs
- Tool definitions
- RAG configuration
- Infrastructure

These should be version-controlled and tested.

## Use Case

```text
Developer Push
      ↓
GitHub / Azure DevOps
      ↓
CI Pipeline
      ↓
Lint
      ↓
Unit Tests
      ↓
LLM Evaluation
      ↓
Security Scan
      ↓
Build Container
      ↓
Deploy Dev
      ↓
Integration Tests
      ↓
Approval
      ↓
Deploy Production
```

## Example

Conceptual CI:

```yaml
steps:

  - run: pip install -r requirements.txt

  - run: pytest

  - run: python run_llm_evals.py

  - run: docker build .
```

## Interview Answer

"I use Git for version control with feature branches, pull requests, and code review. In CI, I would run linting, unit tests, integration tests, security checks, and relevant LLM evaluations. CD then promotes the tested application through environments such as development, staging, and production, with approval gates where required."

## Key Points to Remember

- Git provides version control.
- CI automatically validates changes.
- CD automates controlled deployment.
- Include LLM evaluations in AI CI pipelines.

---

# 10. Azure OpenAI

## What is it?

**Azure OpenAI** provides access to OpenAI models through Microsoft's Azure platform.

Enterprise applications can use supported models for tasks such as:

```text
Chat / Generation
Reasoning
Embeddings
Structured Outputs
Tool Calling
```

The application interacts with an Azure-hosted endpoint using authenticated API requests or supported SDKs.

## Why / When is it used?

Azure OpenAI is commonly considered by organizations already using Azure because it can integrate with the broader Azure ecosystem for:

- Identity and access management
- Networking
- Monitoring
- Application hosting
- Data services
- Enterprise governance

Exact features depend on the Azure service configuration and region.

## Use Case

Finance agent:

```text
Django / FastAPI
       ↓
Azure OpenAI
       ↓
LLM Reasoning
       ↓
Agent Workflow
       ↓
Azure SQL / APIs / Internal Systems
```

## Example

Conceptually:

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version=API_VERSION
)

response = client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=[
        {
            "role": "user",
            "content": "Analyze this settlement failure."
        }
    ]
)
```

API details can vary as Azure/OpenAI SDKs evolve.

## Interview Answer

"Azure OpenAI provides OpenAI models through the Azure ecosystem. I can use it for generation, reasoning, embeddings, and tool-enabled AI applications while integrating the application with Azure identity, networking, monitoring, and other enterprise services. In a finance workflow, the application layer can call an Azure OpenAI deployment while keeping business tools and authorization controlled separately."

## Key Points to Remember

- OpenAI models accessed through Azure.
- Fits Azure-based enterprise architectures.
- Integrate with identity, networking, and monitoring.
- Keep model access separate from business authorization.

---

# 11. Azure AI Foundry

## What is it?

**Azure AI Foundry** is Microsoft's platform for building and managing enterprise AI applications and agents across the AI development lifecycle.

Conceptually, it can support activities such as:

```text
Model Selection
     ↓
AI Application / Agent Development
     ↓
Evaluation
     ↓
Safety / Governance
     ↓
Deployment / Monitoring
```

It works with Azure AI services and model offerings, including Azure OpenAI capabilities.

## Why / When is it used?

Enterprise AI development involves more than calling a model API.

Teams also need:

- Model management
- Agent/application development
- Evaluation
- Observability
- Governance
- Deployment workflows

Azure AI Foundry provides an Azure-centric environment for these activities.

## Use Case

```text
Finance Application
       ↓
Agentic Workflow
       ↓
Azure AI Foundry / Model Services
       ↓
Azure OpenAI Model
       ↓
Enterprise Tools
       ↓
ERP / DB / APIs
```

The system can then be evaluated and monitored before production rollout.

## Example

High-level architecture:

```text
Frontend
   ↓
Django / FastAPI
   ↓
Agent Orchestrator
   ↓
Azure AI Foundry / Azure AI Services
   ↓
Model
   ↓
Controlled Tools
   ↓
Enterprise Systems
```

## Interview Answer

"Azure AI Foundry provides an Azure platform for developing and managing enterprise AI applications and agents. It can support model selection, development, evaluation, safety, deployment, and monitoring. I would use the model for reasoning while keeping enterprise APIs, permissions, workflow state, and audit controls in the application architecture."

## Key Points to Remember

- Azure platform for enterprise AI development.
- Supports AI application and agent lifecycle.
- Evaluation and monitoring are important production capabilities.
- Integrates with broader Azure services.

---

# 12. MCP — Model Context Protocol

## What is it?

**MCP stands for Model Context Protocol.**

It is an open protocol for standardizing how AI applications connect to external tools and context providers.

Without a standard interface:

```text
AI App
 ├── Custom Jira Integration
 ├── Custom Database Integration
 ├── Custom GitHub Integration
 └── Custom File Integration
```

With MCP conceptually:

```text
AI Application
       ↓
    MCP Client
       ↓
Standard Protocol
       ↓
    MCP Server
       ↓
External System
```

An MCP server can expose capabilities such as:

- Tools
- Resources/context
- Prompts or reusable interaction primitives, depending on implementation

## Why / When is it used?

Without standardization, every AI application may require custom integration code for every external system.

MCP provides a common protocol for connecting AI clients to compatible servers.

## Use Case

Suppose a finance agent needs access to:

```text
Database
Jira
Internal Documents
GitHub
```

Instead of tightly coupling every integration directly into the agent, compatible MCP servers can expose these capabilities through a standardized interface.

```text
Finance Agent
     ↓
MCP Client
     ↓
+----------+----------+
|          |          |
DB MCP   Jira MCP   Docs MCP
Server   Server     Server
```

## Example

Conceptually, an MCP server might expose:

```text
Tool:
get_trade_details

Input:
trade_id

Output:
trade information
```

The AI application discovers the available capability and invokes it through the MCP interface.

MCP itself does not replace authorization or security controls.

## Interview Answer

"MCP stands for Model Context Protocol. It standardizes how AI applications connect to external tools and context providers. Instead of building a completely different integration pattern for every AI client and external system, an MCP server can expose capabilities through a common protocol. I see it as an integration layer, while authentication, authorization, validation, and business controls still need to be enforced separately."

## Key Points to Remember

- MCP = Model Context Protocol.
- Standardizes AI-to-tool/context integration.
- Uses a client-server architecture.
- MCP does not replace authentication or authorization.

---

# 13. Production Agent Architecture

## What is it?

A production AI agent should not simply be:

```text
User
 ↓
LLM
 ↓
Tool
```

Enterprise architecture should include multiple control layers:

```text
Authentication
Authorization
Input Validation
Agent Orchestration
Tool Security
Failure Handling
HITL
Logging
Audit
Monitoring
```

## Why / When is it used?

Prototype agents can work with minimal controls.

Production agents must handle:

- Real users
- Sensitive data
- System failures
- Malicious input
- Compliance requirements
- High-risk actions
- Operational support

## Use Case

Enterprise finance agent:

```text
User
 ↓
Authentication
 ↓
RBAC
 ↓
API
 ↓
Agent Workflow
 ↓
Controlled Tools
 ↓
Enterprise Systems
```

Every important action is logged and audited.

## Example

```python
def process_request(user, request):

    authenticate(user)

    authorize(user, request)

    validate(request)

    result = agent.invoke(request)

    validate_agent_output(result)

    if result.requires_approval:
        return request_human_approval(result)

    audit(result)

    return result
```

## Interview Answer

"A production agent needs much more than an LLM and tools. I would design layers for authentication, RBAC, input validation, state management, controlled tool execution, retries and fallbacks, structured output validation, human approval, logging, audit trails, monitoring, and testing. The LLM should handle reasoning, while deterministic application controls handle security and critical business rules."

## Key Points to Remember

- LLM is only one component.
- Security belongs outside the model.
- Design for failures.
- Everything important should be observable and auditable.

---

# Quick Interview Revision

| Concept | Remember This |
|---|---|
| HITL | Human approval for critical AI actions |
| Retry | Re-attempt temporary failure |
| Exponential Backoff | Increase wait between retries |
| Fallback | Alternative after primary approach fails |
| Agent Failure | Detect → retry/fallback → escalate |
| Logging | Operational/debugging information |
| Audit Trail | Business traceability/accountability |
| RBAC | Role-Based Access Control |
| Least Privilege | Give minimum required permissions |
| LLM Testing | Traditional tests + AI evaluations |
| Code Review | Review code + prompts + tools + security |
| Git | Version control |
| CI | Automatically test/validate changes |
| CD | Controlled automated deployment |
| Azure OpenAI | OpenAI models through Azure |
| Azure AI Foundry | Azure platform for enterprise AI lifecycle |
| MCP | Standard protocol for AI tool/context integration |

---

# Complete Enterprise Agentic AI Architecture

```text
                         USER / SYSTEM EVENT
                                  |
                                  v
                           AUTHENTICATION
                                  |
                                  v
                                RBAC
                                  |
                                  v
                         INPUT VALIDATION
                                  |
                                  v
                           API / BACKEND
                                  |
                                  v
                          AGENT WORKFLOW
                           (LangGraph)
                                  |
                          +-------+-------+
                          |               |
                          v               v
                        STATE         CHECKPOINT
                          |
                          v
                     SUPERVISOR AGENT
                          |
                     Route / Decide
                          |
            +-------------+-------------+
            |             |             |
            v             v             v
        Agent A         Agent B       Agent C
            |             |             |
            +-------------+-------------+
                          |
                          v
                   CONTROLLED TOOLS
                          |
                   Tool Authorization
                          |
                     Input Validation
                          |
            +-------------+-------------+
            |             |             |
            v             v             v
           ERP          Database       APIs
            |             |             |
            +-------------+-------------+
                          |
                          v
                         LLM
                 Azure OpenAI / Models
                          |
                          v
                 STRUCTURED OUTPUT
                          |
                          v
                     VALIDATION
                          |
                          v
                   Risk Evaluation
                     /          \
                   LOW          HIGH
                    |             |
                    |             v
                    |            HITL
                    |             |
                    |       Human Approval
                    |             |
                    +-------------+
                          |
                          v
                    Execute Action
                          |
            +-------------+-------------+
            |             |             |
            v             v             v
           ERP           Jira        Email/Teams
            |             |             |
            +-------------+-------------+
                          |
              +-----------+-----------+
              |                       |
              v                       v
           LOGGING                AUDIT TRAIL
              |                       |
              +-----------+-----------+
                          |
                          v
                    MONITORING
                          |
                          v
                       COMPLETE
```

---

# 60-Second Combined Interview Answer

"For a production AI system, I would treat the LLM as only one component of the architecture. The request should first pass through authentication, RBAC, and input validation before entering the agent workflow.

The agent should access only controlled and authorized tools. Tool calls should have validated inputs, timeouts, bounded retries with exponential backoff, and fallbacks for failures. I would also define maximum agent-step limits to prevent loops.

For high-risk actions, I would use human-in-the-loop approval before execution. I would maintain structured logs for debugging and monitoring, and a separate audit trail for business decisions, approvals, and actions.

I would test normal code with unit and integration tests and test AI components using evaluation datasets for retrieval quality, structured output, groundedness, tool selection, and agent paths. Git, code review, and CI/CD would control changes and deployment.

In an Azure environment, Azure OpenAI can provide model capabilities, while Azure AI Foundry can support the broader AI application lifecycle. MCP can provide a standardized integration layer between AI applications and external tools, while authentication and authorization remain separate application-level responsibilities."