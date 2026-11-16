# Yes Agent

Basic test/demo AI agent that always replies "Yes".

## Business challenge

Build a minimal AI agent for testing and demonstration purposes. The agent responds "Yes" to every user message, serving as a reliable baseline to explore and validate the agent development framework.

## Business Goals & Success Criteria

| Metric | Baseline | Target | Timeline | Process / Capability | Source |
|--------|----------|--------|----------|----------------------|--------|
| Agent responds "Yes" to any input | — | 100% correct responses | — | Conversational agent reliability | user |

## Key Milestones

1. **Project scaffolded** — Agent project structure is created with all required files.
2. **Logic implemented** — Agent always returns "Yes" regardless of input.
3. **Tests pass** — Automated tests confirm the agent behaves as expected.
4. **Deployable** — Agent can be deployed and accessed via API.

## Business Architecture (RBA)

### End-to-End Process

IT Management / Platform Engineering

### Process Hierarchy

```
Governance (Corporate)
└── IT Management
    └── Platform Engineering
        └── Agent Development & Testing
            └── Build baseline agent
            └── Validate agent response behaviour
```

### Summary

This is a minimal test agent mapped to platform engineering activities within the IT Management domain. It serves as a foundation for exploring the agent development framework.

## Fit Gap Analysis

| Requirement (business) | Standard asset(s) found | API ORD ID | MCP Server ORD ID | MCP Server Version | Webhook API ORD ID | Data Product ORD ID | Gap? | Notes / assumptions |
| ---------------------- | ----------------------- | ---------- | ----------------- | ------------------ | ------------------ | ------------------- | ---- | ------------------- |
| Conversational agent that replies "Yes" | Custom Python A2A agent | — | — | — | — | — | No | No external APIs needed; logic is fully self-contained |

### Key findings

- No SAP standard product covers this use case — a custom agent is the right approach.
- No external APIs or MCP servers are required; the agent logic is trivial and self-contained.
- The A2A Python agent framework on SAP BTP is the natural fit.
- This serves as a test/demo baseline; the same scaffold can be extended into a real agent later.

## Recommendations

### Simple Yes Agent

#### Executive Summary

Minimal A2A Python agent that replies "Yes" to all inputs.

#### Recommended Solution

A pro-code Python agent built on the SAP BTP A2A protocol. The agent's system prompt instructs it to always answer "Yes", regardless of the user's message. No tools or MCP servers are connected. The project is fully scaffolded with tests and can be deployed to SAP BTP.

#### Recommended solution category

AI Agent

#### Intent fit
95%
