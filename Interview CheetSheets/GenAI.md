# AI / GenAI Interview Notes (Resume Projects)

---

# 1. What is an LLM?

### Answer

LLM (Large Language Model) is an AI model trained on massive amounts of text to understand and generate human-like language.

### Examples

* GPT
* Gemini
* Llama
* Claude
* Mistral

### Uses

* Chatbots
* Code generation
* Content generation
* Summarization
* Question Answering
* Document Analysis

---

# 2. What is Generative AI?

### Answer

Generative AI creates new content like text, images, audio, videos, or code based on user prompts.

### Examples

* ChatGPT generates text
* Gemini generates stories
* Imagen generates images
* GitHub Copilot generates code

---

# 3. What is Prompt Engineering?

### Answer

Prompt Engineering is the process of writing clear instructions to get accurate and structured responses from an LLM.

### Example

Bad Prompt

```text id="bad1"
Write a story.
```

Good Prompt

```text id="good1"
Generate a 5-scene fantasy story for children.
Return JSON with narration, image_prompt and audio_prompt.
```

---

# 4. What is Google Gemini?

### Answer

Gemini is Google's family of Large Language Models used for text generation, reasoning, coding, summarization and multimodal AI.

### Uses in my project

* Story generation
* Structured JSON output
* Content generation

### Interview Answer

> In my Creative Storyteller project, Gemini generates structured story scenes. Each scene contains narration, image prompts, and audio prompts that are later used by image and speech models.

---

# 5. What is Azure OpenAI?

### Answer

Azure OpenAI provides OpenAI models through Microsoft's Azure cloud with enterprise security and scalability.

### Uses in my project

* Root Cause Analysis
* Recommendations
* Risk Analysis
* Settlement Investigation

### Interview Answer

> In Capital Market AI, Azure OpenAI analyzes settlement failures, identifies the root cause, assesses risk, and generates recommendations.

---

# 6. Difference between Gemini and Azure OpenAI

| Gemini                    | Azure OpenAI                       |
| ------------------------- | ---------------------------------- |
| Google AI Platform        | Microsoft Azure                    |
| Vertex AI Integration     | Azure Integration                  |
| Used for story generation | Used for enterprise workflows      |
| Supports multimodal AI    | Enterprise security and compliance |

---

# 7. What is Ollama?

### Answer

Ollama allows us to run open-source LLMs locally without calling cloud APIs.

### Models

* Llama 3
* Mistral
* Gemma
* DeepSeek
* CodeLlama
* Qwen

### Uses

* Offline AI
* No API cost
* Faster local development
* Privacy

### Interview Answer

> I used Ollama in AI Creator Studio to run Llama 3 locally, eliminating API costs while generating creator content.

---

# 8. Why did you use Ollama instead of OpenAI?

### Answer

* No API cost
* Runs locally
* Better privacy
* Works without internet
* Good for development and demos

---

# 9. What is Vertex AI?

### Answer

Vertex AI is Google Cloud's AI platform for building, deploying and managing machine learning and Generative AI applications.

### Services Used

* Gemini
* Imagen
* Text-to-Speech
* Model APIs

### Interview Answer

> I used Vertex AI to access Gemini for text generation and Imagen for image generation in my Creative Storyteller project.

---

# 10. What is Semantic Kernel?

### Answer

Semantic Kernel is Microsoft's SDK for building AI applications that combine LLMs with business logic and workflows.

### Uses

* AI orchestration
* Multi-step workflows
* Function calling
* Prompt management

### Interview Answer

> In Capital Market AI, Semantic Kernel orchestrates multiple investigation steps before sending the final context to Azure OpenAI for Root Cause Analysis.

---

# 11. What is Hugging Face?

### Answer

Hugging Face is a platform that provides thousands of pre-trained machine learning and NLP models.

### Uses

* Embedding models
* NLP models
* Computer Vision models
* Transformers

### Example

I used:

```text id="hf1"
all-MiniLM-L6-v2
```

for generating document embeddings.

---

# 12. What are Embeddings?

### Answer

Embeddings convert text into numerical vectors so that similar documents have similar vector representations.

### Uses

* Semantic Search
* RAG
* Similarity Search
* Recommendations

---

# 13. What is AI Workflow Automation?

### Answer

AI Workflow Automation combines multiple AI and business steps into one automated pipeline.

### Example

```text id="wf1"
Upload SWIFT
      ↓
Parse Message
      ↓
Validate Data
      ↓
Root Cause Analysis
      ↓
Risk Assessment
      ↓
Recommendation
      ↓
Email / Teams / Jira
```

---

# 14. What is Root Cause Analysis (RCA)?

### Answer

Root Cause Analysis identifies the actual reason behind a problem instead of only describing the symptoms.

### Example

Settlement Failure

Possible Root Causes

* Cash shortage
* SSI mismatch
* Insufficient securities
* Counterparty mismatch
* Unknown trade

### Interview Answer

> Azure OpenAI receives all investigation results and determines the most probable root cause along with recommended actions.

---

