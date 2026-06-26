---
name: empirical-analysis
description: Dual-mode empirical research workflow for either full end-to-end analysis from uploaded data or refactoring and standardizing existing empirical results, including variable-name confirmation, empirical-design confirmation, standardized Stata do-file generation, consistency-checked result export, English-only figure finalization, and Markdown-first output packaging for downstream paper writing.
---

# Empirical Analysis Skill

Use this skill for empirical research workflows that either:

1. start from uploaded data and build a full empirical analysis from 0 to 1, or
2. start from existing do-files, legacy result tables, manuscript tables, or prior outputs and standardize or refactor them without losing result traceability.

The formal goal of this skill is not merely to run regressions. The formal goal is to generate a writing-ready empirical result package whose variable names are standardized, whose tables and figures are format-consistent, whose output logic is traceable, and whose result source is explicitly documented.

## Operating Modes

This skill supports two execution modes:

### Mode A. Full Analysis Mode

Use this mode when the user wants end-to-end empirical analysis from raw or newly uploaded data.

Typical triggers:

- upload data and start empirical analysis
- run descriptive statistics and regressions from scratch
- build robustness, mechanism, moderation, heterogeneity, or endogeneity modules from the beginning

### Mode B. Result Refactor Mode

Use this mode when the user already has existing do-files, result tables, manuscript tables, figures, or prior outputs and wants to:

- rename variables
- standardize display names
- regenerate formal do-files
- export standardized rtf and markdown result tables
- standardize figures
- align legacy results with current writing materials

Typical triggers:

- modify variable names without changing logic
- preserve legacy empirical results while improving output format
- synchronize old results, manuscript tables, and new markdown exports
- ensure writing uses a standardized result source

## Mode Selection Rule

Choose the mode before doing substantive analysis work.

- If the user mainly provides uploaded data and asks to start or continue analysis, default to `Full Analysis Mode`.
- If the user mainly provides existing do-files, result files, manuscript tables, or asks to rename variables, standardize outputs, or preserve existing numerical results, default to `Result Refactor Mode`.
- If both are present, identify the primary goal first and state which mode is being used.

## Full Analysis Workflow

Treat `Full Analysis Mode` as a hard six-stage workflow:

1. Variable names and empirical design confirmation
2. Data structure, missingness, outliers, and sample handling
3. Descriptive statistics, correlation, and basic visualization
4. Baseline regression, model specification, and result interpretation
5. Robustness, mechanism, heterogeneity, and extensions
6. Formal export and output packaging

Stage 1 is a hard gate. If the user uploads data, all analysis must start there. No cleaning, statistics, plots, regression, interpretation, or table export may begin before Stage 1 is fully complete.

## Result Refactor Workflow

Treat `Result Refactor Mode` as a hard six-stage workflow:

1. Variable-name and display-name confirmation
2. Legacy-result baseline confirmation
3. Existing code, result, and manuscript audit
4. Standardized do-file regeneration
5. Standardized result-table, markdown, and figure regeneration
6. Consistency audit and writing-ready packaging

In this mode, legacy-result baseline confirmation is a hard gate. No formal standardized export may begin until the baseline source has been explicitly identified.

## Stage 1 Hard Gate In Full Analysis Mode

Stage 1 has two mandatory substeps:

1A. Variable name verification and confirmation
1B. Empirical analysis plan confirmation

### 1A. Variable Name Verification And Confirmation

1. Read and list raw variable names first.
2. Verify names against the naming rules in [Variable Naming Rules](references/variable-naming-rules.md).
3. Use [Variable Naming Reference](references/variable-naming-reference.md) only as meaning-and-measurement guidance.
4. If any name is noncompliant, stop and produce a `变量名称修改建议表`.
5. Do not rename anything until the user explicitly confirms the suggestion table.
6. After renaming, output both:
   - `最终变量名对照表`
   - `结果展示名对照表`
7. Do not move to 1B until 1A is complete.

This skill distinguishes three layers:

- raw variable name
- analysis variable name
- display variable name

The analysis variable name is the formal dataset and code variable name.
The display variable name is the formal table, figure, and manuscript display name.

### 1B. Empirical Analysis Plan Confirmation

1. After 1A is complete, do not start cleaning, descriptive statistics, regression, or visualization yet.
2. Confirm the empirical analysis plan with the user.
3. At minimum, confirm:
   - dependent variable
   - core independent variable
   - control variables
   - mediator, moderator, or mechanism variables if any
   - heterogeneity grouping variables if any
   - panel entity dimension and time dimension
   - whether fixed effects are used
   - clustering level for standard errors
   - baseline regression model
   - whether robustness checks, mechanism tests, and heterogeneity analysis are needed
4. If the user has already provided this information, organize it into a `实证分析方案确认表` and ask for confirmation.
5. If information is incomplete, ask targeted questions to fill the gaps before drafting the confirmation table.
6. The user must explicitly confirm the plan before Stage 2 may begin.

