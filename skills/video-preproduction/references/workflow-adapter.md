# Workflow / Board 接入

仅在当前项目已使用本套 Workflow/Pipeline 时读取。本页说明该工具组合的命令与数据约定；其他环境使用自己的公开接口，无需仿造这些文件。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

- 本轮可用 `video-workflow route [项目] --task concept` 或 `--task storyboard`，无项目可用 `--input` 声明稿件/参考，不自动建目录。
- 结构与方法来源见 `workflow:editorial-grammar`、`workflow:technique-cards`；接初剪见 `workflow:first-cut#从素材与文稿接到初剪`；职责见 `workflow:full-workflow-routing`。
- 包装先查本片采用，再用 `motion:templates`。产物按实际 article/concepts/references 角色保存。
- Pipeline `project-context --segment`、Board preflight/storyboard 只检查其支持格式；已有自定义表达 JSON 可直接读，无需重复转换成 Board。明确采用走 `source-link-prepare`，旧框架物化不是默认步骤。
