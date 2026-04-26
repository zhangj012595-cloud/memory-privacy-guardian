# Sensitivity Taxonomy

Use the highest applicable level.

## Low

Safe to remember when stable and useful:

- Output preferences: language, structure, brevity, tone
- Workflow preferences: "show an outline before drafting"
- Public professional facts already intended for use
- Non-sensitive project preferences

Default: allow in global or project scope when useful.

## Medium

Potentially personal, confidential, or easy to misuse:

- Names connected to roles, customers, vendors, or relationships
- Emails, phone numbers, addresses, handles
- Internal project facts, non-public roadmaps, pricing context
- User role, employer, team structure
- Strong negative preferences that may affect future recommendations

Default: ask before long-term storage; prefer project scope; redact where possible.

## High

Sensitive and potentially harmful if retained or exposed:

- Financial details, salary, revenue, bank information
- Contract terms, legal disputes, regulated business records
- Medical or mental health information
- HR records, performance reviews, disciplinary details
- Family data, minors' data, location routines
- Political, religious, sexual, biometric, or protected-class data

Default: do not store long-term. Use session-only unless the user explicitly requests storage and safe controls exist.

## Critical

Must not be remembered:

- Passwords
- API keys, tokens, private keys, SSH keys, signing secrets
- Recovery phrases, OTPs, auth cookies
- Full government ID numbers
- Full payment card data
- Instructions to bypass access controls or hide data misuse

Default: block storage, recommend secret rotation when exposed.

## Inferred Sensitive Data

Do not store sensitive inferences unless the user explicitly states them and requests memory. Examples:

- "User is likely depressed"
- "User is probably pregnant"
- "User may be a political dissident"
- "User might be in financial distress"

Convert to non-sensitive task context when needed:

- Bad: "User is anxious about investors."
- Better: "For this investor memo, use a calm and concrete tone."
