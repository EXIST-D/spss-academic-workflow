# SPSS Academic Workflow Skill

English | [简体中文](README.zh-CN.md)

This repository packages `spss-academic-workflow`, a Codex Agent Skill for SPSS-based empirical academic research workflows. It helps an agent organize research projects, prepare datasets, design variables and models, run or guide SPSS/SPSS-MCP analyses, export tables and Chinese result paragraphs, draft Chinese LaTeX papers, and compile final PDFs.

## Repository Layout

```text
spss-academic-workflow/
├── README.md
├── README.zh-CN.md
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

## What It Does

- Creates a reproducible empirical research project structure.
- Guides data preparation, variable design, sample rules, and model design.
- Runs or documents SPSS/SPSS-MCP analyses such as descriptive statistics, correlations, regression models, robustness checks, and related empirical tests.
- Converts statistical outputs into paper-ready tables, result notes, and Chinese academic writing.
- Produces LaTeX source files and supports PDF compilation for Chinese empirical papers.

## Install

Use Codex's skill installer with the GitHub directory URL:

```text
$skill-installer install https://github.com/<your-account>/spss-academic-workflow/tree/main/skills/spss-academic-workflow
```

Restart Codex if the skill does not appear immediately.

## Usage

Invoke the skill explicitly:

```text
Use $spss-academic-workflow to analyze this dataset with SPSS and produce Chinese result sections, tables, LaTeX source, and a PDF.
```

You can also ask naturally:

```text
Use SPSS to analyze this empirical dataset and write the Chinese paper results section.
```

## Included Resources

- `SKILL.md`: the main workflow and trigger instructions.
- `references/`: detailed guidance for workflow routing, empirical design, SPSS-MCP usage, tool selection, paper writing, and LaTeX layout.
- `scripts/`: helper scripts, including a conservative project scaffolder.
- `assets/`: reusable templates for LaTeX papers, table notes, and result sections.
- `agents/openai.yaml`: optional Codex UI metadata and invocation policy.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE). The packaged skill also includes its own copy at `skills/spss-academic-workflow/LICENSE.txt`.
