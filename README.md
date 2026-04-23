# SPSS Academic Workflow Skill

[English](README.en.md) | 简体中文

本仓库打包了 `spss-academic-workflow`，这是一个面向 Codex 的 Agent Skill，用于基于 SPSS 的中文实证学术研究流程。它可以帮助 agent 组织研究项目、准备数据集、设计变量和模型、运行或指导 SPSS/SPSS-MCP 分析、导出表格和中文结果段落、撰写中文 LaTeX 论文，并编译最终 PDF。

## 仓库结构

```text
spss-academic-workflow/
├── README.md
├── README.en.md
├── LICENSE
└── skills/
    └── spss-academic-workflow/
        ├── SKILL.md
        ├── LICENSE.txt
        ├── agents/
        │   └── openai.yaml
        ├── assets/
        ├── references/
        └── scripts/
```

## 功能范围

- 创建可复现的实证研究项目目录结构。
- 指导数据准备、变量设计、样本规则和模型设计。
- 运行或记录 SPSS/SPSS-MCP 分析，包括描述性统计、相关分析、回归模型、稳健性检验及相关实证检验。
- 将统计输出整理成论文可用的表格、结果说明和中文学术写作内容。
- 生成 LaTeX 源文件，并支持中文实证论文的 PDF 编译。

## 安装方式

在 Codex 中使用 skill installer，并指向 GitHub 目录 URL：

```text
$skill-installer install https://github.com/<你的账号>/spss-academic-workflow/tree/main/skills/spss-academic-workflow
```

如果安装后没有立即出现该 skill，请重启 Codex。

## 使用示例

可以显式调用：

```text
Use $spss-academic-workflow to analyze this dataset with SPSS and produce Chinese result sections, tables, LaTeX source, and a PDF.
```

也可以用自然语言描述任务：

```text
请使用 SPSS 分析这份实证数据，并写出中文论文结果部分。
```

## 包含内容

- `SKILL.md`：主要 workflow 和触发说明。
- `references/`：工作流路由、实证设计、SPSS-MCP 使用、工具选择、论文写作和 LaTeX 排版的详细参考。
- `scripts/`：辅助脚本，包括保守的项目脚手架脚本。
- `assets/`：LaTeX 论文、表格注释和结果段落模板。
- `agents/openai.yaml`：可选的 Codex UI 元数据和调用策略。

## 许可证

本仓库使用 MIT License。详见 [LICENSE](LICENSE)。打包后的 skill 内部也包含一份许可证副本：`skills/spss-academic-workflow/LICENSE.txt`。
