# Memory Privacy Guardian / AI 记忆隐私守卫

Memory Privacy Guardian is a Codex/agent skill that adds a privacy and permission guardrail layer around AI agent memory.

Memory Privacy Guardian 是一个面向 Codex / AI Agent 的 skill，用来在 Agent 记忆系统外增加一层隐私、权限、作用域和授权判断。

Most memory tools focus on how to remember more. This project focuses on the missing question:

大多数 memory 工具都在解决“如何记住更多”。这个项目关注一个更容易被忽略的问题：

> Should this information be remembered at all?  
> 这条信息到底应不应该被 AI 记住？

It helps an AI agent decide what can be stored, what must stay session-only, what needs user consent, what should be redacted, and what must never be saved.

它帮助 AI Agent 判断：哪些信息可以长期保存，哪些只能在当前会话使用，哪些需要用户确认，哪些应该脱敏，哪些绝对不能被记住。

## Why This Matters / 为什么需要它

AI agent memory is becoming a core product layer. It makes assistants feel continuous, personal, and useful across sessions. But poorly governed memory can create real risks:

AI Agent 的 Memory 正在变成一个核心产品层。它让助手具备连续性、个性化和长期协作能力。但如果记忆缺少治理，也会带来真实风险：

- Secrets and credentials may be stored accidentally.  
  密钥、token、密码等凭证可能被意外保存。
- Personal or customer data may leak across projects.  
  个人信息或客户数据可能跨项目泄露。
- Old or incorrect memory may keep influencing future work.  
  过时或错误记忆可能持续影响后续任务。
- Users may not know what an agent remembers or why.  
  用户可能不知道 Agent 记住了什么、为什么记住。
- Sensitive inferences may be saved without consent.  
  敏感推断可能在未经授权的情况下被保存。

Memory Privacy Guardian treats memory as a permissioned product surface, not just a technical cache.

Memory Privacy Guardian 把 memory 当作一个需要权限、边界和治理的产品能力，而不只是技术缓存。

## What It Does / 它能做什么

The skill provides a clear decision workflow for memory operations:

这个 skill 为记忆写入、读取、更新、删除和审计提供一套清晰决策流程：

```text
Detect -> Classify -> Scope -> Consent -> Act -> Record rationale
识别 -> 分类 -> 定作用域 -> 获取授权 -> 执行动作 -> 记录原因
```

It helps agents decide whether to:

它帮助 Agent 判断是否应该：

- Save memory / 保存记忆
- Save only in project scope / 只保存为项目记忆
- Keep information session-only / 仅在当前会话中使用
- Ask the user for confirmation / 向用户请求确认
- Redact before saving / 脱敏后保存
- Refuse to store unsafe information / 拒绝保存不安全信息
- Delete or correct existing memory / 删除或修正已有记忆
- Audit memory files for likely privacy risks / 审计 memory 文件中的潜在隐私风险

## Core Concepts / 核心概念

| Concept | 中文 | Meaning |
|---|---|---|
| Sensitivity classification | 敏感度分级 | Categorizes information as low, medium, high, or critical risk |
| Scope control | 作用域控制 | Chooses no memory, session, project, skill-specific, or global memory |
| Consent pattern | 授权模式 | Defines when the user must confirm storage |
| Redaction | 脱敏 | Stores minimal useful information instead of raw sensitive data |
| Retrieval guard | 读取守卫 | Prevents irrelevant or unauthorized memory from being reused |
| Audit script | 审计脚本 | Scans memory-like files for likely secrets or personal data |

## Install / 安装

Clone this repository into your Codex skills directory:

把仓库 clone 到你的 Codex skills 目录：

```bash
git clone https://github.com/zhangj012595-cloud/memory-privacy-guardian.git ~/.codex/skills/memory-privacy-guardian
```

Restart or refresh Codex so the skill list reloads.

重启或刷新 Codex，让 skill 列表重新加载。

Then invoke it explicitly:

然后可以显式调用：

```text
Use $memory-privacy-guardian to decide whether this information should be saved as memory.
```

中文也可以这样说：

```text
使用 $memory-privacy-guardian 判断这条信息是否应该被保存为 AI 记忆。
```

## Usage Examples / 使用示例

### Low-risk preference / 低风险偏好

User says / 用户说：

```text
以后写报告时，先给我大纲，再展开正文。
```

The skill may classify this as a low-risk workflow preference and allow saving it as global or skill-specific memory.

这个 skill 可以将其识别为低风险工作流偏好，并建议保存为全局记忆或 skill 专属记忆。

### Project-only context / 只适合项目内使用的上下文

User says / 用户说：

```text
这个项目是宠物殡葬商业计划书，重点是商业模式和服务流程。
```

The skill should recommend project memory, not global memory.

这个 skill 应该建议保存为项目记忆，而不是全局记忆，避免污染其他项目。

### Secret exposure / 密钥暴露

User says / 用户说：

```text
这是我的 API key：sk-...
```

The skill should block storage and recommend rotating or revoking the exposed credential.

这个 skill 应该拒绝保存，并建议用户撤销或轮换已经暴露的凭证。

### Personal data / 个人信息

User says / 用户说：

```text
这是客户的手机号，帮我以后都记住。
```

The skill should ask for explicit consent, recommend redaction, and prefer project scope or session-only use.

这个 skill 应该要求明确授权，建议脱敏，并优先使用项目作用域或仅当前会话使用。

## Audit Existing Memory / 审计已有记忆

The repo includes a lightweight scanner for likely privacy and credential risks:

仓库内置了一个轻量扫描脚本，用来发现 memory 文件中可能存在的隐私或凭证风险：

```bash
python3 scripts/scan_memory_risks.py <path>
```

Example / 示例：

```bash
python3 scripts/scan_memory_risks.py ~/.codex
```

The scanner flags common patterns such as:

扫描器会提示以下常见风险：

- API keys and token-like assignments / API key 和 token 类内容
- Private key blocks / 私钥块
- Email addresses / 邮箱
- Phone numbers / 手机号
- Bank card-like numbers / 类银行卡号
- Medical or financial keywords / 医疗或财务关键词

It is intentionally conservative and may produce false positives. Treat results as review prompts, not final judgments.

扫描器会偏保守，因此可能出现误报。请把结果当作审查线索，而不是最终判断。

## Project Structure / 项目结构

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

## Design Philosophy / 设计理念

Good memory is not maximum memory.

好的 AI 记忆不是“记得越多越好”。

Good memory should be:

好的记忆应该是：

- Useful / 有用
- Stable / 稳定
- Appropriately scoped / 作用域合适
- Consent-aware / 尊重用户授权
- Easy to correct / 易于修正
- Safe to forget / 可以安全遗忘

This skill is designed to work alongside existing memory systems. It does not replace memory storage or retrieval. It acts as the governance layer before memory is written, reused, exported, or deleted.

这个 skill 不是用来替代已有 memory 系统的。它更像一层治理规则，放在 memory 被写入、读取、导出或删除之前，帮助 Agent 做隐私和权限判断。

## Who Should Use This / 适合谁使用

- AI agent builders / AI Agent 开发者
- Product managers working on AI memory / 正在研究 AI Memory 的产品经理
- Codex or Claude Code skill authors / Codex 或 Claude Code skill 作者
- Teams building personal assistants or internal copilots / 正在做个人助理或企业内部 Copilot 的团队
- Anyone who wants AI memory to be useful without becoming risky / 希望 AI 记忆既有用又可控的人

## Author / 作者

Created by [OneMore07](https://github.com/OneMore07).

由 [OneMore07](https://github.com/OneMore07) 创建。

## License / 许可证

MIT
