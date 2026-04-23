# SPSS Academic Workflow Skill

English | [简体中文](README.md)

This repository packages `spss-academic-workflow`, a Codex Agent Skill for SPSS-based empirical academic research workflows. It helps an agent organize research projects, prepare datasets, design variables and models, run or guide SPSS/SPSS-MCP analyses, export tables and Chinese result paragraphs, draft Chinese LaTeX papers, and compile final PDFs.

## Repository Layout

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

## What It Does

- Creates a reproducible empirical research project structure.
- Guides data preparation, variable design, sample rules, and model design.
- Runs or documents SPSS/SPSS-MCP analyses such as descriptive statistics, correlations, regression models, robustness checks, and related empirical tests.
- Converts statistical outputs into paper-ready tables, result notes, and Chinese academic writing.
- Produces LaTeX source files and supports PDF compilation for Chinese empirical papers.

## SPSS-MCP Dependency

This skill's SPSS-MCP workflow uses the MCP server from [Exekiel179/SPSS-MCP](https://github.com/Exekiel179/SPSS-MCP). SPSS-MCP translates natural-language analysis requests into SPSS syntax, runs them against the local IBM SPSS Statistics engine, and returns formatted results.

This repository does not bundle or redistribute SPSS-MCP source code. Users should install and configure SPSS-MCP separately by following its upstream documentation. SPSS-MCP is currently licensed under the MIT License, so this skill can reference it, document it, and use it as an external dependency. If SPSS-MCP source code or substantial excerpts are copied into this repository in the future, retain its copyright notice and MIT license text.

### Requirements

- Windows 10/11.
- Python 3.10 or newer.
- IBM SPSS Statistics installed locally; SPSS-MCP currently documents support for versions 20-31.
- `spss-mcp` installed and runnable from the terminal.
- An MCP-capable agent client. SPSS-MCP's auto-configuration command targets Claude Code; for Codex, configure the equivalent MCP server entry so Codex can call `spss-mcp serve --transport stdio`.
- If SPSS is not auto-detected, set `SPSS_INSTALL_PATH` as documented by SPSS-MCP. For slow startup or long analyses, configure `SPSS_STARTUP_TIMEOUT` or `SPSS_TIMEOUT`.

### Codex Compatibility Example

The upstream SPSS-MCP documentation primarily targets Claude Code; this repository targets Codex usage. Codex supports local STDIO MCP servers, so you can add a configuration like this to `~/.codex/config.toml` or a trusted project's `.codex/config.toml`:

```toml
[mcp_servers.spss]
command = "spss-mcp"
args = ["serve", "--transport", "stdio"]
startup_timeout_sec = 300
tool_timeout_sec = 300
```

If you need to set the SPSS path or longer timeouts manually, add:

```toml
[mcp_servers.spss.env]
SPSS_INSTALL_PATH = "C:\\Program Files\\IBM\\SPSS Statistics\\31"
SPSS_STARTUP_TIMEOUT = "300"
SPSS_TIMEOUT = "300"
```

Restart Codex after configuration and confirm that the `spss` server is running in Codex's MCP status view. This workflow has been tested by the project author with Codex on Windows using a local SPSS installation; other environments depend on upstream SPSS-MCP support and the local SPSS setup.

## Install

Use Codex's skill installer with the GitHub directory URL:

```text
$skill-installer install https://github.com/EXIST-D/spss-academic-workflow/tree/main/skills/spss-academic-workflow
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

## Generated Project Structure

When this skill is used on a concrete empirical project, it organizes outputs under the user-provided project root with these `01` to `08` directories:

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

- `01_source_data/`: raw data, external data, and source documentation. Raw files should stay in `raw/` and should not be overwritten or edited in place.
- `02_data_prep/`: variable mappings, cleaned interim datasets, final analysis datasets, and audit artifacts such as codebooks, missing-value checks, and descriptive summaries.
- `03_research_design/`: research questions, hypotheses, variable design, model design, and sample rules.
- `04_spss_syntax/`: SPSS syntax grouped by data cleaning, variable construction, descriptive analysis, main models, robustness checks, and appendix models.
- `05_analysis_output/`: analysis outputs, including tables, figures, result notes, run logs, and paper-ready table interfaces.
- `06_paper_draft/`: Chinese paper drafts, section files, references, table/figure inputs, the LaTeX main file, and compiled PDF output.
- `07_submission_package/`: draft, final, and archive files for submission, defense, or delivery.
- `08_project_admin/`: project administration and reproducibility notes, such as a project README, changelog, and reproducibility checklist.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE). The packaged skill also includes its own copy at `skills/spss-academic-workflow/LICENSE.txt`.
