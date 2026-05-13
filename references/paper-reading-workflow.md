# Paper Reading Workflow

## Source Inspection

Start from the most reliable available source:

1. PDF or paper text extracted from PDF
2. Screenshots of figures, tables, or equations
3. User-provided excerpts
4. Existing notes in the workspace
5. Paper title and partial context

Do not pretend to have read unavailable text. Clearly label inference when working from partial context.

## Full Paper Walkthrough

For a full paper presentation, organize slides in the paper's order:

1. Problem and motivation
2. Background and gap
3. Core observation
4. System/model overview
5. Method details
6. Formula or algorithm explanation
7. Evaluation setup
8. Main results
9. Ablation, sensitivity, or overhead
10. Related work and conclusion

## Section-Level PPT Generation

For a section, identify:

- The section's role in the whole paper
- The main question it answers
- The key technical terms
- The important figure/table/equation references
- The minimum slide count needed

Then generate slide content using:

- Title
- Original location
- PPT bullets
- Speaker notes
- Corresponding figure/table/formula

## Evaluation Workflow

When generating Evaluation slides, follow this order unless the paper's structure requires otherwise:

1. Experimental setup: hardware, models, datasets, workloads, traces
2. Baselines: what methods are compared and why
3. Metrics: latency, throughput, cost, memory, cache hit rate, accuracy, utilization, overhead
4. Main results: end-to-end comparison
5. Ablation: contribution of each design
6. Sensitivity analysis: parameters, workload changes, cache budget, request rate, edge conditions
7. Overhead or scalability analysis
8. Final experimental conclusion

## Related Work One-Slide Rule

When compressing Related Work into one slide:

- Group prior work into 2-4 categories.
- Explain the limitation of each category.
- End with how this paper differs from them.
- Avoid listing many paper names unless the distinction depends on them.

## Common AI Systems Terms

Preserve these terms when useful:

- KV Cache
- prefill
- decoding
- batching
- dynamic batching
- pipeline parallelism
- tensor parallelism
- model parallelism
- cache budget
- migration cost
- offloading
- scheduling
- serverless
- edge inference
- competitive ratio
- LP relaxation
- dependent rounding
- relative entropy
