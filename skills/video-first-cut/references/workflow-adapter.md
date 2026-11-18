# Workflow / Pipeline 接入

仅在当前项目已使用本套 Workflow/Pipeline 时读取。本页说明该工具组合的命令与数据约定；其他环境使用自己的公开接口，无需仿造这些文件。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

- 已有原生粗剪恢复看 `pipeline:native-intake`；从素材开始的采用/证据字段看 `workflow:first-cut`。
- Resolve 启动后用 `video-workflow resolve-inspect --wait-seconds 30` 等待就绪；无当前工程也是有效连接。核实为未保存空白 `Untitled Project` 时，使用 `video-workflow run pipeline:cli -- resolve-create-project --name 名称 --receipt 新回执路径 --expected-current-project-id 实际ID --allow-empty-startup-project`，不传 checkpoint；真实已有工程仍按 native-intake 导出保护点。已有命令缺这些参数先核对本机公共工具版本，不回到项目里的旧拷贝或临时绕过。
- `video-workflow brief 项目 --task first-cut` 恢复当前采用/相关证据，`first-cut check` 检查支持范围。`selection_scope` 只描述计划目录。
- 首次编译用 `source-link-prepare --selection-package`；已有计划用 `source-link-screening` 更新指定源，再 prepare/check。参数查 `pipeline:shared-seams`，不能只将路径放备注。执行用支持的 cut-plan/source-link/局部原生接口。
- 已有较完整方法来源：`workflow:editorial-grammar`、`workflow:technique-cards`；切口验收：`workflow:editorial-qa#切口覆盖先绑定目标和退出点`；真实 AV 工具与限制：`workflow:av-review`。
- 结果沿 FIRST_CUT_CONTEXT/NEXT_ACTIONS；声明初剪完成前调用 `first-cut check` 和 `workflow:shared-execution` 的 complete，明确采用另用 adopt。自写渲染脚本、直接 SDK 导出或降低预览分辨率不豁免完成核对。接口不支持当前产物时如实保留未完成核验，不伪造计划/观察来通过，也不退回只凭渲染成功报完成。预览可以直接绑定媒体文件，或使用已选 Review 的登记版；缺少新接口时明确该安装版本限制，不强迫用户改用 Review。检查字段通过不等于选镜/声音通过。
- 按 `workflow:review-delivery` 沿聊天、文档或已选 Review 回传；选用 Review 产品时才调用 decide/note/return。
