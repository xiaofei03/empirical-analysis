---
name: empirical-analysis
description: Rigorous empirical research workflow for uploaded datasets, variable-name verification and confirmation, data cleaning, regression design, Stata code generation, and iterative empirical analysis including robustness, mechanism, and heterogeneity checks.
---

# Empirical Analysis Skill

Use this skill for empirical research workflows that start from uploaded datasets and move through variable-name verification, data preparation, model design, Stata code generation, and empirical analysis.

## Mandatory Workflow

Treat the workflow as a hard five-stage state machine:

1. Variable name verification and confirmation
2. Data structure, missingness, outliers, and sample handling
3. Descriptive statistics, correlation, and basic visualization
4. Baseline regression, model specification, and result interpretation
5. Robustness, mechanism, heterogeneity, and extensions

Stage 1 is a hard gate. If the user uploads data, all analysis must start there. No cleaning, statistics, plots, regression, interpretation, or table export may begin before Stage 1 is completed and the user has confirmed any required renaming.

## Stage 1 Hard Gate

1. Read and list raw variable names first.
2. Verify names against the naming rules in [Variable Naming Rules](references/variable-naming-rules.md).
3. Use [Variable Naming Reference](references/variable-naming-reference.md) only as meaning-and-measurement guidance.
4. If any name is noncompliant, stop and produce a `变量名称修改建议表`.
5. Do not rename anything until the user explicitly confirms the suggestion table.
6. After renaming, output a `最终变量名对照表`.
7. Only then may Stage 2 begin.
8. If all names already comply, output exactly this conclusion and continue:

`变量名称已通过规范化核验：未发现下划线、数字、中文变量名、特殊符号或明显不统一命名。可以进入第二阶段的数据结构与清洗处理。`

Note: digit checks apply to actual dataset variable names and newly generated variable names, not to superscript digits used in formulas, model notation, or paper presentation.

## Reference Loading

Load these files as needed, one level deep from this file:

- [Variable Naming Rules](references/variable-naming-rules.md)
- [Variable Naming Reference](references/variable-naming-reference.md)
- [Data Cleaning Rules](references/data-cleaning-rules.md)
- [Empirical Modeling Rules](references/empirical-modeling-rules.md)
- [Output Format Rules](references/output-format-rules.md)

## Non-Negotiable Enforcement

- All analysis entry points must honor Stage 1 before any later stage.
- User confirmation is required before renaming.
- No later-stage analysis may proceed while variable names are unresolved.
- When a blueprint is confirmed, the generated code must implement every promised module.
- Use explicit variable lists rather than global shortcuts.
- Write Chinese logic comments before every key empirical block.
