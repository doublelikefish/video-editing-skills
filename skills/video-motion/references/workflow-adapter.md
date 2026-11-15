# Motion / Workflow 接入

仅在当前项目已使用本套 Workflow/Pipeline 时读取。本页说明该工具组合的命令与数据约定；其他环境使用自己的公开接口，无需仿造这些文件。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

- 可用 `video-workflow route [项目] --task packaging`；读 `workflow:template-reuse`，先查当前实例，再查 `motion:templates`、`motion:designs` 及其图册/源。
- 旧 components、creator-card、实验或历史 ZIP 不代表当前生产模板库。无法定位时修复绑定，不以旧组件代替当前采用。
- 本套目前主要生产路径为既有 Remotion renderer；保留请求、字体/素材身份、模板修订和回执。普通原片/照片仍可调，外部渲染可回填。
- cue 与标记接续看 `workflow:motion-sound-execution` 及其“从设计决定到时间线标记”；只保留与本轮有关的决定。
- Pipeline motion-plan 消费已验证回执；回填仍核实支持方式与实际条目。结果放本片 elements/working_renders 和实例记录。
- 审阅版按 `workflow:review-delivery` 沿聊天/文档或已选 Review 交付；只有选用服务时核对登记和页面。
