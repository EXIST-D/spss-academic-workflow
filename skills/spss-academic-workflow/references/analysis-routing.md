# 分析触发与自动路由

## 一、显式分析触发

如果用户明确说出要做哪种分析，优先尊重用户指定路线，再自动补齐前置和收尾步骤。

### 1. 数据读取前置

无论用户点名哪种分析，默认先执行：

- `spss_check_status`
- `spss_list_files` 或定位目标文件
- `spss_list_variables`
- `spss_read_metadata`
- `spss_file_summary`
- `spss_read_data`

如输入为 CSV，先执行：

- `spss_import_csv`

### 2. 显式分析到工具的映射

| 用户表述 | 默认主工具 | 常规补充 |
|---|---|---|
| 描述性统计 | `spss_descriptives` / `spss_frequencies` | 缺失说明、变量标签整理 |
| 频数/列联表 | `spss_frequencies` / `spss_crosstabs` | 卡方解释、组别占比 |
| 相关分析 | `spss_correlations` | `spss_descriptives`、共线性说明 |
| t 检验 | `spss_t_test` | `spss_normality_outliers`、必要时 `spss_nonparametric_tests` |
| 方差分析 | `spss_anova` | 事后检验、必要时 `spss_glm_univariate` |
| 线性回归 | `spss_regression` | 描述统计、相关矩阵、稳健性检查 |
| 二元逻辑回归 | `spss_logistic_regression` | 描述统计、分类结果解释 |
| 序数回归 | `spss_ordinal_regression` | 平行线检验说明 |
| 多分类模型 | `spss_genlin` | 指定 `MULTINOMIAL` 分布 |
| 重复测量 | `spss_repeated_measures_anova` 或 `spss_mixed` | 数据结构检查 |
| 混合模型 | `spss_mixed` / `spss_genlinmixed` | subject/repeated 结构说明 |
| 生存分析 | `spss_kaplan_meier` / `spss_cox_regression` | 事件定义、删失说明 |
| 因子分析 | `spss_factor` | 信度、量表得分 |
| 信度分析 | `spss_reliability_alpha` | `spss_compute_scale_score` |
| 聚类分析 | `spss_cluster_hierarchical` / `spss_twostep_cluster` | 变量标准化说明 |
| 判别分析 | `spss_discriminant` | 分类准确率解释 |
| MANOVA/GLM | `spss_manova` / `spss_glm_univariate` | 组间效应解释 |

### 3. 显式分析模式下的默认补齐

除非用户明确说“只做这个检验”，否则默认补齐：

- 数据摘要。
- 核心变量说明。
- 至少一张主结果表。
- 中文结果段落。
- 适合时的诊断或替代检验。

## 二、自动分析路由

如果用户只说“用 spss skills 分析某数据”，而没有明确说检验类型，则按以下保守路线：

### 第一步：识别任务类型

- 如果用户给出明确因变量、自变量、控制变量，视为验证性分析。
- 如果用户只给数据文件，没有研究设定，视为探索性分析。
- 如果用户给出论文题目但变量不完整，先做变量识别与可行性判断，再进入验证性分析。

### 第二步：自动选择分析主线

#### 探索性分析

默认执行：

- 文件概览和变量识别。
- 描述性统计。
- 分类变量频数。
- 核心连续变量相关矩阵。
- 初步发现总结。
- 对可行的后续模型提出建议。

只有在数据结构和变量关系足够清楚时，才自动补回归或聚类等强假设分析。

#### 验证性分析

按因变量类型自动选模型：

- 连续：`spss_regression`
- 二分类：`spss_logistic_regression`
- 有序分类：`spss_ordinal_regression`
- 多分类：`spss_genlin` with `MULTINOMIAL`
- 多因变量：`spss_manova`
- 时间到事件：`spss_kaplan_meier` / `spss_cox_regression`
- 重复测量或层级结构：`spss_mixed` / `spss_genlinmixed`

### 第三步：自动补充

默认尝试以下补充模块中的至少一个：

- 诊断检验。
- 稳健性检验。
- 异质性分析。
- 机制或调节分析。

前提是：

- 样本量允许。
- 变量定义清楚。
- 不会明显超出数据的识别能力。

## 三、止损规则

以下情况不要强行自动做复杂模型：

- 因变量不明确。
- 变量编码不清晰。
- 样本量过小。
- 缺失过多。
- 用户问题本身只需要描述性结果。
- 当前数据不支持机制、异质性或因果解释。

遇到这些情况，应退回更保守的分析，并在日志中写明原因。

## 四、结果汇报规则

无论显式还是自动路由，最终都要说明：

- 实际调用了哪些工具或回退函数。
- 为什么选择当前分析路线。
- 哪些分析没做，以及为什么。
- 结果支持什么结论，不支持什么结论。
