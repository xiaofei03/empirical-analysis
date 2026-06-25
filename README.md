# empirical-analysis

`empirical-analysis` is a Codex skill for empirical research workflows that start from uploaded datasets and move through variable-name verification, data preparation, regression design, Stata code generation, and empirical analysis.

It is designed for users who need a strict first-stage variable-name hard gate before any cleaning, modeling, robustness testing, mechanism analysis, or heterogeneity analysis begins.

## What It Covers

- Uploaded dataset inspection
- Variable-name verification and confirmation
- Data cleaning and sample handling
- Descriptive statistics and correlation analysis
- Regression design and Stata code generation
- Robustness, mechanism, and heterogeneity analysis
- Output formatting for research workflows

## Repository Layout

- `empirical-analysis-skill/SKILL.md`: main controller for the skill
- `empirical-analysis-skill/agents/openai.yaml`: UI metadata for Codex
- `empirical-analysis-skill/references/`: modular workflow and naming rules
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

1. Verify dataset variable names.
2. Present a rename suggestion table if needed.
3. Wait for user confirmation before renaming.
4. Proceed to cleaning, statistics, modeling, and analysis only after the Stage 1 gate is cleared.
5. Generate Stata code and empirical outputs according to the confirmed blueprint.

## Release Notes

- The packaged skill is published in the GitHub Release assets as `skill.zip`.
- The repository keeps the modular skill source in sync with the release artifact.

## Source

This repository is the packaged version of the local Codex skill source for `empirical-analysis`.
