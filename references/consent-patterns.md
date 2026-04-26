# Consent Patterns

Keep consent prompts short and specific.

## Low-Risk Preference

"I can remember that you prefer <preference> for future work. Should I save that?"

## Project Memory

"I can save this as project memory for <project>, so it applies only here. Should I do that?"

## Medium-Risk Personal Data

"This includes personal information. I can keep it session-only, save a redacted version, or not remember it. Which do you prefer?"

## High-Risk Data

"This is sensitive information. I should not store it as long-term memory. I can use it for this session only if needed."

## Secret Exposure

"That looks like a secret or credential. I will not store it. You should revoke or rotate it if it was exposed."

## Deletion Confirmation

"I removed the matching memory I can access. If it also exists in logs, backups, or external systems, those may need separate deletion."

## Redaction Examples

- Phone: `+1 *** *** 1234`
- Email: `a***@example.com`
- Address: "city-level only"
- Customer: "Customer A" or "enterprise customer"
- Contract: "pricing terms exist" rather than exact figures

## Avoid

- Do not ask broad consent like "Can I remember this?"
- Do not bury risk in long text.
- Do not imply deletion from systems you cannot control.
- Do not save a sensitive detail merely because the user pasted it.
