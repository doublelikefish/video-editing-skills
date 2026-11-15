# 字幕工具 / Workflow 接入

仅在当前项目已使用本套 Workflow/Pipeline 时读取。本页说明该工具组合的命令与数据约定；其他环境使用自己的公开接口，无需仿造这些文件。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

- 可用 `video-workflow route [项目] --task subtitles`；读取 `workflow:native-subtitles` 及 `workflow:template-reuse` 的字幕部分。
- 当前采用的辅助对白与切口检查接 `workflow:editorial-qa`。已有转写和当前速度映射复用，不为辅助理解覆盖原生字幕轨。
- 原生脚手架只用于其支持的空轨；局部修改不支持时沿本片有效方法保留手改。
- 产物放 elements/editing/exports 的实际角色，绑定当前修订；轨道、导出模式和像素/外挂分别验证。
