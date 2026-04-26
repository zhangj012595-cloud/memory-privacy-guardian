# Consent Patterns

Keep consent prompts short and specific.

授权提示应简短、明确、具体。不要让用户在一大段解释里猜测自己同意了什么。

## Low-Risk Preference

"I can remember that you prefer <preference> for future work. Should I save that?"

中文示例："我可以记住你偏好 <preference>，以后类似任务会按这个方式处理。需要我保存吗？"

## Project Memory

"I can save this as project memory for <project>, so it applies only here. Should I do that?"

中文示例："我可以把这条信息保存为 <project> 的项目记忆，只在这个项目里使用。需要保存吗？"

## Medium-Risk Personal Data

"This includes personal information. I can keep it session-only, save a redacted version, or not remember it. Which do you prefer?"

中文示例："这包含个人信息。我可以只在当前会话使用、保存脱敏版本，或者不记住。你希望怎么处理？"

## High-Risk Data

"This is sensitive information. I should not store it as long-term memory. I can use it for this session only if needed."

中文示例："这是敏感信息，不建议保存为长期记忆。如有必要，我只能在当前会话中使用。"

## Secret Exposure

"That looks like a secret or credential. I will not store it. You should revoke or rotate it if it was exposed."

中文示例："这看起来像密钥或凭证。我不会保存它。如果它已经暴露，建议你撤销或轮换。"

## Deletion Confirmation

"I removed the matching memory I can access. If it also exists in logs, backups, or external systems, those may need separate deletion."

中文示例："我已经删除了我能访问到的相关记忆。如果它也存在于日志、备份或外部系统中，可能需要单独处理。"

## Redaction Examples

- Phone: `+1 *** *** 1234`
- Email: `a***@example.com`
- Address: "city-level only"
- Customer: "Customer A" or "enterprise customer"
- Contract: "pricing terms exist" rather than exact figures

中文脱敏示例：

- 手机号：`138****1234`
- 邮箱：`a***@example.com`
- 地址：仅保留城市或区域
- 客户：使用“客户 A”或“某企业客户”
- 合同：保存“存在价格条款”，不保存具体金额

## Avoid

- Do not ask broad consent like "Can I remember this?"
- Do not bury risk in long text.
- Do not imply deletion from systems you cannot control.
- Do not save a sensitive detail merely because the user pasted it.

避免：

- 不要笼统地问“我能记住这个吗？”
- 不要把风险说明藏在很长的文字里。
- 不要承诺删除你无法控制的系统内容。
- 不要因为用户粘贴了敏感信息，就默认可以保存。
