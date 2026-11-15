# 声音工具 / Workflow 接入

仅在当前项目已使用本套 Workflow/Pipeline 时读取。本页说明该工具组合的命令与数据约定；其他环境使用自己的公开接口，无需仿造这些文件。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

- 真实听音工具、输入准备及限制读 `workflow:av-review`；已保存有效观察优先复用。
- 查曲、器乐分轨与 SFX 时读 `workflow:sound-sources`；Epidemic 的既有 MCP/CLI 与 schema 按当前安装核实，适配入口 `workflow:epidemic-mcp`。认证由本机安全配置提供，不能装进 Skill 包；工具未挂载不代表没有既有缓存/素材。
- 原轨提取、变速、处理延迟与回填见 `workflow:motion-sound-execution#分轨到最终导出的检查`；音乐编排的工具细节见该资源的“音乐编辑与混音”。
- 声画方法来源可按需查 `workflow:technique-cards#声画组织`。设计落到本片 cue/标记，支持的音轨 API 或 FFmpeg 负责实现；高级 Fairlight 界面能力不自动成为脚本能力。
- `audit-audio --roles` 只核对声明的信号关系，不认证自然度、音乐适配或原 VO 内容保留。
- 返回对象按 `workflow:review-delivery`，聊天/文档可直接交付文件、版本与处理结果。已选 Review 时，整片走版本链、局部走关联候选、独立声音走独立媒体，再执行公共回调。
