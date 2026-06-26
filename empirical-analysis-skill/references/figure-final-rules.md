# Figure Final Rules

## Purpose

This file governs the final stage of empirical figure production.

The goal is not merely to produce a readable figure. The goal is to produce a writing-ready figure whose language, font, variable labels, and visual cleanliness are suitable for direct downstream manuscript use.

## Final Figure Standard

Every final empirical figure must satisfy all of the following:

- all visible text is English only
- all visible text uses Times New Roman
- no Chinese title, subtitle, axis label, legend, annotation, note, or caption appears inside the figure
- no raw variable name with underscores appears inside the figure
- no numeric-suffix raw variable name such as `ROA1`, `Balance1`, or `AIwashing_sq` appears inside the figure
- the displayed labels must follow the confirmed `结果展示名对照表`
- axis tick labels must not overlap
- legends must not overlap the plotted content
- the final figure must match the corresponding regression or exported plotting data

## Preferred Workflow

Preferred route:

1. Stata estimates the model
2. Stata exports margins, predictions, coefficients, or plotting data
3. Python generates the final figure

Do not treat a raw Stata graph as the default final deliverable.

## Language Rule

Use English-only wording for:

- title
- axis titles
- legend labels
- annotation labels
- note text inside figures

Examples:

- use `AI Washing` rather than `AIwashing`
- use `AI Washing Squared` rather than `AIwashing_sq`
- use `Resilience` rather than `CR`
- use `Trade Credit` rather than `TCF`
- use `Agency Cost` rather than `AC1`

## Font Rule

- final exported figures must use Times New Roman
- if Python is used, explicitly set the font family rather than relying on system defaults
- if a font fallback occurs, the assistant must detect it and fix it before declaring the figure final

## Figure Naming Rule

Use stable English file names for final figures.

Recommended examples:

- `baseline_curve_final.png`
- `robustness_curve_final.png`
- `moderation_main_final.png`
- `moderation_trade_credit_final.png`
- `heterogeneity_rd_final.png`
- `heterogeneity_constraint_final.png`
- `heterogeneity_region_final.png`
- `psm_density_final.png`
- `psm_balance_final.png`

Avoid:

- Chinese file names
- temporary names such as `a1.png`, `result.png`, `new.png`
- mixed naming styles

## Required Figure Inputs

Before drawing a final figure, confirm:

- which regression result it corresponds to
- which sample it uses
- which variable display names it should use
- whether the plotted values come from the current run or a legacy baseline

If the figure source is ambiguous, stop and trigger legacy drift confirmation.

## Figure Self-Check

Before final export, the assistant must check:

- English-only text
- Times New Roman text
- no overlapping tick labels
- no legend overlap
- no Chinese inside figure
- no raw code variable names
- consistent line styles and color labels
- consistency with the corresponding table or exported plotting data

## Figure Consistency Audit Output

If figure finalization is part of a formal delivery, record at least:

- figure file name
- data source
- model source
- whether labels match the display-name map
- whether font requirement passed
- whether English-only requirement passed
- whether overlap check passed

## Failure Rule

Do not declare a figure final if:

- the figure still contains Chinese text
- the font is not Times New Roman
- the axis labels overlap
- the legend overlaps
- the labels do not match the display-name map
- the curve or points cannot be traced back to a confirmed result source
