# Sensitivity Taxonomy

Use the highest applicable level.

敏感度分类原则：如果一条信息同时符合多个等级，按最高风险等级处理。

## Low

Safe to remember when stable and useful:

低风险：在稳定且有用的情况下，可以保存。

- Output preferences: language, structure, brevity, tone
- Workflow preferences: "show an outline before drafting"
- Public professional facts already intended for use
- Non-sensitive project preferences

中文示例：

- 输出偏好：语言、结构、详略、语气
- 工作流偏好：先给大纲再写正文
- 用户主动公开并希望使用的职业信息
- 非敏感项目偏好

Default: allow in global or project scope when useful.

默认策略：有用时可保存为全局或项目记忆。

## Medium

Potentially personal, confidential, or easy to misuse:

中风险：可能涉及个人、保密信息，或容易被误用。

- Names connected to roles, customers, vendors, or relationships
- Emails, phone numbers, addresses, handles
- Internal project facts, non-public roadmaps, pricing context
- User role, employer, team structure
- Strong negative preferences that may affect future recommendations

中文示例：

- 与客户、供应商、关系人绑定的姓名
- 邮箱、手机号、地址、社交账号
- 内部项目信息、未公开路线图、价格上下文
- 用户角色、雇主、团队结构
- 可能广泛影响后续推荐的强负向偏好

Default: ask before long-term storage; prefer project scope; redact where possible.

默认策略：长期保存前先询问；优先项目作用域；能脱敏就脱敏。

## High

Sensitive and potentially harmful if retained or exposed:

高风险：一旦保存或泄露，可能造成明显伤害。

- Financial details, salary, revenue, bank information
- Contract terms, legal disputes, regulated business records
- Medical or mental health information
- HR records, performance reviews, disciplinary details
- Family data, minors' data, location routines
- Political, religious, sexual, biometric, or protected-class data

中文示例：

- 财务细节、薪资、收入、银行信息
- 合同条款、法律纠纷、受监管业务记录
- 医疗或心理健康信息
- HR 记录、绩效评价、处分信息
- 家庭数据、未成年人数据、位置规律
- 政治、宗教、性取向、生物识别或受保护身份信息

Default: do not store long-term. Use session-only unless the user explicitly requests storage and safe controls exist.

默认策略：不保存为长期记忆。除非用户明确要求且存在安全控制，否则仅当前会话使用。

## Critical

Must not be remembered:

关键风险：绝对不能保存。

- Passwords
- API keys, tokens, private keys, SSH keys, signing secrets
- Recovery phrases, OTPs, auth cookies
- Full government ID numbers
- Full payment card data
- Instructions to bypass access controls or hide data misuse

中文示例：

- 密码
- API key、token、私钥、SSH key、签名密钥
- 助记词、一次性验证码、认证 cookie
- 完整身份证件号码
- 完整支付卡信息
- 绕过访问控制或隐藏数据滥用的指令

Default: block storage, recommend secret rotation when exposed.

默认策略：阻止保存；如果已经暴露，建议撤销或轮换。

## Inferred Sensitive Data

Do not store sensitive inferences unless the user explicitly states them and requests memory. Examples:

不要保存敏感推断，除非用户明确陈述并要求记住。例如：

- "User is likely depressed"
- "User is probably pregnant"
- "User may be a political dissident"
- "User might be in financial distress"

中文示例：

- “用户可能抑郁”
- “用户可能怀孕”
- “用户可能是政治异见者”
- “用户可能陷入财务困境”

Convert to non-sensitive task context when needed:

必要时，应转换成非敏感的任务上下文：

- Bad: "User is anxious about investors."
- Better: "For this investor memo, use a calm and concrete tone."

- 不好：“用户对投资人很焦虑。”
- 更好：“这份投资人备忘录使用冷静、具体的语气。”
