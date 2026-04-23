# SPSS-MCP 工具矩阵

以下名称基于当前已安装 `spss_mcp` 包中注册的工具名。不同 Codex 会话中，这些工具不一定都以原生 `mcp__spss__*` 形式直接显示；如果未直接显示，可用 Python 调用 `spss_mcp.server` 中的同名函数回退执行。

## 1. 状态、发现与数据文件

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_check_status` | 状态诊断 | 检查 SPSS、pyreadstat、pandas、路径、超时配置 | 是 | 推荐最先调用 |
| `spss_list_files` | 文件发现 | 列出目录中的 `.sav` 文件 | 是 | 文件级 |
| `spss_list_variables` | 元数据 | 读取变量列表和标签 | 是 | 常作分析前置 |
| `spss_read_metadata` | 元数据 | 读取变量类型、标签、取值信息 | 是 | 常作分析前置 |
| `spss_read_data` | 数据预览 | 读取前若干行观察值 | 是 | 常作分析前置 |
| `spss_file_summary` | 数据概览 | 获取样本量、变量数等摘要 | 是 | 常作分析前置 |
| `spss_import_csv` | 导入转换 | 将 CSV 导入为 `.sav` | 是 | 适合工作流起点 |

## 2. 结构化方法发现与底层 syntax

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_list_supported_methods` | 方法发现 | 查看 registry-backed 的高级结构化方法 | 是 | 高级分析前可先查 |
| `spss_get_method_schema` | 方法 schema | 获取高级方法参数 schema | 是 | 适合自动编排 |
| `spss_get_method_support` | 方法支持信息 | 查看支持级别、命令家族、断言 | 是 | 适合自动编排 |
| `spss_run_syntax` | 底层执行 | 直接运行自定义 SPSS syntax | 是 | 最灵活 |
| `spss_validate_syntax` | syntax 校验 | 执行前检查 syntax | 是 | 与 `spss_run_syntax` 配套 |

## 3. 基础统计与探索性分析

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_frequencies` | 频数 | 分类变量频数和比例 | 是 | EDA 起点 |
| `spss_descriptives` | 描述统计 | 均值、标准差、极值 | 是 | EDA 起点 |
| `spss_crosstabs` | 列联表 | 分类变量交叉表和卡方 | 是 | 分组差异 |
| `spss_t_test` | 均值比较 | 单样本、独立样本、配对 t 检验 | 是 | 分组或前后测 |
| `spss_anova` | 方差分析 | 单因素 ANOVA 与事后检验 | 是 | 组间差异 |
| `spss_correlations` | 相关分析 | Pearson 或 Spearman | 是 | 回归前常用 |
| `spss_nonparametric_tests` | 非参数检验 | Mann-Whitney、Wilcoxon、Kruskal-Wallis | 是 | 分布不满足假设时 |
| `spss_normality_outliers` | 正态性/异常值 | 分布、异常值检查 | 是 | 假设检验辅助 |

## 4. 回归、量表和一般学术分析

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_regression` | 线性回归 | OLS、多模型回归 | 是 | 实证分析高频 |
| `spss_factor` | 因子分析 | 探索性因子提取 | 是 | 量表构建 |
| `spss_reliability_alpha` | 信度分析 | Cronbach's alpha | 是 | 量表检验 |
| `spss_compute_scale_score` | 量表得分 | 计算题项均值、总分等 | 是 | 常与信度配合 |
| `spss_repeated_measures_anova` | 重复测量方差分析 | 同一对象多时点或多条件比较 | 是 | 前后测 |

## 5. 广义与高级回归

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_logistic_regression` | 二元逻辑回归 | 因变量为二分类 | 是 | registry-backed |
| `spss_ordinal_regression` | 序数回归 | 因变量为有序分类 | 是 | registry-backed |
| `spss_genlin` | 广义线性模型 | 正态、二项、泊松、Gamma、负二项、多项分布 | 是 | 可覆盖多项模型 |
| `spss_mixed` | 混合模型 | 线性混合模型 | 是 | registry-backed |
| `spss_genlinmixed` | 广义线性混合模型 | 混合广义模型 | 是 | registry-backed |
| `spss_glm_univariate` | 单变量 GLM | 因变量一个、因素与协变量组合 | 是 | registry-backed |

## 6. 生存分析

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_cox_regression` | Cox 回归 | 生存时间与风险因素分析 | 是 | registry-backed |
| `spss_kaplan_meier` | Kaplan-Meier | 生存曲线和组间比较 | 是 | registry-backed |

## 7. 多元统计与分类

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_discriminant` | 判别分析 | 基于多个变量进行分组判别 | 是 | registry-backed |
| `spss_manova` | MANOVA | 多个因变量的方差分析 | 是 | registry-backed |

## 8. 聚类

| 工具名 | 类别 | 典型用途 | 当前包内已注册 | 备注 |
|---|---|---|---|---|
| `spss_cluster_hierarchical` | 层次聚类 | 样本分群 | 是 | registry-backed |
| `spss_twostep_cluster` | 两步聚类 | 连续与分类变量混合聚类 | 是 | registry-backed |

## 使用说明

- “当前包内已注册 = 是”表示该名称已经真实存在于本机安装的 `spss_mcp.server` 中。
- 这不等于“当前对话一定显示为原生 MCP 工具”。若当前会话没有 `mcp__spss__*` 命名空间，可用 Python 回退调用。
- 对需要高可靠参数校验的高级方法，优先用 `spss_list_supported_methods`、`spss_get_method_schema`、`spss_get_method_support` 先检查。
