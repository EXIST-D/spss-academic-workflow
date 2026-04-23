"""Create a reproducible SPSS academic project scaffold.

This helper is intentionally conservative: it creates missing directories and
starter files, but never deletes or overwrites user data.
"""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


DIRS = [
    "01_source_data/raw",
    "01_source_data/external",
    "01_source_data/documentation",
    "02_data_prep/mapping",
    "02_data_prep/interim",
    "02_data_prep/final",
    "02_data_prep/audit",
    "03_research_design",
    "04_spss_syntax/data_cleaning",
    "04_spss_syntax/variable_construction",
    "04_spss_syntax/descriptive",
    "04_spss_syntax/main_models",
    "04_spss_syntax/robustness",
    "04_spss_syntax/appendix_models",
    "05_analysis_output/tables",
    "05_analysis_output/figures",
    "05_analysis_output/notes",
    "05_analysis_output/logs",
    "05_analysis_output/export_for_paper",
    "06_paper_draft/sections",
    "06_paper_draft/references",
    "06_paper_draft/tables_inputs",
    "06_paper_draft/figures_inputs",
    "06_paper_draft/output",
    "07_submission_package/draft",
    "07_submission_package/final",
    "07_submission_package/archive",
    "08_project_admin",
]


RESEARCH_DESIGN_FILES = {
    "03_research_design/question.md": "# 研究问题\n\n- 主题：\n- 核心问题：\n- 识别目标：\n",
    "03_research_design/hypotheses.md": "# 研究假设\n\n- H1:\n- H2:\n- H3:\n",
    "03_research_design/variable_design.md": "# 变量设计\n\n## 因变量\n\n## 自变量\n\n## 控制变量\n\n## 变量构造规则\n",
    "03_research_design/model_design.md": "# 模型设计\n\n## 主模型\n\n## 稳健性方案\n\n## 异质性或机制方案\n",
    "03_research_design/sample_rules.md": "# 样本规则\n\n- 样本范围：\n- 删除规则：\n- 缺失处理：\n",
}


ADMIN_FILES = {
    "08_project_admin/README.md": None,
    "08_project_admin/changelog.md": "# Changelog\n\n",
    "08_project_admin/reproducibility_checklist.md": (
        "# Reproducibility Checklist\n\n"
        "- [ ] 原始数据已保存到 `01_source_data/raw/`\n"
        "- [ ] 变量映射和样本规则已写入设计文件\n"
        "- [ ] 最终分析数据已保存到 `02_data_prep/final/`\n"
        "- [ ] 结果表已按 `table_XX_<content>` 输出到 `05_analysis_output/tables/`\n"
        "- [ ] 论文接口文件已按 `paper_table_XX_<content>` 输出到 `05_analysis_output/export_for_paper/`\n"
        "- [ ] 结果说明已按 `note_XX_<content>` 输出到 `05_analysis_output/notes/`\n"
        "- [ ] 复现日志已按 `run_XX_<content>` 输出到 `05_analysis_output/logs/`\n"
        "- [ ] `06_paper_draft/paper.tex` 可编译\n"
    ),
}


def copy_raw_file(raw_file: Path, raw_dir: Path) -> Path:
    target = raw_dir / raw_file.name
    if target.exists():
        return target
    shutil.copy2(raw_file, target)
    return target


def write_text_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def render_readme(project_root: Path, copied_raw: Path | None) -> str:
    raw_line = f"`{copied_raw}`" if copied_raw else "未提供"
    created_at = datetime.now().isoformat(timespec="seconds")
    return (
        "# SPSS Academic Workflow Project\n\n"
        f"- Created at: `{created_at}`\n"
        f"- Project root: `{project_root}`\n"
        f"- Raw data copied to: {raw_line}\n\n"
        "## Structure\n\n"
        "- `01_source_data/`: 原始数据、外部数据与说明文档\n"
        "- `02_data_prep/`: 数据准备、中间数据、最终分析数据与审计文件\n"
        "- `03_research_design/`: 研究问题、假设、变量和模型设计\n"
        "- `04_spss_syntax/`: SPSS 清洗、描述统计、主模型与稳健性脚本\n"
        "- `05_analysis_output/`: 表格、图形、说明笔记、日志和论文接口\n"
        "- `06_paper_draft/`: 论文主稿、章节和编译输出\n"
        "- `07_submission_package/`: 对外提交包\n"
        "- `08_project_admin/`: 项目说明、变更记录和复现检查清单\n"
    )


def load_paper_template() -> str:
    assets_dir = Path(__file__).resolve().parents[1] / "assets"
    template = assets_dir / "paper_template.tex"
    return template.read_text(encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create SPSS academic workflow directories.")
    parser.add_argument("--project-root", required=True, help="Project root directory.")
    parser.add_argument("--raw-file", help="Optional raw data file to copy into 01_source_data/raw.")
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    project_root.mkdir(parents=True, exist_ok=True)

    for rel in DIRS:
        (project_root / rel).mkdir(parents=True, exist_ok=True)

    copied_raw = None
    if args.raw_file:
        raw_file = Path(args.raw_file).expanduser().resolve()
        if not raw_file.exists():
            raise FileNotFoundError(f"Raw file does not exist: {raw_file}")
        copied_raw = copy_raw_file(raw_file, project_root / "01_source_data" / "raw")

    for rel_path, content in RESEARCH_DESIGN_FILES.items():
        write_text_if_missing(project_root / rel_path, content)

    admin_readme = render_readme(project_root, copied_raw)
    write_text_if_missing(project_root / "08_project_admin" / "README.md", admin_readme)

    for rel_path, content in ADMIN_FILES.items():
        if content is not None:
            write_text_if_missing(project_root / rel_path, content)

    paper_path = project_root / "06_paper_draft" / "paper.tex"
    write_text_if_missing(paper_path, load_paper_template())

    print(f"Scaffold ready: {project_root}")


if __name__ == "__main__":
    main()
