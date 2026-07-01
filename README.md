# empirical-analysis

`empirical-analysis` is a Codex skill for empirical research workflows that either start from uploaded datasets or refactor existing empirical code/results into a writing-ready output package.

It is designed for users who need strict variable-name and model-design gates, standardized Stata and result exports, Markdown-first tables, and bilingual publication-quality figures generated from shared plotting data.

## What It Covers

- Uploaded dataset inspection
- Variable-name verification and confirmation
- Data cleaning and sample handling
- Descriptive statistics and correlation analysis
- Regression design and Stata code generation
- Robustness, mechanism, and heterogeneity analysis
- Output formatting for research workflows
- Result-refactor workflows that preserve legacy results while improving names, tables, and figures
- RTF and Markdown result-table export
- Project-local Python plotting environment setup
- Paired Chinese and English figure finalization from the same plotting data

## Repository Layout

- `empirical-analysis-skill/SKILL.md`: main controller for the skill
- `empirical-analysis-skill/agents/openai.yaml`: UI metadata for Codex
- `empirical-analysis-skill/references/`: modular workflow and naming rules
- `empirical-analysis-skill/scripts/`: reusable figure finalization and environment bootstrap helpers
- `skill.zip`: packaged release artifact

## Install

Copy the `empirical-analysis-skill` folder into your local Codex skills directory:

```bash
~/.codex/skills/
```

After installation, the skill name is:

```text
empirical-analysis
```

## Workflow Summary

1. Select either Full Analysis Mode or Result Refactor Mode.
2. Verify variable names and display names before analysis or regeneration.
3. Confirm the empirical model plan or legacy-result baseline.
4. Generate or refactor Stata code without changing unapproved logic.
5. Export formal RTF and Markdown tables, with Markdown as the writing source of truth.
6. Generate paired Chinese and English figures from shared plotting data in a project-local figure environment.
7. Produce a manifest and consistency audit for downstream manuscript writing.

## Release Notes

- The packaged skill is published in the GitHub Release assets as `skill.zip`.
- The repository keeps the modular skill source in sync with the release artifact.

## Source

This repository is the packaged version of the local Codex skill source for `empirical-analysis`.