# 15. What is an Agentic Workflow?

### Answer

An Agentic Workflow is a system where AI performs multiple reasoning steps to complete a task instead of generating a single response.

### Example

```text id="agent1"
User Upload
      ↓
Parser Agent
      ↓
Validation Agent
      ↓
Investigation Agent
      ↓
AI Analysis
      ↓
Recommendation Agent
```

---

# 16. How is Agentic AI different from a normal chatbot?

| Chatbot           | Agentic AI                 |
| ----------------- | -------------------------- |
| Single response   | Multi-step workflow        |
| Answers questions | Performs tasks             |
| Limited reasoning | Planning and orchestration |
| No workflow       | Executes complete pipeline |

---

# 17. Explain your Creative Storyteller AI Flow

```text id="story1"
User Prompt
      ↓
Gemini
      ↓
Generate Story Scenes
      ↓
Imagen
      ↓
Generate Images
      ↓
Text-to-Speech
      ↓
Generate Audio
      ↓
Google Cloud Storage
      ↓
Frontend Playback
```

---

# 18. Explain your Capital Market AI Flow

```text id="cap1"
Upload SWIFT File
        ↓
Parser
        ↓
Validate Trade
        ↓
Validate SSI
        ↓
Validate Cash
        ↓
Validate Holdings
        ↓
Semantic Kernel
        ↓
Azure OpenAI
        ↓
Root Cause Analysis
        ↓
Recommendations
        ↓
Jira / Teams / Email
```

---

# 19. How do you reduce LLM hallucinations?

### Answer

* Use structured prompts
* Provide business context
* Limit output format
* Validate responses
* Use deterministic settings when needed
* Use RAG for factual data

---

# 20. What is Temperature?

### Answer

Temperature controls randomness in LLM responses.

| Temperature | Result             |
| ----------- | ------------------ |
| 0.0         | Very deterministic |
| 0.2         | Mostly consistent  |
| 0.7         | Balanced           |
| 1.0         | More creative      |

### Interview Answer

> I use lower temperature for business workflows and higher temperature for creative applications like storytelling.

---

# 21. What are Tokens?

### Answer

Tokens are small pieces of text processed by an LLM.

More tokens mean:

* Higher cost
* More processing time
* Larger context

---

# 22. What is Context Window?

### Answer

The context window is the maximum amount of text an LLM can process in one request.

---

# 23. What is JSON Mode?

### Answer

JSON Mode forces the model to return structured JSON instead of free text.

### Example

```json id="json1"
{
  "title": "Adventure",
  "scene": 1,
  "narration": "...",
  "image_prompt": "...",
  "audio_prompt": "..."
}
```

---

# 24. Why use Structured Output?

### Answer

Structured output is easier to:

* Parse
* Validate
* Store
* Send to frontend
* Chain into other services

---

# 25. How do you handle LLM API failures?

### Answer

* Retry requests
* Log errors
* Return fallback message
* Notify user
* Continue workflow when possible

---

# 26. Interview Question

### Why did you choose Gemini?

**Answer**

> Gemini provides excellent multimodal capabilities and integrates well with Vertex AI, making it suitable for generating structured stories, prompts, and creative content.

---

# 27. Interview Question

### Why did you choose Azure OpenAI?

**Answer**

> Azure OpenAI integrates well with enterprise Azure services and provides secure, scalable AI capabilities suitable for financial workflows.

---

# 28. Interview Question

### Where did you use Semantic Kernel?

**Answer**

> I used Semantic Kernel in the Capital Market AI project to orchestrate multiple validation and investigation steps before sending the consolidated context to Azure OpenAI.

---

# 29. Interview Question

### Explain Agentic Workflow in one minute.

**Answer**

> Instead of sending a single prompt to an LLM, an Agentic Workflow divides the task into multiple steps. Different agents perform parsing, validation, investigation, reasoning, and recommendation before producing the final result. This makes the workflow more reliable and structured.

---

# 30. Explain your AI projects in one minute.

**Answer**

> I have worked on multiple GenAI projects. In Creative Storyteller, I used Gemini, Imagen, and Google Text-to-Speech through Vertex AI to generate complete multimedia stories. In AI Creator Studio, I used Ollama with Llama 3 to generate creator content locally without API costs. In Capital Market AI, I used Semantic Kernel and Azure OpenAI to automate settlement failure investigations, perform Root Cause Analysis, assess risks, and generate recommendations.

---

# Quick Revision

```text id="rev1"
LLM
→ Generates text and code

Gemini
→ Story generation

Azure OpenAI
→ Enterprise AI + RCA

Ollama
→ Local LLM execution

Vertex AI
→ Google AI platform

Semantic Kernel
→ AI orchestration

Hugging Face
→ Pre-trained models

Embeddings
→ Text → Vector

Temperature
→ Controls randomness

Context Window
→ Maximum input size

Agentic Workflow
→ Multi-step AI execution

Root Cause Analysis
→ Finds actual reason

AI Workflow Automation
→ AI + Business Logic Pipeline
```
