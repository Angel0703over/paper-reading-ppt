---
name: paper-reading-ppt
description: >-
  Analyze AI systems papers and generate Chinese PPT-ready explanations, slide
  outlines, speaker notes, formula explanations, figure/table interpretations,
  related-work summaries, and evaluation-section walkthroughs. Use when the user
  asks to read a paper, prepare PPT content, explain equations, explain figures
  or tables, summarize experiments, compress a section into one slide, or
  produce Chinese research-group presentation notes for AI systems, LLM serving,
  KV cache, edge inference, scheduling, distributed inference, or multimodal
  inference papers.
---

# Paper Reading PPT

## Purpose

Use this skill to turn academic paper material into Chinese presentation content for research group meetings, classes, and paper-reading talks. Focus especially on AI systems, LLM/VLM inference, KV cache, serving systems, edge AI, scheduling, distributed inference, model parallelism, caching, and evaluation-heavy papers.

## Operating Rules

- Follow the paper's original order unless the user asks for thematic reorganization.
- Ground every claim in the provided PDF, extracted text, screenshot, figure, table, formula, or pasted excerpt.
- Mark inferred content clearly when only partial context is available.
- Ask for the paper, screenshot, title, section text, or figure/table/formula image when the requested content is unavailable.
- Preserve important English technical terms when Chinese translation would obscure meaning.
- Explain what the authors are trying to solve, why the design is needed, and how the evidence supports the conclusion.
- Avoid fabricating datasets, results, baselines, equations, figure trends, or experimental conclusions.
- Default to concise Chinese PPT-ready wording with speaker notes.

## Resource Map

Load only the resource needed for the current task:

- For slide density, Chinese phrasing, and PPT wording, read `references/ppt-style-guide.md`.
- For end-to-end paper reading and section ordering, read `references/paper-reading-workflow.md`.
- For equations, optimization objectives, constraints, and algorithmic math, read `references/formula-explanation-guide.md`.
- For figures and tables, read `references/figure-table-explanation-guide.md`.
- For reusable output structures, read the matching file in `templates/`.
- For local PDF helpers, use scripts in `scripts/` only when the environment has the required Python packages.

## Default Workflow

1. Identify the user's target: full paper walkthrough, specific section, formula, figure/table, evaluation, related work, compression, or speaker notes.
2. Inspect available source material before writing. Prefer PDF text, extracted text files, screenshots, and existing notes in the workspace.
3. Choose the smallest useful template:
   - Use `templates/section-slide-template.md` for normal section slides.
   - Use `templates/formula-slide-template.md` for equations or optimization problems.
   - Use `templates/figure-slide-template.md` for figures.
   - Use `templates/evaluation-slide-template.md` for experiments.
4. Produce Chinese output in a slide-ready format. Keep each slide focused on one idea unless the user requests compression.
5. Include speaker notes when the user is preparing a presentation, not just a summary.
6. State the corresponding paper location, figure/table/equation number, or section name whenever possible.

## Slide Content Defaults

- Use 3-5 bullets per slide.
- Prefer "Problem -> Design -> Result", "Observation -> Mechanism -> Conclusion", or "Challenge -> Method -> Benefit".
- Keep formulas limited to the key expression unless the user asks for a detailed derivation.
- For one-slide compression, keep only the main logical chain and the most important evidence.
- For oral notes, use natural Chinese presentation language while preserving technical precision.

## Default PPT Output Format

When generating slide content, use this format by default:

### 第 X 页：{主题}

**标题**  
{PPT 标题}

**原文位置**  
{Section / Figure / Table / Equation / Algorithm}

**PPT 内容**
- **核心点 1**：...
- **核心点 2**：...
- **核心点 3**：...

**讲解稿**  
{中文口语化讲解，说明这一页怎么讲}

**对应图表 / 公式**  
{建议放置的 Figure/Table/Equation；没有则写“无”}

## User Preference Adaptation

When the user says:

- "格式和上面一样": continue the previous slide structure and wording style.
- "只要一页": compress aggressively into one central message and at most 3 bullets.
- "内容太多": reduce formulas, secondary details, and repeated background.
- "讲详细一点": add motivation, variable meaning, and system-level intuition.
- "从头到尾讲一遍": follow the paper order and connect sections into a coherent storyline.
- "图从头到尾讲一遍": explain each figure by purpose, axes or legend, trend, conclusion, and presentation wording.
- "表格从头到尾讲一遍": explain each table by compared methods, metrics, best result, and supported conclusion.

## Do Not

- Do not invent experimental numbers, baselines, datasets, or figure trends.
- Do not claim to have read the full paper if only screenshots or partial text are available.
- Do not overfill slides with dense paragraphs.
- Do not translate every English technical term if keeping the English term is clearer.
- Do not explain formulas only mathematically; always connect them to the system design.

## Missing Context Policy

When the user asks about a specific section, figure, table, or formula and the source is not available:

1. State what material is missing.
2. Ask for the PDF, screenshot, extracted text, or pasted excerpt.
3. If enough partial context exists, give a best-effort explanation and label inferred parts.

## Quality Check

Before finalizing, verify that:

- The output follows the user's requested granularity, such as "one page", "reduce formulas", or "explain in detail".
- Claims are supported by provided source material.
- Slide bullets are not dense paragraphs.
- Figure/table explanations cover purpose, axes or metrics, trend, and conclusion.
- Formula explanations connect mathematical terms to system meaning.
