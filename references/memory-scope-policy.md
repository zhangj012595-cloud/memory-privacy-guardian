# Memory Scope Policy

Choose the narrowest scope.

记忆作用域原则：选择能满足任务的最小作用域，避免把局部信息变成全局偏好。

## No Memory

Use when the information is irrelevant, one-time, sensitive, speculative, or unsafe.

适用场景：信息无关、一次性、敏感、推测性强，或存在安全风险。

Examples:

- Passwords, keys, tokens
- Temporary emotions
- One-off editing instructions
- Unverified assumptions

中文示例：

- 密码、密钥、token
- 临时情绪
- 一次性编辑要求
- 未经确认的推断

## Session Memory

Use for details needed only in the current conversation.

Retention: current session only.

用于只在当前对话中需要的信息。

保留周期：仅当前会话。

Examples:

- "Today, revise section two first."
- "Use the data from the file I just uploaded."
- "For this answer, keep it short."

中文示例：

- “今天先改第二部分。”
- “使用我刚上传的文件里的数据。”
- “这次回答简短一点。”

## Project Memory

Use for facts that should persist only inside a specific project.

Retention: until project end or explicit deletion.

用于只应该在某个项目内持续生效的信息。

保留周期：直到项目结束或用户明确删除。

Examples:

- Project goals, constraints, stakeholders
- Document structure choices
- Repository conventions
- Product requirements for a single initiative

中文示例：

- 项目目标、限制、相关方
- 文档结构选择
- 代码仓库规范
- 单个项目的产品需求

## Skill-Specific Memory

Use for preferences that apply only when a particular skill runs.

Retention: until changed or skill disabled.

用于只在某个 skill 被调用时才应生效的偏好。

保留周期：直到用户修改或禁用该 skill。

Examples:

- "When drafting business plans, start with market logic."
- "When reviewing code, lead with risks."

中文示例：

- “写商业计划书时，先从市场逻辑开始。”
- “做代码审查时，先列风险。”

## Global Memory

Use sparingly for stable, low-risk preferences that apply across contexts.

Retention: until changed.

谨慎使用全局记忆。它只适合稳定、低风险、跨场景适用的偏好。

保留周期：直到用户修改。

Examples:

- Preferred language
- Preferred answer density
- Accessibility preferences
- Stable collaboration preferences

中文示例：

- 首选语言
- 回答详略偏好
- 无障碍偏好
- 稳定的协作偏好

## Scope Escalation Rules

Only escalate from session to project/global when:

- The information is likely reusable.
- The user benefit is clear.
- The information is low risk, or consent is obtained.
- The memory will not leak one project's context into another.

只有满足以下条件时，才可以从会话记忆升级到项目或全局记忆：

- 信息未来确实可能复用。
- 对用户有明确价值。
- 信息低风险，或已经获得用户授权。
- 不会把一个项目的上下文泄露到另一个项目。

## Conflict Rules

When two memories conflict:

- Prefer explicit current instructions over stored memory.
- Prefer project memory over global memory for project work.
- Prefer newer memory over older memory.
- Ask the user before changing a long-term preference.

记忆冲突时：

- 当前明确指令优先于历史记忆。
- 项目任务中，项目记忆优先于全局记忆。
- 新记忆优先于旧记忆。
- 修改长期偏好前，先询问用户。
