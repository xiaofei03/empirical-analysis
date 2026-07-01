# Empirical Analysis Skill

This skill supports two empirical-analysis modes:

- `Full Analysis Mode`: build an empirical analysis from uploaded or raw data.
- `Result Refactor Mode`: standardize existing do-files, outputs, variable labels, tables, and figures without changing the empirical logic.

## Formal Output Philosophy

The goal is a writing-ready result package, not only a set of regression outputs.

Formal empirical delivery should include:

- confirmed variable-name map
- confirmed display-name map
- confirmed empirical model plan
- Stata do-files
- RTF result tables
- Markdown result tables
- plotting data
- paired Chinese and English final figures when bilingual manuscripts are maintained
- result manifest
- consistency audit

Markdown tables are the manuscript-writing source of truth.

## Bilingual Figure Workflow

For final manuscript figures, use this route by default:

```text
Stata model estimation
  -> exported margins / predictions / coefficients / plotting data
  -> Python final plotting
  -> Chinese figure + English figure from the same plotting data
  -> consistency audit
```

Stata graphs are useful as a benchmark, but Python should normally own final typography and layout.

Paired bilingual figures are required from the first formal figure pass. Do not create a Chinese figure first and later crop, copy, or relabel it into an English figure.

## Figure Environment Bootstrap

For reusable publication-quality figure generation, use a project-local isolated environment:

```bash
python3 "$HOME/.codex/skills/empirical-analysis-skill/scripts/bootstrap_figure_env.py" \
  --project-root "<paper-project>" \
  --env-name .venv_figures
```

The helper creates or verifies a local plotting environment, installs/checks core plotting dependencies, and writes a manifest with:

- Python executable
- package versions
- resolved Chinese font candidates
- resolved English font candidates
- recommended `.gitignore` entry

Default output layout:

```text
figures/
├── data/<figure_id>_plotdata.csv
├── cn/<figure_id>_cn.png
├── en/<figure_id>_en.png
├── config/<figure_id>_labels.json
└── manifest/figure_manifest.md
```

The isolated environment should be excluded from Git. It solves the recurring problem where one project can draw correctly only because of a hidden local Python/font state.

Chinese figures:

- Chinese labels
- Songti/SimSun/STSong-style font
- no garbled Chinese glyphs

English figures:

- English labels
- Times New Roman
- no Chinese text inside figure

Both variants must share the same empirical geometry:

- same plotting data
- same curve and points
- same confidence intervals
- same axis ranges
- same tick positions
- same legend order

Failure conditions:

- English figures contain any Chinese visible text
- figures use raw variable names, underscores, or numeric suffixes
- paired figures come from different data or model logic
- a font silently falls back to an unintended family
- output files use ambiguous names rather than stable paired names

## Robustness Figure Case

If the Stata code did not originally produce a graph, such as an overlaid robustness curve, Python may generate the figure from the confirmed robustness specifications.

The project-specific plotting script must record:

- dataset path
- model list
- sample filters
- dependent variables
- independent variables
- controls
- prediction grid
- whether predictions are normalized
- consistency checks against the robustness table

The final figure must still be paired:

- `figures/cn/robustness_curve_cn.png`
- `figures/en/robustness_curve_en.png`

## Companion Template

Use `scripts/bilingual_figure_template.py` as a generic line-figure finalizer when plotting data already exist.

Example:

```bash
python3 scripts/bilingual_figure_template.py \
  --plot-data figures/data/robustness_curve_plotdata.csv \
  --label-config figures/config/robustness_curve_labels.json \
  --output figures/cn/robustness_curve_cn.png \
  --lang cn \
  --x-col x \
  --y-col y \
  --group-col model

python3 scripts/bilingual_figure_template.py \
  --plot-data figures/data/robustness_curve_plotdata.csv \
  --label-config figures/config/robustness_curve_labels.json \
  --output figures/en/robustness_curve_en.png \
  --lang en \
  --x-col x \
  --y-col y \
  --group-col model
```

Project-specific scripts may still compute plotting data, but they should keep final language/font/layout rules aligned with this template.
