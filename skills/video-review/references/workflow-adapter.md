# Pipeline Review 接入

仅在当前项目已选用本套 Review 产品时读取。本页说明其命令与数据约定；使用 Workflow/Pipeline 剪辑不要求新项目注册 Review。已有 Review 版本、反馈批次或登记记录时，默认沿这条链继续登记和回写。聊天/文档反馈按包内反馈格式直接闭环，无需仿造这些文件或等待服务同步。

先确认 `video-workflow` 可用及本机绑定；`video-workflow resource ID --read` 解析下文资源，`video-workflow run PROVIDER:COMMAND -- 参数` 调用工具。缺绑定时说明具体能力缺口，不能猜相邻目录或自动初始化项目。需要发现才用 route/brief，已知入口可直接调用。原生执行约定为 `workflow:resolve-execution`：核对实际支持、工程/时间线与单写入者，失败不自动回退前台。

以下命令通过 `video-workflow run pipeline:cli -- 命令 参数` 调用。其他 Review 产品沿自己的公开接口，不仿造这些字段。

## 读取和决定

1. 先完成或复用评审登记。使用已有 `review_feedback` 登记接口登记实际媒体/版本和父版本，核对预览、帧率、起点、计划指纹与可访问入口。登记之前只能提供聊天/文档预览，不能调用 Review 页面作为反馈目标。
2. 调用 `review-prepare --project 本片项目登记.json --out 本轮批次.json`；输入类型及参数看 `pipeline:first-cut-revision`。project 是已有 editing_project.v1 JSON，不是影片目录或 Workflow schema_version=2 登记。
3. 读取最终批次的 tasks[].editing_instruction、锚点/参考、work_queue.items、regression_checks、carryover/held_feedback。版本或意见变化后刷新，旧时码核对源 hash 和映射。
4. 用 `review-decide` 重新核对意见状态/修订，写本轮决定、保留范围及完成依据。全片举例的范围补充可查 `workflow:agent-integration#从举例回到完整任务范围`。
   `decision.acceptance` 按原话中的独立要求展开，`result.checks` 与之逐项对应；“完成修改/已核对”不能代替多个条件。现有接口只校验声明条件齐全，语义是否漏拆仍由负责人对照原话检查。
5. 直接 SDK 导出的首版按 `workflow:review-delivery#第一版来自原生工程或直接-sdk-导出` 登记真实媒体/聊天反馈；缺映射标明 unmapped，不捏造计划。

## 证据和结果

- 复查既有意见通过公共 `review-note`、kind=evidence 追加真实对象、源/时间、证据与未完成项。真正新问题才建普通反馈；未登记候选仅引用路径/hash。
- 写后刷新 prepare，复用历史回执避免重复。向已授权制作会话通知反馈 ID 与最终记录路径，通知不代替正式回调。
- 执行并核查后用 `review-return` 或现有 Color 对应公开接口绑定原意见、结果版本和证据。partial 使用 completion_state=partial、pending/failed 检查与 remaining_work，维持 in_progress。
- 完整结果是 returned 待复核；用户接受单独记录。原基准、并发修订、删除/取代、幂等与版本检查不能由旧快照绕过。
- 禁止临时脚本直接 UPDATE Review 数据库或批量写 resolved 来补回执。公开回调失败保持原状态和明确缺口，处理报错后重试；不能把有修订保护的接口换成无保护写库。回调后刷新 prepare，按有效 ID 集合、逐项 checks、结果版本和 remaining_work 核对，不能只数行数。
- 按 `workflow:review-delivery` 运行 `review-check --scope film|segment|media` 核对版本、可达和反馈定位。页面机制回归按变化/故障决定，日常改片走 API。
- 原 Review/control、FIRST_CUT_CONTEXT/NEXT_ACTIONS 继续承载状态；brief 的 reconciliation/followthrough 冲突先核实。产品开发和服务迁移另行处理，不在影片修改中顺带执行。
