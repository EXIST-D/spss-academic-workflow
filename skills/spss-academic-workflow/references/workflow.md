# SPSS Academic Workflow：项目流程

## 目录结构

在用户指定的项目根目录下创建并维护以下结构：

```text
project-name/
├── 01_source_data/
│   ├── raw/
│   ├── external/
│   └── documentation/
├── 02_data_prep/
│   ├── mapping/
│   ├── interim/
│   ├── final/
│   └── audit/
├── 03_research_design/
│   ├── question.md
│   ├── hypotheses.md
│   ├── variable_design.md
│   ├── model_design.md
│   └── sample_rules.md
├── 04_spss_syntax/
│   ├── data_cleaning/
│   ├── variable_construction/
│   ├── descriptive/
│   ├── main_models/
│   ├── robustness/
│   └── appendix_models/
├── 05_analysis_output/
│   ├── tables/
│   ├── figures/
│   ├── notes/
│   ├── logs/
│   └── export_for_paper/
├── 06_paper_draft/
│   ├── sections/
│   ├── references/
│   ├── tables_inputs/
│   ├── figures_inputs/
│   └── paper.tex
├── 07_submission_package/
│   ├── draft/
│   ├── final/
│   └── archive/
└── 08_project_admin/
    ├── README.md
    ├── changelog.md
    └── reproducibility_checklist.md
```

## 各层分工

- `01_source_data/raw`：原始数据副本，只读，不覆盖。
- `01_source_data/external`：外部补充数据，如地区宏观数据、学校层面数据、政策表。
- `01_source_data/documentation`：问卷说明、变量字典、来源记录、数据许可说明。
- `02_data_prep/mapping`：变量映射、编码转换、中文题项到英文变量名的对应表。
- `02_data_prep/interim`：清洗中的中间数据。
- `02_data_prep/final`：正式进入 SPSS 分析的最终数据，优先使用英文变量名的 `.sav`。
- `02_data_prep/audit`：codebook、描述统计、缺失处理说明、样本筛选说明。
- `03_research_design`：研究问题、假设、变量设计、模型设计、样本口径。
- `04_spss_syntax`：SPSS 语法或与 SPSS-MCP 配套的执行脚本，按用途分层保存。
- `05_analysis_output/tables`：原始分析表格输出，包含 `.md`、`.tex` 等。
- `05_analysis_output/figures`：图形与可视化输出。
- `05_analysis_output/notes`：结果摘要、中文解释、模型说明。
- `05_analysis_output/logs`：复现日志、环境记录、调用工具记录。
- `05_analysis_output/export_for_paper`：专门供论文主稿消费的 `.tex` 片段、图注包装文件或摘要接口。
- `06_paper_draft/sections`：论文分章节草稿。
- `06_paper_draft/references`：`.bib` 或稿件内参考文献资源。
- `06_paper_draft/tables_inputs`：仅在稿件需要本地适配时放置稿件侧表格输入。
- `06_paper_draft/figures_inputs`：仅在稿件需要本地适配时放置稿件侧图形输入。
- `06_paper_draft/paper.tex`：主稿入口。
- `07_submission_package`：对外投递包。
- `08_project_admin`：项目说明、变更记录、复现检查清单。

## 数据阶段

- 所有“用户要求全部在项目目录内完成”的任务，都应先把外部原始数据复制到 `01_source_data/raw/` 再处理。
- 原始数据一律不原地改写。
- `02_data_prep/final/` 中的最终分析数据是进入 SPSS 的真源。
- 如有多个版本，命名上体现日期、样本口径或变量口径差异。

推荐命名：

```text
02_data_prep/final/cfps2020_children_analysis_final.sav
02_data_prep/mapping/variable_map_cfps2020_children.csv
02_data_prep/audit/codebook_cfps2020_children.md
02_data_prep/audit/desc_cfps2020_children.csv
02_data_prep/audit/sample_flow_cfps2020_children.md
```

## 研究设计阶段

`03_research_design/` 不是摆设，而是实证分析的前置约束层：

- `question.md`：研究主题和研究问题
- `hypotheses.md`：研究假设或经验预期
- `variable_design.md`：因变量、自变量、控制变量、构造方式
- `model_design.md`：主模型、扩展模型、稳健性方案
- `sample_rules.md`：样本筛选和删失规则

如果用户已经直接给出这些信息，仍建议在此目录落一份简短说明，避免后续写作和分析脱节。

## SPSS 执行阶段

清洗和分析逻辑统一放入 `04_spss_syntax/`：

