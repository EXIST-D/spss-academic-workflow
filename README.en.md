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
- Runs or documents SPSS/SPSS-MCP analyses, including descriptive statistics, frequencies and crosstabs, correlations, mean comparisons, t-tests, ANOVA, chi-square tests, reliability analysis, factor analysis, principal component analysis, cluster analysis, linear regression, hierarchical/stepwise regression, logistic regression, nonparametric tests, and common diagnostic checks.
- Supports empirical-paper model extensions such as main-effect models, control-variable models, robustness checks, alternative-variable or alternative-sample tests, heterogeneity analysis, mechanism analysis, moderation, and mediation.
- Recommends suitable SPSS analysis routes for exploratory tasks based on variable types, research questions, and sample conditions, while recording analysis choices, sample handling, and interpretation logic.
- Converts statistical outputs into paper-ready tables, result notes, and Chinese academic writing.
- Produces LaTeX source files and supports PDF compilation for Chinese empirical papers.

## SPSS-MCP Dependency

This skill's SPSS-MCP workflow uses the MCP server from [Exekiel179/SPSS-MCP](https://github.com/Exekiel179/SPSS-MCP). SPSS-MCP translates natural-language analysis requests into SPSS syntax, runs them against the local IBM SPSS Statistics engine, and returns formatted results.

This repository does not package SPSS-MCP source code or replace its installation flow. Please install and configure the MCP server locally by following the SPSS-MCP repository first. This skill uses SPSS-MCP as an external analysis interface inside a Codex workflow for SPSS analysis, result organization, and paper writing.

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

The recommended option is to install it for Codex with the [skills.sh](https://skills.sh/) `skills` CLI:

```powershell
npx skills add EXIST-D/spss-academic-workflow --skill spss-academic-workflow --agent codex --yes --copy
```

This command has been verified on Windows. It detects `spss-academic-workflow` in this repository and installs it into the current project's `.agents/skills/spss-academic-workflow` directory.

You can also use Codex's skill installer with the GitHub directory URL:

```text
$skill-installer install https://github.com/EXIST-D/spss-academic-workflow/tree/main/skills/spss-academic-workflow
```

Restart Codex if the skill does not appear immediately.

## Usage

Invoke the skill explicitly:

```text
Use $spss-academic-workflow to analyze this dataset with SPSS and produce Chinese result sections, tables, LaTeX source, and a PDF.
```

You can also ask naturally. Here are a few simple templates:

```text
Use SPSS to analyze this empirical dataset and write the Chinese paper results section.

Review this dataset, suggest suitable SPSS analyses, and create the project structure with an initial analysis plan.

Run descriptive statistics, reliability analysis, and regression analysis for this survey dataset, then format the results as paper tables.

Use SPSS-MCP to run the main model and robustness checks, then produce Chinese result interpretation and LaTeX tables.

Organize this project into a full Chinese empirical paper draft, including data, model, results, and conclusion sections.
```

For a full request that includes the project path, data file, analysis goal, and local environment, use this template:

```text
Use $spss-academic-workflow to run a detailed <analysis topic or model type> analysis on the data file "<data file name>" under "<project root>".

Complete all work inside "<project root>".

Please choose the most complete and reasonable analysis workflow, including data loading, variable inspection, missing-value checks, descriptive statistics, correlation analysis, main model estimation, diagnostic checks, robustness or supplementary analysis, and result organization for paper writing.

Automatically choose the appropriate SPSS analysis workflow, output Chinese result interpretation, result tables, paper.tex, and a compilable PDF. In the final response, explain which tools were called, which key files were generated, and whether the PDF compiled successfully.

Use the conda environment "<conda environment name>".

The local SPSS installation directory is "<SPSS installation directory>".
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

## Author and Maintenance

This project is created and maintained by [EXIST-D](https://github.com/EXIST-D).

Feedback, bug reports, and improvement ideas are welcome through GitHub Issues. Pull requests are also welcome if you extend or improve this skill.

## License

This repository is licensed under the MIT License. See [LICENSE](LICENSE). The packaged skill also includes its own copy at `skills/spss-academic-workflow/LICENSE.txt`.
