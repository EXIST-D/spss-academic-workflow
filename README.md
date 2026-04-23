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

## SPSS-MCP 依赖

本 skill 的 SPSS-MCP 工作流使用 [Exekiel179/SPSS-MCP](https://github.com/Exekiel179/SPSS-MCP) 提供的 MCP server，将自然语言分析需求转换为 SPSS syntax，并通过本机 IBM SPSS Statistics 引擎执行分析。

本仓库不内置或再分发 SPSS-MCP 源码；用户需要按 SPSS-MCP 仓库说明单独安装和配置。SPSS-MCP 当前使用 MIT License，因此可以在本 skill 中引用、说明和作为外部依赖使用。若未来把 SPSS-MCP 的源码或实质性片段复制进本仓库，请同时保留其版权声明和 MIT 许可文本。

### 环境要求

- Windows 10/11。
- Python 3.10 或更高版本。
- 本机已安装 IBM SPSS Statistics，SPSS-MCP 当前说明支持 version 20-31。
- 已安装并可在终端运行 `spss-mcp`。
- 当前 agent 客户端需要支持 MCP。SPSS-MCP 的自动配置命令面向 Claude Code；在 Codex 中使用时，请将等价 MCP server 配置接入 Codex，使其能够通过 `spss-mcp serve --transport stdio` 调用该服务。
- 如果 SPSS 不能被自动检测，请按 SPSS-MCP 文档设置 `SPSS_INSTALL_PATH`；如启动或分析较慢，可设置 `SPSS_STARTUP_TIMEOUT` 或 `SPSS_TIMEOUT`。

### Codex 兼容配置示例

SPSS-MCP 上游文档主要面向 Claude Code；本仓库面向 Codex 使用场景。Codex 支持本地 STDIO MCP server，可在 `~/.codex/config.toml` 或受信任项目的 `.codex/config.toml` 中加入类似配置：

```toml
[mcp_servers.spss]
command = "spss-mcp"
args = ["serve", "--transport", "stdio"]
startup_timeout_sec = 300
tool_timeout_sec = 300
```

如果需要手动指定 SPSS 路径或超时时间，可加入：

```toml
[mcp_servers.spss.env]
SPSS_INSTALL_PATH = "C:\\Program Files\\IBM\\SPSS Statistics\\31"
SPSS_STARTUP_TIMEOUT = "300"
SPSS_TIMEOUT = "300"
```

配置后重启 Codex，并在 Codex 的 MCP 状态界面确认 `spss` server 已启动。本项目作者已在 Codex + Windows + 本机 SPSS 环境下测试该工作流；其他环境请以 SPSS-MCP 上游支持范围和本机 SPSS 安装情况为准。

## 安装方式

在 Codex 中使用 skill installer，并指向 GitHub 目录 URL：

```text
$skill-installer install https://github.com/EXIST-D/spss-academic-workflow/tree/main/skills/spss-academic-workflow
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

## 生成项目目录

使用本 skill 处理具体实证项目时，默认会在用户指定的项目根目录下组织以下 `01` 到 `08` 目录：

```text
project-name/
├── 01_source_data/
├── 02_data_prep/
├── 03_research_design/
├── 04_spss_syntax/
├── 05_analysis_output/
├── 06_paper_draft/
├── 07_submission_package/
└── 08_project_admin/
```

- `01_source_data/`：保存原始数据、外部数据和数据来源说明；原始数据应保留在 `raw/`，不覆盖、不原地修改。
- `02_data_prep/`：保存变量映射、清洗中间数据、最终分析数据和数据审计文件，例如 codebook、缺失值检查和描述统计摘要。
- `03_research_design/`：保存研究问题、研究假设、变量设计、模型设计和样本规则。
- `04_spss_syntax/`：保存 SPSS syntax，按数据清洗、变量构造、描述统计、主模型、稳健性和附录模型分组。
- `05_analysis_output/`：保存分析输出，包括表格、图形、结果说明、运行日志和论文可直接引用的表格接口。
- `06_paper_draft/`：保存中文论文草稿、章节文件、参考文献、表格/图形输入文件、LaTeX 主稿和编译输出 PDF。
- `07_submission_package/`：保存投稿、答辩或交付所需的草稿、最终版和归档文件。
- `08_project_admin/`：保存项目管理和复现说明，例如项目 README、changelog 和 reproducibility checklist。

## 许可证

本仓库使用 MIT License。详见 [LICENSE](LICENSE)。打包后的 skill 内部也包含一份许可证副本：`skills/spss-academic-workflow/LICENSE.txt`。
