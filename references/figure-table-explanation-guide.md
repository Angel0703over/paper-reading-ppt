# Figure And Table Explanation Guide

## Figure Explanation Order

When explaining a figure, cover:

1. What question the figure is trying to answer.
2. What the x-axis, y-axis, curves, bars, colors, or legends mean.
3. What trend or contrast is visible.
4. What conclusion the authors want to support.
5. How to present the figure orally.

## Table Explanation Order

When explaining a table, cover:

1. What methods, settings, datasets, or systems are compared.
2. What metrics are used.
3. Which rows or columns matter most.
4. Which result is best or most meaningful.
5. What conclusion the table supports.
6. How to summarize it on one PPT slide.

## Reading Experimental Visuals

For system papers, pay attention to:

- Latency: average, p95, p99, tail latency
- Throughput: requests/s, tokens/s, tasks/s
- Cost: GPU hours, memory, bandwidth, migration overhead
- Quality: accuracy, BLEU, Rouge, F1, task success rate
- Resource metrics: utilization, cache hit rate, load balance, cold start time

## Avoid Shallow Restatement

Do not only say "横轴是 A，纵轴是 B". Add:

- Why this metric matters
- What comparison is important
- Whether the trend validates a design choice
- What limitation or trade-off is visible

## Multi-Figure Walkthrough

When the user asks to explain figures from beginning to end:

- Follow figure number order.
- Group subfigures under the same figure.
- State the role of each figure in the paper's argument.
- Avoid over-explaining minor subplots unless they change the conclusion.
