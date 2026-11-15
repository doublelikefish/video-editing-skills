# Workflow / 原生渲染接入

仅在当前项目已使用本套 Workflow/Pipeline 时读取。本页说明该工具组合的命令与数据约定；其他环境使用自己的公开接口，无需仿造这些文件。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

- 按任务用 `video-workflow route [项目] --task delivery`、`--task publish` 或 `--task archive-reuse`，只展开适用部分。
- 渲染读 `workflow:native-render`：明确计划 → 应用设置 → preset 读取 → 作业读回 → 指定作业渲染 → 文件验证。SetRenderSettings 成功不作为交付验收。
- 收尾与手改接续见 `workflow:editorial-qa#收尾与手改交接`，同步当前采用/进行中与实际剩余项。
- 产物沿实际 final_renders/exports/final_version/publish/records 角色，目录约定必要时读 `workflow:workflow`；既有项目位置不批量改造。
