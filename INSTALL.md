本包：complete；包含 video-production, media-screening, video-preproduction, video-first-cut, video-color, video-motion, video-sound, video-subtitles, video-review, video-delivery。

# 视频剪辑 · 完整 Skill 包

本包包含 **10 个可安装的 Skill 目录**：新版 `video-production` 总控入口，以及原有九个阶段 Skill 和它们各自的参考文件。安装时一并复制；执行时由 Agent 按当前任务读取相关方法。

## 包内目录

```text
skills/
  video-production/       项目配置、规范模板、全流程与接续
  video-preproduction/    创意、文稿、结构与分镜
  media-screening/        素材接收、观察、候选与源窗口
  video-first-cut/        初精剪、选镜、剪点与切口覆盖
  video-color/            输入还原、匹配与调色
  video-motion/           包装、模板、分屏与合成
  video-sound/            声音选材、设计、编排与混音
  video-subtitles/        真实台词、时码与字幕显示
  video-review/           有效反馈、逐条修改与核查回传
  video-delivery/         输出、交付、归档与依赖
```

每个目录含 `SKILL.md`；阶段目录内的 `references/` 与 `agents/`（如有）一起保留。原有另一个总控 `video-editing` 不在本包，新项目统一从 `video-production` 进入；已有安装和项目约定不会被本包主动删除或改名。

## 安装后直接使用

把 `skills/` 内的 **10 个完整文件夹**复制到目标 Agent 支持的 Skill 目录，不要只复制 `video-production`，也不要把外层 `video-skills` 当成一项 Skill。

也可在解压后的 `video-skills` 目录，用 Python 3.10+ 运行可选安装器：

```text
python skill_bundle.py install --dest <目标 Agent 的 Skill 目录>
```

macOS/Linux 可能使用 `python3`。省略 `--skill` 就安装包内全部 10 项；手动复制不需要 Python。常见位置为 Codex/Cursor 的 `~/.agents/skills`、Claude Code 的 `~/.claude/skills`、Cursor 的 `~/.cursor/skills`，以宿主支持的位置为准。省略 `--dest` 时安装器沿用 Codex 的默认目录；其他宿主请明确指定。

相同内容重装跳过；已有不同内容时默认停止并报告，明确更新时用 `--replace` 备份后替换。安装器不联网、不安装媒体软件、不配置账号、不批量改项目。宿主发现 Skill 后即可使用；未发现时按宿主方式刷新或重开会话，不宣称仅复制文件就验证了自动加载。

直接告诉 Agent 这次要剪什么，例如：

> 用视频剪辑流程继续这条片。素材在……，项目存……，使用……软件，基准粗剪是……。这轮先完成……。

信息不必一次填齐。总控读取已有记录，只补问影响执行的缺项；项目位置明确后，实际创建/合并 `AGENTS.md`、`CLAUDE.md`，没有现成状态记录才创建 `PROJECT.md`，随后继续制作。项目模板就在总控 Skill 中。已有项目沿原规则和当前版本接续，不重建。

显式调用总控可用 Codex 的 `$video-production` 或 Claude Code 的 `/video-production`；独立字幕、声音等任务也可直接用对应阶段 Skill。系统、用户软件、Agent 执行端与接口能力分别识别，不按操作系统替用户选择剪辑软件。

## 工作和检查

十项职责为项目配置、创意分镜、素材筛选、初精剪、调色、包装、声音、字幕、审片反馈、输出交付。声音、调色、包装和字幕与初剪交叉进行；已有粗剪或局部反馈从对应位置进入，用户不必逐阶段审批。

总控说明每步的输入、用户交互、工具调用、产出和下一步；对应阶段 Skill 提供具体方法。需要时读取它的参考文件。只在项目确实使用 Workflow/Pipeline 时读取相应 `workflow-adapter.md`，其他工具按公开能力执行。

Review 可选，没有既有链可在聊天反馈；已有链沿原版本登记、修改和回传。每条要求分别记录结果、技术检查、真实看听和剩余项。需要的内部检查未完成时保持部分完成，用户接受不由 Agent 代填。

包内是方法与参考，不包括编辑器、FFmpeg、模型、API 密钥或素材。Agent 按本轮需要检查/接入实际工具；复制安装检查不代表所有系统、编辑器或客户端运行行为已经验证。
