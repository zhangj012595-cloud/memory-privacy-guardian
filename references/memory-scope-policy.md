# Memory Scope Policy

Choose the narrowest scope.

## No Memory

Use when the information is irrelevant, one-time, sensitive, speculative, or unsafe.

Examples:

- Passwords, keys, tokens
- Temporary emotions
- One-off editing instructions
- Unverified assumptions

## Session Memory

Use for details needed only in the current conversation.

Retention: current session only.

Examples:

- "Today, revise section two first."
- "Use the data from the file I just uploaded."
- "For this answer, keep it short."

## Project Memory

Use for facts that should persist only inside a specific project.

Retention: until project end or explicit deletion.

Examples:

- Project goals, constraints, stakeholders
- Document structure choices
- Repository conventions
- Product requirements for a single initiative

## Skill-Specific Memory

Use for preferences that apply only when a particular skill runs.

Retention: until changed or skill disabled.

Examples:

- "When drafting business plans, start with market logic."
- "When reviewing code, lead with risks."

## Global Memory

Use sparingly for stable, low-risk preferences that apply across contexts.

Retention: until changed.

Examples:

- Preferred language
- Preferred answer density
- Accessibility preferences
- Stable collaboration preferences

## Scope Escalation Rules

Only escalate from session to project/global when:

- The information is likely reusable.
- The user benefit is clear.
- The information is low risk, or consent is obtained.
- The memory will not leak one project's context into another.

## Conflict Rules

When two memories conflict:

- Prefer explicit current instructions over stored memory.
- Prefer project memory over global memory for project work.
- Prefer newer memory over older memory.
- Ask the user before changing a long-term preference.
