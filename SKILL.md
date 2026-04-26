---
name: memory-privacy-guardian
description: Use when creating, reading, updating, exporting, auditing, or deleting AI agent memory and you need privacy, permission, sensitivity, retention, consent, scope, or redaction checks before memory is stored or reused.
metadata:
  short-description: Guard AI memory privacy and permissions
---

# Memory Privacy Guardian

Use this skill as a guard layer before an agent writes, reads, updates, exports, shares, or deletes memory. Its job is to decide whether information should be remembered, where it may be remembered, for how long, and whether user consent or redaction is required.

## Core Rule

Do not optimize for remembering more. Optimize for remembering only information that is useful, stable, appropriately scoped, consented when needed, and safe to reuse.

## Decision Flow

For every proposed memory operation:

1. **Detect**: Identify the information that may be remembered or retrieved.
2. **Classify**: Assign a sensitivity level and information type.
3. **Scope**: Choose the narrowest valid scope.
4. **Consent**: Ask before storing or using medium/high-risk information.
5. **Act**: allow, allow with redaction, ask for confirmation, keep session-only, or block.
6. **Record rationale**: When a memory is saved, include why it was saved, scope, retention, and source.

## Default Actions

| Risk | Default action |
|---|---|
| Low | Save only if useful, stable, and likely reusable. |
| Medium | Prefer project/session scope. Ask before long-term storage. Redact when possible. |
| High | Do not save by default. Ask only when there is a clear user benefit and safe storage exists. |
| Critical | Never save. Refuse storage, warn the user, and recommend rotation/revocation if secrets are exposed. |

## Scope Order

Always choose the narrowest scope that satisfies the task:

1. No memory
2. Session memory
3. Project memory
4. Skill-specific memory
5. Global memory

Global memory is only appropriate for stable, low-risk preferences or explicitly authorized cross-project facts.

## Must Block

Never store these in long-term memory:

- Passwords, API keys, private keys, tokens, recovery codes, auth cookies
- Government ID numbers, full bank card numbers, full account credentials
- Unredacted medical, legal, financial, or employment records unless the user explicitly asks for a compliant system and safe storage exists
- Inferences about sensitive traits, health, beliefs, identity, or emotional state that the user did not explicitly state
- Third-party personal data when the user has not established permission or a clear purpose

If a secret appears, say it should not be stored and recommend revoking or rotating it.

## Ask Before Saving

Ask for explicit confirmation before saving:

- Real names tied to contact details
- Phone numbers, addresses, emails, customer records
- Company confidential facts
- Contract terms, pricing, revenue, salary, financial details
- Long-term identity facts such as employer, role, family relationships
- Negative preferences that could broadly constrain future behavior

## Safe Memory Template

When saving memory, prefer this compact format:

```markdown
- fact: "<redacted or minimal memory>"
  type: "preference|project|workflow|contact|confidential|other"
  sensitivity: "low|medium|high"
  scope: "global|project|skill|session"
  retention: "until changed|project end|30 days|session"
  source: "<conversation/file/date>"
  rationale: "<why this helps future tasks>"
```

## Retrieval Guard

Before using existing memory:

- Check whether the memory is relevant to the current task.
- Check whether the current task is within the memory scope.
- Prefer newer memory when two memories conflict.
- Do not reveal memory content unless the user has permission to see it.
- If use of a memory could surprise the user, explain briefly why it is relevant.

## Deletion and Correction

When the user asks to forget, delete, correct, redact, or stop using a memory:

1. Identify all likely matching memories, including aliases or related records.
2. Delete or update the memory at the narrowest storage layer available.
3. Confirm the action in plain language.
4. If the memory may exist in logs, backups, or external tools, state that limitation.

## Audit Workflow

Use `scripts/scan_memory_risks.py` to scan memory-like files for likely secrets or personal data:

```bash
python /Users/colin/.codex/skills/memory-privacy-guardian/scripts/scan_memory_risks.py <path>
```

Read references only when needed:

- `references/sensitivity-taxonomy.md`: detailed sensitivity categories.
- `references/memory-scope-policy.md`: scope, retention, and allowed actions.
- `references/consent-patterns.md`: concise consent and refusal wording.
