# Memory Privacy Guardian

Memory Privacy Guardian is a Codex/agent skill that adds a privacy and permission guardrail layer around AI agent memory.

Most memory tools focus on how to remember more: ingest notes, summarize context, retrieve facts, and keep long-term knowledge. This project focuses on the missing question:

> Should this information be remembered at all?

It helps an AI agent decide what can be stored, what must stay session-only, what needs user consent, what should be redacted, and what must never be saved.

## Why This Matters

AI agent memory is becoming a core product layer. It makes assistants feel continuous, personal, and useful across sessions. But poorly governed memory can create real risks:

- Secrets and credentials may be stored accidentally.
- Personal or customer data may leak across projects.
- Old or incorrect memory may keep influencing future work.
- Users may not know what an agent remembers or why.
- Sensitive inferences may be saved without consent.

Memory Privacy Guardian treats memory as a permissioned product surface, not just a technical cache.

## What It Does

The skill provides a clear decision workflow for memory operations:

```text
Detect -> Classify -> Scope -> Consent -> Act -> Record rationale
```

It helps agents decide whether to:

- Save memory
- Save only in project scope
- Keep information session-only
- Ask the user for confirmation
- Redact before saving
- Refuse to store unsafe information
- Delete or correct existing memory
- Audit memory files for likely privacy risks

## Core Concepts

| Concept | Meaning |
|---|---|
| Sensitivity classification | Categorizes information as low, medium, high, or critical risk |
| Scope control | Chooses no memory, session, project, skill-specific, or global memory |
| Consent pattern | Defines when the user must confirm storage |
| Redaction | Stores minimal useful information instead of raw sensitive data |
| Retrieval guard | Prevents irrelevant or unauthorized memory from being reused |
| Audit script | Scans memory-like files for likely secrets or personal data |

## Install

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/<your-username>/memory-privacy-guardian.git ~/.codex/skills/memory-privacy-guardian
```

Restart or refresh Codex so the skill list reloads.

Then invoke it explicitly:

```text
Use $memory-privacy-guardian to decide whether this information should be saved as memory.
```

## Usage Examples

### Low-risk preference

User says:

```text
以后写报告时，先给我大纲，再展开正文。
```

The skill may classify this as a low-risk workflow preference and allow saving it as global or skill-specific memory.

### Project-only context

User says:

```text
这个项目是宠物殡葬商业计划书，重点是商业模式和服务流程。
```

The skill should recommend project memory, not global memory.

### Secret exposure

User says:

```text
这是我的 API key：sk-...
```

The skill should block storage and recommend rotating or revoking the exposed credential.

## Audit Existing Memory

The repo includes a lightweight scanner for likely privacy and credential risks:

```bash
python3 scripts/scan_memory_risks.py <path>
```

Example:

```bash
python3 scripts/scan_memory_risks.py ~/.codex
```

The scanner flags common patterns such as:

- API keys and token-like assignments
- Private key blocks
- Email addresses
- Phone numbers
- Bank card-like numbers
- Medical or financial keywords

It is intentionally conservative and may produce false positives. Treat results as review prompts, not final judgments.

## Project Structure

```text
memory-privacy-guardian/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── consent-patterns.md
│   ├── memory-scope-policy.md
│   └── sensitivity-taxonomy.md
└── scripts/
    └── scan_memory_risks.py
```

## Design Philosophy

Good memory is not maximum memory. Good memory is:

- Useful
- Stable
- Appropriately scoped
- Consent-aware
- Easy to correct
- Safe to forget

This skill is designed to work alongside existing memory systems. It does not replace memory storage or retrieval. It acts as the governance layer before memory is written, reused, exported, or deleted.

## Author

Created by [OneMore07](https://github.com/OneMore07).

## License

MIT
