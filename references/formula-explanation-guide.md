# Formula Explanation Guide

## Explanation Order

When explaining a formula, use this order:

1. State what the formula is used for.
2. Explain each variable.
3. Explain each term's system meaning.
4. Explain why the formula is designed this way.
5. Connect the formula to the algorithm, system decision, or experiment.
6. Give a simplified intuitive explanation.

## Optimization Problems

For optimization objectives and constraints, identify:

- Decision variables
- Objective function
- Constraints
- Coupling terms across time, nodes, models, requests, or cache states
- Cost terms such as latency, memory, migration, bandwidth, or compute
- Relaxation or approximation method
- How the mathematical solution maps back to real system actions

## Systems Interpretation

Do not stop at mathematical notation. Always translate math into system meaning.

Examples:

- A migration-cost term often means today's placement decision affects future movement overhead.
- A cache-budget constraint means only part of the model state or KV Cache can remain resident.
- A rounding step often converts fractional optimization results into deployable discrete decisions.
- A relative-entropy term often controls distribution shift or regularizes how far a new decision moves from a reference distribution.

## Slide-Level Formula Compression

For PPT slides:

- Show only the key formula if there are many related expressions.
- Explain variables in one compact block.
- Use speaker notes for derivation or proof intuition.
- Avoid filling a slide with all constraints unless the constraints are the main contribution.

## Missing Formula Context

If the formula is shown without surrounding text, explain the mathematical form and ask for the paper context before claiming author intent.
