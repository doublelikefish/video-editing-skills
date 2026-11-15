# Color / Workflow 接入

仅在当前项目已使用本套 Workflow/Pipeline 时读取。本页说明该工具组合的命令与数据约定；其他环境使用自己的公开接口，无需仿造这些文件。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

- 可用 `video-workflow route [项目] --task color` 恢复本轮；读取 `color:capability-map`、`color:color-workflow`、`color:primary-correction` 核对支持范围。
- 当前实现提供 CDL/prepared-DRX 等路径，按真实版本能力调用；二级/跟踪不因此自动支持。精确同帧对照复用 Color 指定帧与缓存。
- 聊天/文档可直接回传方案、源身份与实际对照；选用 Color Review 时再用其公开接口。结果沿 Color 会话、editing 和预览的实际位置保存。
- 输入事实归原库，影片风格留本片。全流程接续必要时查 `workflow:full-workflow-routing`。
