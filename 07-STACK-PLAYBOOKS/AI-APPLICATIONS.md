# AI Applications

## Product and architecture

- Identify where model output changes the user experience and where deterministic logic is safer.
- Specify providers/models, data sent to them, retention/training policy, latency/cost limits, fallback behavior, and user disclosure.
- Keep provider credentials server-side. Apply authorization before retrieval and tool execution; scope tools to the minimum capability.
- Treat prompts, retrieved documents, model output, and tool arguments as untrusted. Use structured validation and explicit human confirmation for consequential actions.

## Evaluation and operations

- Build a representative evaluation set before prompt tuning; include normal, edge, adversarial, and refusal cases.
- Measure task success, factuality or groundedness where relevant, safety, latency, and spend. Compare changes against a baseline.
- Add timeouts, quotas, retries with limits, graceful degradation, and redacted observability. Avoid storing sensitive prompts by default.
- Test prompt injection, indirect instructions in retrieved content, cross-tenant retrieval, data exfiltration, unsafe tool use, and provider outage.

Candidate resources: AI SDKs, LangGraph/LlamaIndex, LiteLLM, pgvector, Promptfoo, Langfuse, OWASP GenAI guidance. These categories are not interchangeable; choose based on architecture and verify current docs and data terms.