If any name is noncompliant, stop and produce a `变量名称修改建议表`.
If the empirical design is not fully specified, stop and request the missing information.
Only when 1A and 1B are both complete may Stage 2 begin.

If all names already comply, output exactly:

`变量名称已通过规范化核验：未发现下划线、数字、中文变量名、特殊符号或明显不统一命名。可以进入第二阶段的数据结构与清洗处理。`

Note: digit checks apply to actual dataset variable names and newly generated variable names, not to superscript digits used in formulas, model notation, or paper presentation. Normalized academic casing such as `AI`, `ROA`, `AIwashing`, or `TobinQ` is allowed for actual variable names.

## Stage R1 Hard Gate In Result Refactor Mode

The assistant must first confirm:

- raw variable names
- current analysis variable names
- current display variable names if they already exist
- target analysis variable names
- target display variable names

Required outputs:

- `变量名称修改建议表`
- `最终变量名对照表`
- `结果展示名对照表`

Do not regenerate formal outputs before this confirmation is complete.

## Stage R2 Hard Gate In Result Refactor Mode

The assistant must explicitly confirm the legacy result baseline before refactoring outputs.

Possible baseline sources include:

- current do-file
- current dataset
- legacy result files
- manuscript-embedded tables
- user-specified benchmark output

If these sources conflict, output `结果口径差异确认表` and wait for confirmation before formal regeneration.

This baseline confirmation is mandatory only in `Result Refactor Mode`, not in `Full Analysis Mode`.

## Legacy Drift Rule

Legacy drift occurs when the current do-file, current dataset, prior result files, manuscript tables, or user-declared benchmark outputs do not align.

When legacy drift is detected:

1. stop formal export
2. output `结果口径差异确认表`
3. state which source currently conflicts with which
4. ask the user to confirm which source is the formal baseline

Do not assume that the current do-file is the true source of the current result tables.

## Markdown-First Rule

Markdown is the only formal table source for downstream manuscript writing.

- formal empirical tables must be exported to both `rtf` and `markdown`
- `markdown` is the writing-source truth
- `rtf` is a parallel formatting artifact, not the writing-source truth
- if `rtf` and `markdown` conflict, the assistant must stop and perform a consistency audit

## Figure Final Rule

Final empirical figures must satisfy all of the following:

- all visible text must be English only
- the font must be Times New Roman
- no Chinese title, axis label, legend, annotation, or caption is allowed inside the final figure
- no raw variable names with underscores or numeric suffixes are allowed in the final figure
- final figures must be traceable to the corresponding result table or exported plotting data

Preferred route:

- Stata computes and exports values
- Python handles final plotting and layout

Do not treat a raw Stata graph as a final deliverable by default.

For detailed final-figure requirements, read [Figure Final Rules](references/figure-final-rules.md) whenever figures are part of the requested deliverable.

## Formal Deliverable Rule

Every formal empirical delivery must include, when applicable:

- master do-file
- module-specific do-files
- standardized `rtf` tables
- standardized `markdown` tables
- figure source files or exported plotting data
- final English-only figure files
- `result_manifest`
- `consistency_check`

The manifest must state:

- which dataset was used
- which do-file generated each table or figure
- which sample definition was used
- whether the output was generated from current code or synchronized from a legacy baseline
- whether consistency audit passed

## Final Consistency Audit Rule

Before declaring outputs formal and writing-ready, perform a consistency audit.

At minimum, check:

- sample size
- coefficient values
- t statistics or z statistics
- significance markers
- dependent-variable labels
- control-variable labels
- figure labels
- whether display names match the display-name map

If mismatches exist, output `结果差异核查表` and do not silently proceed.

## Reference Loading

Load these files as needed, one level deep from this file:

- [Variable Naming Rules](references/variable-naming-rules.md)
- [Variable Naming Reference](references/variable-naming-reference.md)
- [Empirical Analysis Plan Rules](references/empirical-analysis-plan-rules.md)
- [Data Cleaning Rules](references/data-cleaning-rules.md)
- [Empirical Modeling Rules](references/empirical-modeling-rules.md)
- [Output Format Rules](references/output-format-rules.md)
- [Figure Final Rules](references/figure-final-rules.md)

## Non-Negotiable Enforcement

- All analysis entry points must choose the operating mode first.
- Stage 1A and 1B are both required before later stages in `Full Analysis Mode`.
- Stage R1 and R2 are both required before formal regeneration in `Result Refactor Mode`.
- User confirmation is required before renaming.
- No later-stage analysis may proceed while variable names or the empirical design are unresolved.
- No formal result refactor may proceed while the legacy baseline is unresolved.
- When a blueprint is confirmed, the generated code must implement every promised module.
- Use explicit variable lists rather than global shortcuts.
- Write Chinese logic comments before every key empirical block in Stata code.
- Formal figures must be English-only and Times New Roman.
- Formal tables must include markdown exports.
- Markdown is the only formal table source for downstream paper writing.
