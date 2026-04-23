# SPSS-MCP 使用说明

## 环境发现与配置

不要假设某台机器的固定盘符、用户目录、conda 环境名或 SPSS 安装路径。执行时按以下优先级发现环境：

1. 优先读取用户显式提供的 `SPSS_INSTALL_PATH`、Python 可执行文件、conda/venv 名称和项目根目录。
2. 如用户未提供，检查当前 Codex 进程可用的 Python：`python`、`python3`、`py -3` 或当前虚拟环境解释器。
3. 检查 `spss-mcp`、`pandas`、`pyreadstat` 是否已安装；缺失时在当前环境或用户指定环境中安装。
4. 检查 SPSS batch 程序是否可用。Windows 常见程序名为 `stats.exe`。
5. 将实际发现的 Python、SPSS、SPSS-MCP 路径写入 `05_analysis_output/logs/run_XX_<content>.md`。

常用诊断命令：

```powershell
python -m pip show spss-mcp
python -m spss_mcp.cli status
```

## 推荐调用方式

如当前 Codex 会话直接暴露 SPSS MCP 工具，优先调用这些工具。若工具未直接暴露，可在 Python 中调用已安装的 `spss_mcp.server` 函数，沿用同一套 server 逻辑。

分析阶段应记录：

- 使用了哪些 MCP 工具或回退函数
- 输入数据路径
- 输出表格路径
- SPSS syntax 类型
- 环境信息与任何重要 warning

这些内容统一写入：

```text
05_analysis_output/logs/run_XX_<content>.md
```

## Windows 与旧版 SPSS 兼容策略

SPSS 24 对新 Python 语法、中文路径和中文变量名可能不稳定。遇到问题时按以下顺序处理：

1. 将分析变量转换为英文变量名。
2. 尽量把 SPSS 输入输出放在 ASCII 子路径下。
3. 优先让 SPSS 读取 `.sav`，而不是直接读取中文路径下的 Excel。
4. 必要时为 SPSS 单独设置临时目录。

## SPSS syntax 规范

- 路径使用正斜杠或转义反斜杠。
- 回归建议使用明确的模型块，例如控制变量模型、核心变量模型、完整模型。
- 分类变量要说明虚拟变量构造和参考组。
- 对 SPSS 输出进行结构化解析后再生成论文表格，不从截图或终端直接抄数。
