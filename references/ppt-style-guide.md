# PPT Style Guide

## Default Slide Density

Use 3-5 main bullets per slide. Each bullet should be short enough to paste into a slide without becoming a paragraph.

Prefer:

- Problem -> Method -> Result
- Challenge -> Design -> Benefit
- Observation -> Mechanism -> Conclusion
- Setup -> Metric -> Finding

Avoid:

- Copying long paper paragraphs directly
- Listing too many numbers without explaining the trend
- Putting many equations on one slide
- Saying generic phrases such as "效果很好" or "显著提升" without naming the metric and reason

## Chinese Academic Presentation Style

Use precise, presentation-ready Chinese. Good reusable phrases include:

- 本文关注的问题是...
- 作者的核心观察是...
- 这一设计的作用是...
- 从系统角度看...
- 该实验主要验证...
- 这张图想说明...
- 这里的关键结论是...

## Slide Title Rules

Write titles as claims or topics, not vague labels.

Good:

- "KV Cache 迁移成本使缓存决策具有时间耦合性"
- "Evaluation 先验证端到端性能，再拆解关键设计"

Weak:

- "方法介绍"
- "实验结果"
- "相关工作"

## Speaker Notes

Speaker notes should explain the logic of the slide, not merely repeat the bullets. Use natural Chinese suitable for a research group presentation.

When explaining a system paper, connect:

- Workload assumption
- Bottleneck
- System design
- Metric improvement
- Limitation or trade-off

## Compression Rules

When the user asks for "只要一页" or "压缩一下":

- Keep only one central message.
- Combine minor details into one bullet.
- Keep at most one formula or one figure unless the user explicitly asks otherwise.
- Move implementation details into speaker notes or omit them.

When the user asks for "讲详细一点":

- Add the motivation before the mechanism.
- Explain key terms once.
- Include the paper location and corresponding figure/table/equation.
