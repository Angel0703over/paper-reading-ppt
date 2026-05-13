# Paper Reading PPT

[English](README.md)

`paper-reading-ppt` 是一个兼容 Agent Skills 格式的论文阅读与中文 PPT 内容生成 skill。

它主要面向 AI Systems 方向论文，尤其适合 LLM Serving、KV Cache、边缘推理、调度、分布式推理、Serverless Inference、模型并行和多模态推理等主题。

## 功能

- 根据论文章节生成中文 PPT 大纲。
- 解释公式、变量、目标函数、约束和系统含义。
- 按汇报逻辑讲解图和表。
- 拆解 Evaluation 部分，包括实验设置、baseline、指标、主要结果、消融实验和结论。
- 将 Related Work 或信息密度较高的章节压缩成一页 PPT。
- 生成适合组会或课堂汇报的中文讲解稿。

## 目录结构

```text
paper-reading-ppt/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── ppt-style-guide.md
│   ├── paper-reading-workflow.md
│   ├── formula-explanation-guide.md
│   └── figure-table-explanation-guide.md
├── templates/
│   ├── section-slide-template.md
│   ├── figure-slide-template.md
│   ├── formula-slide-template.md
│   └── evaluation-slide-template.md
└── scripts/
    ├── extract_pdf_text.py
    ├── extract_figures.py
    └── check_slide_density.py
```

## 安装

将整个 `paper-reading-ppt` 文件夹复制或克隆到你的 Agent Skills 工具所使用的 skills 目录中。

对于 Codex 风格的本地 skills，常见位置是：

```bash
~/.codex/skills/paper-reading-ppt
```

Windows 上通常类似：

```text
C:\Users\<you>\.codex\skills\paper-reading-ppt
```

如果你的工具支持 workspace-local skills，也可以把这个文件夹直接放在项目工作区中。

## 使用示例

```text
Use $paper-reading-ppt to explain the Evaluation section of this paper as Chinese PPT slides.
```

```text
Use $paper-reading-ppt to explain Figure 4 from beginning to end, including what the authors want to prove.
```

```text
Use $paper-reading-ppt to compress Related Work into one Chinese PPT slide.
```

```text
Use $paper-reading-ppt to explain this optimization formula and connect each term to the system design.
```

也可以直接用中文提问，例如：

```text
使用 $paper-reading-ppt，把这篇论文的 Evaluation 部分按照文章顺序整理成中文 PPT 内容。
```

```text
使用 $paper-reading-ppt，帮我解释这个公式里每一项的系统含义。
```

## 可选脚本

这个 skill 的核心功能不依赖 Python。`scripts/` 里的脚本只是辅助工具。

安装可选依赖：

```bash
pip install -r requirements.txt
```

提取 PDF 文本：

```bash
python scripts/extract_pdf_text.py paper.pdf paper.txt
```

提取 PDF 中的嵌入图片：

```bash
python scripts/extract_figures.py paper.pdf extracted_figures/
```

检查 Markdown PPT 草稿的 bullet 密度：

```bash
python scripts/check_slide_density.py slides.md
```

## 准确性与边界

这个 skill 不应该凭空编造论文内容。如果缺少论文原文、截图、公式、图或表，agent 应该要求用户提供材料，或者明确标注哪些内容是基于已有上下文的推断。

如果要公开上传到 GitHub，请不要把没有授权分享的论文 PDF、提取图片或大段原文一起提交到公开仓库。

## 许可证

MIT License。详见 `LICENSE.txt`。
