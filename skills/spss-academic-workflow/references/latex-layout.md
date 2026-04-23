# 中文论文 LaTeX 排版规划

## 适用时机

当用户已经完成或接近完成实证分析，希望把结果整理为一篇规范、清晰、可编译的中文 LaTeX 论文时，读取本文件。

## 总体目标

中文论文排版的目标不是“花哨”，而是：

- 结构清晰
- 结果表接口稳定
- 图表和正文风格统一
- 编译链简单可靠
- 后续扩写、换模板或改投时成本较低

## 主稿规则

默认主稿：

```text
06_paper_draft/paper.tex
```

默认版式选择：

- 首选 `ctexart`
- 只有在篇幅很长且天然需要 chapter 级结构时，才考虑 `ctexrep`
- 若用户已有既定模板，优先沿用

## 与分析输出的衔接

分析结果的真源在 `05_analysis_output/`：

- `tables/`：机器生成的原始表格
- `figures/`：机器生成的图形
- `notes/`：中文结果说明
- `export_for_paper/`：供主稿消费的稳定接口

默认策略：

- 分析脚本生成 `05_analysis_output/export_for_paper/*.tex`
- 主稿通过 `\input{}` 直接消费这些接口
- 不在主稿中手工重做表格

推荐写法：

```latex
\input{../05_analysis_output/export_for_paper/paper_table_03_baseline_model.tex}
```

`06_paper_draft/tables_inputs/` 和 `06_paper_draft/figures_inputs/` 仅在期刊模板、学校模板或编译方式要求本地复制时使用；默认不是统计结果的唯一真源。

论文侧接口命名统一使用 `paper_table_XX_<content>.tex` 或 `paper_figure_XX_<content>.tex`。其中 `XX` 对应正文展示顺序，`<content>` 使用小写 `snake_case`，例如 `paper_table_01_descriptive_statistics.tex`。

## 图表规范

### 表格

- 优先使用三线表风格
- 每张表有标题、编号、主体和表注
- 表注说明显著性符号、标准误形式、参考组或变量定义
- 表格过宽时，优先简化列名、拆表或调整列宽，必要时再用 `resizebox`

### 图形

- 图形文件放在 `05_analysis_output/figures/`
- 图题、编号和表格风格统一
- 图注只写必要说明，不重复正文
- 纯探索性图形可放附录

## 参考文献与引用流

优先保证引用流顺畅：

- 明确 `.bib` 是否存在
- 明确使用 `bibtex` 还是 `biber`
- 确认引用命令风格统一
- 文献样式和当前 class 不冲突

如用户未提供正式文献库：

- 不编造文献条目
- 可以保留引用占位或待补文献说明

## 编译链

普通中文论文默认优先：

```powershell
xelatex -interaction=nonstopmode -halt-on-error paper.tex
```

如项目更适合 `latexmk`：

```powershell
latexmk -xelatex -interaction=nonstopmode paper.tex
```

建议把 PDF 输出到：

```text
06_paper_draft/output/paper.pdf
```

## 排版 QA

### 编译前检查

- 主稿路径是否明确
- `\input{}` 的表格路径是否存在
- class 和核心宏包是否冲突
- 图表文件是否存在
- 参考文献文件是否存在

### 编译后检查

- PDF 是否成功生成
- 目录、页码、交叉引用是否正常
- 表格是否溢出页面
- 中文是否正常显示
- 变量名中的下划线、百分号是否正确转义

### 交付前检查

- 标题、摘要、关键词是否齐全
- 主回归表和正文是否对应
- 图表编号是否连续
- 表注和显著性说明是否统一
- 文献是否挂接成功

## 与 SPSS 工作流的边界

LaTeX 排版必须服从 SPSS 实证分析主线：

- 结果数字以 `05_analysis_output/` 为准
- 结果解释以 `05_analysis_output/notes/` 为准
- 主稿负责组织，不负责重新计算结果
- PDF 编译只是交付阶段，不改变统计结论