```text
04_spss_syntax/data_cleaning/
04_spss_syntax/variable_construction/
04_spss_syntax/descriptive/
04_spss_syntax/main_models/
04_spss_syntax/robustness/
04_spss_syntax/appendix_models/
```

命名建议：

```text
04_spss_syntax/data_cleaning/clean_01_import_raw.py
04_spss_syntax/variable_construction/clean_02_construct_variables.py
04_spss_syntax/descriptive/desc_01_sample_profile.py
04_spss_syntax/main_models/model_01_baseline_ols.py
04_spss_syntax/main_models/model_02_controls_extended.py
04_spss_syntax/robustness/robust_01_alt_depvar.py
04_spss_syntax/appendix_models/appendix_01_full_controls.py
```

## 命名规范

全流程默认使用小写 `snake_case`，优先 ASCII 文件名，避免中文文件名、空格、驼峰命名和含义不清的临时编号。文件名应体现“阶段、顺序、内容”，而不是单纯复用脚本名。

统一规则：

- 数据文件：`<source>_<population>_<purpose>_<stage>.<ext>`
- 映射文件：`variable_map_<study_slug>.csv`
- 审计文件：`codebook_<study_slug>.md`、`desc_<study_slug>.csv`、`sample_flow_<study_slug>.md`
- 清洗脚本：`clean_01_import_raw.py`、`clean_02_construct_variables.py`
- 描述脚本：`desc_01_sample_profile.py`
- 主模型脚本：`model_01_baseline_ols.py`
- 稳健性脚本：`robust_01_alt_depvar.py`
- 附录脚本：`appendix_01_full_controls.py`
- 结果表：`table_01_descriptive_statistics.tex`
- 论文表接口：`paper_table_01_descriptive_statistics.tex`
- 结果说明：`note_01_data_profile.md`
- 复现日志：`run_01_data_profile.md`

编号规则：

- `01`、`02`、`03` 表示论文展示顺序或分析流程顺序。
- 同一类结果编号一旦进入论文主线，不因重新运行脚本而改变。
- 新增补充结果时追加编号，不重排已有正式结果，除非用户明确要求整体重排。
- 探索性临时文件如必须保留，应放入对应阶段目录并使用 `explore_` 前缀。

## 结果阶段

分析输出统一进入 `05_analysis_output/`：

```text
05_analysis_output/tables/table_01_descriptive_statistics.md
05_analysis_output/tables/table_01_descriptive_statistics.tex
05_analysis_output/tables/table_02_correlation_matrix.md
05_analysis_output/tables/table_02_correlation_matrix.tex
05_analysis_output/tables/table_03_baseline_model.md
05_analysis_output/tables/table_03_baseline_model.tex
05_analysis_output/notes/note_03_baseline_model.md
05_analysis_output/logs/run_03_baseline_model.md
05_analysis_output/export_for_paper/paper_table_03_baseline_model.tex
```

分工原则：

- `tables/`：分析程序直接导出的原始表
- `notes/`：为论文服务的结果解释与摘要
- `logs/`：为复现服务的环境和运行记录
- `export_for_paper/`：为 LaTeX 主稿服务的稳定接口

## 论文阶段

论文主稿统一进入 `06_paper_draft/`：

- `paper.tex`：稿件主入口
- `sections/`：分章节内容
- `references/`：文献资源
- `tables_inputs/` 和 `figures_inputs/`：仅当模板、期刊或编译策略需要本地复制时使用

默认主稿应优先直接消费 `../05_analysis_output/export_for_paper/` 中的接口，而不是重新做表。

## 清理规则

只有在用户明确要求删除旧分析时，才删除生成产物。安全删除范围通常包括：

- `02_data_prep/interim`
- `02_data_prep/final`
- `02_data_prep/audit`
- `03_research_design`
- `04_spss_syntax`
- `05_analysis_output`
- `06_paper_draft`
- `07_submission_package`
- `08_project_admin` 中由本流程自动生成的文件

不要删除：

- `01_source_data/raw` 中的原始数据副本
- `01_source_data/external` 中用户手动放入的外部数据
- 用户未确认属于本流程生成的其他文件

## 验证门禁

完成前至少检查：

- 清洗脚本可重复运行
- 最终分析数据存在且样本量与日志一致
- 研究设计、变量设计和模型设定与实际分析一致
- 结果表中的数字来自 SPSS 输出或结构化解析结果
- `05_analysis_output/export_for_paper/` 中的接口文件存在
- `06_paper_draft/paper.tex` 中的 `\input{}` 或图形引用有效
- PDF 编译成功，或已记录明确失败原因
