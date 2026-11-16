# Specification: yes-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## Basic Setup

- [x] Read the project input (`product-requirements-document.md` and `intent.md`)
- [x] Bootstrap agent code in `assets/yes-agent/` using instructions from the sap-agent-bootstrap section (invoke from inside `assets/yes-agent/`, use copy commands — do NOT create files manually)
- [x] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

No runtime skills are needed for this agent. The response logic ("always reply Yes") is trivial and fits entirely in the system prompt.

---

## Project-Specific Tasks

### System Prompt — Always-Yes Behaviour

- [x] Open `assets/yes-agent/app/agent.py`
- [x] Set the agent system prompt (in `get_system_prompt()` or equivalent `@prompt_section`) to:
  ```
  You are a simple test agent. Reply with exactly "Yes" to every user message, regardless of its content.
  Do not add explanations, punctuation beyond the word, or any other text. Your only valid response is: Yes
  ```
- [x] Verify the system prompt is the sole driver of the response — no conditional logic, branching, or tool calls

### Response Validation

- [x] Confirm the agent returns exactly `"Yes"` (case-sensitive) for any input, including:
  - A regular question (e.g. "What is the weather today?")
  - An empty or blank message
  - A multi-line message
  - A message in a language other than English

### No External Integrations

- [x] Confirm no MCP servers, tools, or external API calls are wired to this agent
- [x] Confirm `asset.yaml` has no `requires` entries (no dependencies)
- [x] Confirm `requirements.txt` contains only the standard bootstrap dependencies

---

## Business Instrumentation

- [x] Implement structured logging and OpenTelemetry spans for all four PRD milestones:

  | Milestone | Achievement log | Miss log |
  |-----------|-----------------|----------|
  | M1 — Project Scaffolded | `M1.achieved: agent project scaffolded successfully` | `M1.missed: project scaffolding did not complete` |
  | M2 — Logic Implemented | `M2.achieved: yes-response logic implemented and verified` | `M2.missed: agent did not return expected yes response` |
  | M3 — Tests Pass | `M3.achieved: all automated tests passed` | `M3.missed: one or more tests failed` |
  | M4 — Agent Deployable | `M4.achieved: agent deployed and reachable on SAP BTP` | `M4.missed: deployment did not complete or agent is unreachable` |

- [x] Extract business logic from `stream()` into a plain async helper (e.g. `_run_agent()`) and apply `@tracer.start_as_current_span` to that helper — do NOT use a context manager inside the generator
- [x] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

No MCP integrations required. Skip the entire MCP Tool Integration section.

---

## Testing

- [x] `conftest.py` only sets `IBD_TESTING=true`
- [x] Write unit tests in `assets/yes-agent/tests/`:
  - `test_yes_response.py` — assert the agent returns `"Yes"` for a regular user message
  - `test_yes_response_empty.py` — assert the agent returns `"Yes"` for an empty message
- [x] Write one integration test (`test_integration.py`) executing the full agent flow end-to-end with a mocked LLM that returns `"Yes"`
- [x] Run `pytest` from `assets/yes-agent/` (no args) — fix any failures before proceeding
- [x] Ensure coverage ≥ 70%; add tests if needed
- [x] Run `pytest` again (no args) from `assets/yes-agent/` to generate the final `test_report.json`
- [x] Verify `test_report.json` exists in `assets/yes-agent/`
