# Paper Reading PPT

[简体中文](README.zh-CN.md)

`paper-reading-ppt` is an Agent Skills-compatible skill for reading academic papers and turning them into Chinese PPT-ready explanations.

It is designed for AI systems papers, especially topics such as LLM serving, KV Cache, edge inference, scheduling, distributed inference, serverless inference, model parallelism, and multimodal inference.

## What It Does

- Generate Chinese slide outlines for paper sections.
- Explain formulas, variables, objectives, constraints, and system meaning.
- Interpret figures and tables for presentation.
- Break down Evaluation sections into setup, baselines, metrics, results, ablations, and conclusions.
- Compress Related Work or dense sections into one slide.
- Produce Chinese speaker notes for research group or classroom presentations.

## Repository Structure

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

## Installation

Copy or clone this folder into the skills directory used by your Agent Skills-compatible tool.

For Codex-style local skills, a typical location is:

```bash
~/.codex/skills/paper-reading-ppt
```

On Windows, the equivalent may look like:

```text
C:\Users\<you>\.codex\skills\paper-reading-ppt
```

You can also keep the folder in a workspace if your tool supports workspace-local skills.

## Example Prompts

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

## Optional Scripts

The skill works without Python dependencies. The scripts are optional helpers.

Install optional dependencies:

```bash
pip install -r requirements.txt
```

Extract PDF text:

```bash
python scripts/extract_pdf_text.py paper.pdf paper.txt
```

Extract embedded PDF images:

```bash
python scripts/extract_figures.py paper.pdf extracted_figures/
```

Check Markdown slide density:

```bash
python scripts/check_slide_density.py slides.md
```

## Safety And Accuracy

This skill should not invent paper content. If the paper text, screenshot, formula, figure, or table is missing, the agent should ask for the source material or clearly mark any inference.

For copyrighted papers, avoid committing PDFs, extracted figures, or large copied text into public repositories unless you have the right to share them.

## License

MIT License. See `LICENSE.txt`.
