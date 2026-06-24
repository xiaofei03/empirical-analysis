---
name: empirical-analysis-skill
description: Rigorous empirical analysis workflow for Stata-based research design, code generation, and automated debugging. Use when the user wants empirical analysis support with Stata, needs panel/OLS/DID/multi-period DID/inverted-U/mediation/moderation/IV/PSM/Heckman/heterogeneity workflows, or wants an AI agent to first confirm the research blueprint, then write `.do` code, then run and self-correct through `stata-mcp`.
---

# Empirical Analysis Skill

Follow this skill when handling empirical-analysis tasks in Stata. Treat the workflow as a hard three-phase state machine. Do not skip phases.

## Phase 1: Requirement Alignment And Research Blueprint

Start here whenever the user gives a topic, model idea, paper design, variable relationship, or empirical question.

Hard rules:

1. Do not write full Stata `.do` code in this phase.
2. Ask for the minimum required information to lock the design:
   - data structure: panel/cross-section/repeated cross-section, entity id, time variable, sample period
   - sample filters: industry, region, ownership, listing status, special-year exclusions
   - dependent variable
   - key independent variable
   - control variables
   - whether variables need renaming, standardization, squared terms, lags, interactions
   - baseline model choice: FE / DID / multi-period DID / inverted-U / mediation / IV / PSM / Heckman / heterogeneity
3. Proactively ask whether to include:
   - mechanism analysis
   - robustness checks
   - endogeneity checks
   - heterogeneity analysis
4. When the user is undecided, proactively suggest common options:
   - robustness: replace X or Y, adjust sample period, drop special years, add controls, add FE dimensions, lag X, robust SE
   - endogeneity: IV, PSM or PSM-DID, placebo, Heckman
   - heterogeneity: SOE/non-SOE, firm size groups, region groups, financing constraints, competition intensity, innovation intensity
5. Do not allow vague blueprint language such as:
   - "consider doing"
   - "optionally do"
   - "if data are available"
   - "you may add one endogeneity test"
   - "you may do one heterogeneity split"
6. For every module that appears in the blueprint, force the user decision down to the variable-and-operation level before finalizing the blueprint.
   - If the blueprint includes endogeneity checks, you must ask exactly which method will be used and what the concrete implementation is, such as:
     - which IV variable
     - whether to use lagged X, and lag how many periods
     - whether to use PSM or PSM-DID
     - whether placebo will randomize DID, interaction terms, or policy year
   - If the blueprint includes heterogeneity analysis, you must ask exactly which grouping variable will be used, such as:
     - `SOE`
     - financing constraints
     - firm size
     - region
     - competition intensity
     - innovation intensity
     and whether the split is binary, tercile, quartile, median split, or another explicit rule.
   - If the blueprint includes mechanism analysis, you must ask exactly which mediator or moderator variables will be used and whether the structure is simple mediation, parallel mediation, chain mediation, or moderation.
   - If the blueprint includes robustness checks, you must ask exactly which checks will be implemented rather than leaving a generic robustness bucket.
7. You must keep drilling through multi-round dialogue until every module is specified without ambiguity. Do not stop at category labels.
8. You may generate the final blueprint only when all included modules have concrete variables, concrete procedures, and no unresolved ambiguity.

Before leaving this phase, output a clearly labeled `【最终研究设计蓝图】` that includes:

- research question
- sample and data structure
- variable setup
- baseline model
- mechanism analysis
- robustness checks
- endogeneity checks
- heterogeneity analysis
- expected outputs

End this phase by explicitly asking:

`请确认以上【最终研究设计蓝图】是否准确。只有在你回复“确认”后，我才会进入代码生成阶段。`

If the user has not explicitly replied `确认`, remain in Phase 1.

## Phase 2: Stata Code Generation

Enter this phase only after the user explicitly replies `确认`.

Your only job in this phase is to write Stata code that follows the user's confirmed blueprint and the style rules below.

Highest-priority warning: `蓝图执行契约`

Once the user has confirmed the blueprint, the generated `.do` code must implement every module promised in that blueprint with no omissions.

Hard rules:

1. If the blueprint includes heterogeneity analysis, the code must contain the agreed grouped regressions or equivalent heterogeneity implementation.
2. If the blueprint includes endogeneity checks, the code must contain the agreed IV / lag / PSM / placebo / Heckman implementation.
3. If the blueprint includes mechanism analysis, the code must contain the agreed mediation / moderation / chain-mediation structure.
4. If the blueprint includes robustness checks, the code must contain each agreed robustness specification.
5. Do not silently skip a promised module while writing code.
6. Do not downgrade a concrete agreed method into a weaker placeholder.
7. Do not replace a blueprint-locked method with another method unless the user explicitly reopens the design.

### Code Organization

Organize the `.do` file in a paper-style workflow:

1. data preprocessing
2. basic tests
3. baseline regression
4. parallel-trend test if applicable
5. placebo test if applicable
6. robustness checks
7. endogeneity checks
8. mechanism / mediation / moderation
9. heterogeneity analysis
10. further analysis if applicable
11. export tables and figures

Use strong module separators such as:

```stata
*=====================          基准回归         =====================*
```

or:

```stata
* =================================基准回归===================================
```

### Header And Environment Style

Default style:

- do not force `clear all`
- do not force `set more off`
- do not rely on `log using` as the main output system
- usually start from `cd` and data preprocessing
- clean data before `xtset`
- save intermediate datasets when useful

If the user provides an existing `.do` file and asks for enhancement rather than a full rewrite:

1. Preserve the user's existing module order, separator style, comment density, and naming style unless a change is required to make the code runnable.
2. Prefer minimal in-place augmentation such as adding export lines, adding graph-style options, or inserting safety guards.
3. Do not casually rewrite the whole file into a new house style just because another style might also be acceptable.
4. If rerun safety is uncertain, create a shadow rerun file such as `xxx_rerun.do` and keep the user's original file as intact as possible.
5. Treat style preservation as part of correctness for collaborative empirical work.

### Rich Chinese Comment Requirement

Code quality is not acceptable if it only has cold module separators.

- Before every key data-processing block, baseline regression, robustness check, mechanism test, endogeneity test, or heterogeneity test, write one or two lines of Chinese comments explaining the business logic, identification idea, or theoretical intent.
- Comments must explain why this block exists in the empirical design, not just what the syntax does.
- Bad example: `* 异质性分析`
- Good example: `* 异质性分析：按国有与非国有企业(SOE)分组回归，检验产权性质是否会改变 X 对 Y 的影响方向与显著性。`
- Good example: `* 稳健性检验：通过替换核心解释变量的构造口径，确认主结论不是由单一度量方式驱动。`
- Zero tolerance: if a key regression or key processing block appears without this kind of Chinese logic comment, treat the code as seriously under-documented and therefore non-compliant.

### Variable And Sample Handling

Preferred habits:

1. Rename Chinese or raw variable names into concise English names first.

```stata
rename 人工智能水平 AI
rename ROA1 ROA
rename TFP_FE TFP
```

2. Apply sample screening explicitly:
   - sample period
   - manufacturing filter if needed
   - ST/PT/delisted exclusion if needed
   - drop firms with only one observation if needed

3. Drop missing values with explicit `foreach` loops.

```stata
foreach i in EIR AI Size Lev Cashflow Growth TobinQ Mshare Occupy {
    drop if `i'==.
}
```

4. Winsorize continuous variables with:

```stata
winsor2 ...,cut(1 99)replace
```

Add the note:

```stata
*收尾处理（只能收尾连续型变量）
```

5. Use `egen` for grouped statistics, means, SDs, medians, percentiles, totals, and standardization inputs.
6. Use `gen` for final constructed variables, squared terms, interaction terms, dummies, DID terms, and transformed indicators.
7. Prefer explicit squared terms:

```stata
gen AIwashing_sq = AIwashing^2
gen AIdisclosure_sq = AIdisclosure*AIdisclosure
```

8. For interactions, either:

```stata
gen DID_HHI = DID * hhia
gen AI_post = AI_pre * post
```

or use factor syntax directly:

```stata
reghdfe Y c.X##c.X ...
reghdfe Y c.X##c.M ...
reghdfe Y c.X##c.X##i.group ...
```

9. Default panel setup:

```stata
xtset stkcd year
```

or:

```stata
xtset id year
```

10. If needed, clear duplicated panel keys before `xtset`:

```stata
duplicates drop stkcd year ,force
```

### Hard Rule On Variable Writing

Do not default to:

- `$y`
- `$x`
- `$controls`
- `global y`
- `global x`
- `global controls`

The default style is explicit variable lists written directly inside commands.

Correct style:

```stata
reghdfe EIR AI_post AI_pre post Size Lev Cashflow Growth TobinQ Mshare Occupy, absorb(stkcd indyear) vce(cluster stkcd)
```

Not:

```stata
reghdfe $y $x $controls, ...
```

Only allow a local control list in a very narrow temporary block when truly necessary. It must not become the dominant template of the file.

### Core Regression Preference

Highest-level ban: absolutely prohibit `xtreg` and `areg` unless the user explicitly and directly asks for them in writing. For panel fixed-effects regression, the default and only allowed main engine is `reghdfe`.

Hard rules:

- Use `reghdfe` by default for the main regression flow. Do not fall back to `xtreg`, `areg`, or softer substitutes.
- Fixed effects must be specified through `absorb(...)`, for example `absorb(id year)`.
- Clustered standard errors must be written explicitly with `vce(cluster id)` or an equivalent explicit cluster target.
- Never fake two-way fixed effects by putting `i.year` in the regressor list and then using `fe`.
- If the task involves firm, year, industry, city, province, or other absorbable fixed effects, you must use `reghdfe ..., absorb(...) vce(cluster ...)`.
- If generated code contains `xtreg`, `areg`, or the mixed pattern `i.year` plus `fe`, treat it as a serious rule violation.

Preferred progression:

```stata
reghdfe Y X
estadd local FirmFE "NO"
estadd local YearFE "NO"
est store y1

reghdfe Y X controls
estadd local FirmFE "NO"
estadd local YearFE "NO"
est store y2

reghdfe Y X controls, absorb(stkcd year) vce(cluster stkcd)
estadd local FirmFE "YES"
estadd local YearFE "YES"
est store y3
```

Common FE styles:

```stata
absorb(stkcd year)
absorb(id year)
absorb(stkcd indyear)
absorb(stkcd year industry)
absorb(id year i.ind#i.year)
```

Default clustering:

```stata
vce(cluster stkcd)
vce(cluster id)
```

Use `vce(robust)` mainly as a robustness alternative, not as the default primary specification.

### Basic Tests

If not explicitly ruled out, include:

1. descriptive statistics
2. year distribution
3. VIF
4. correlation matrix

Preferred style:

```stata
sum Y X controls
tab year
sum2docx Y X controls using 描述性统计分析.docx,replace stats(N mean median sd min max)

reg Y X controls
estat vif
logout,save(多重共线性检验)word replace:estat vif

pwcorr_a Y X controls,sig
corr2docx Y X controls using 相关性分析.docx ,star(* 0.1 ** 0.05 *** 0.01) replace pearson(pw) spearman(ignore)
```

### Output And Table Style

Use `esttab` as the main regression table tool. Store models as `y1`, `y2`, `y3`, and so on.

Strict format isolation rules:

1. Never export different analysis modules in the same `esttab` or `outreg2` command.
2. Never mix baseline regression results with mechanism, robustness, endogeneity, or heterogeneity results in one table.
3. Enforce a strict `one module -> one table file` rule.
4. After finishing `est store` for a module, immediately export that module's table before moving to the next module.
5. If needed, clear estimates or reset stored models before starting the next module so tables cannot stick together across modules.
6. After exporting the human-readable Word/RTF version of a table, immediately export the same results again as a native `.md` table file.
7. Treat table export as a dual-track requirement: every important result table must have both a human-readable office-format output and a `.md` output for downstream automation.
8. Dual-track consecutive-writing law: after one line that exports `.rtf`, the very next export line must be the matching `.md` export for the same models. Do not postpone it, skip it, or separate it by unrelated logic.
9. The `.md` export command should directly use the `.md` extension, without adding the `markdown` option, and must include `varwidth(30) modelwidth(15)` to avoid truncation.
10. When enhancing an existing paper-style `.do` file, add the matching `.md` export immediately after the original office-format export line so the surrounding writing rhythm stays unchanged.
11. If a later module reuses model names such as `y1 y2 y3`, clear estimates or reset the storage context before that module begins so old models cannot leak into the new table.
12. Zero tolerance: exporting only `.rtf` without the matching `.md` file means the result-export block is incomplete and therefore failed.

Attach FE indicators with `estadd local`, typically:

- `FirmFE`
- `YearFE`
- `IndFE`

or Chinese labels:

- `个体`
- `年份`
- `行业`

Mandatory baseline `esttab` style:

```stata
esttab y1 y2 y3 using 基准回归.rtf,nogap compress replace star(* 0.1 ** 0.05 *** 0.01) b(3) t(3) stats(FirmFE YearFE N F r2 ,star(F) fmt(0 0 0 0 3))
```

Mandatory higher-precision style for nonlinear/IV/mechanism outputs:

```stata
esttab y1 y2 y3 y4 using 稳健性检验.rtf,nogap compress replace star(* 0.1 ** 0.05 *** 0.01) b(4) t(4) stats(FirmFE YearFE IndFE N F r2 ,star(F) fmt(0 0 0 0 3 3))
```

High-frequency options:

- `nogap`
- `compress`
- `replace`
- `star(* 0.1 ** 0.05 *** 0.01)`
- `b(3)` / `b(4)`
- `t(3)` / `t(4)`
- `stats(...)`
- preserve the model-number row and dependent-variable header row in `.md` exports by default
- never use header-suppressing forms unless the user explicitly asks for them: `nomtitles`, `nonumbers`, `nodepvars`, `collabels(none)`, `mlabels(none)`
- add `mtitle(...)` whenever header stability matters or there is any risk that the dependent-variable header may be missing
- add `order(...)` when variable ordering is needed
- mandatory anti-truncation pair for Markdown exports: `varwidth(30) modelwidth(15)`

Mandatory decimal convention:

- standard FE / DID / mediation tables: use `b(3) t(3)`
- inverted-U / IV / nonlinear / mechanism-detail tables: use `b(4) t(4)`

Other allowed output tools:

```stata
sum2docx ... using 描述性统计分析.docx,replace stats(N mean median sd min max)
corr2docx ... using 相关性分析.docx ,star(* 0.1 ** 0.05 *** 0.01) replace pearson(pw) spearman(ignore)
logout,save(多重共线性检验)word replace:estat vif
outreg2 using result.doc,replace tstat bdec(4) tdec(4) ctitle(psm)
```

Mandatory output naming convention:

- descriptive statistics -> `描述性统计.docx`
- descriptive statistics markdown companion -> `描述性统计.md`
- correlation analysis -> `相关性检验.docx`
- correlation analysis markdown companion -> `相关性检验.md`
- baseline regression -> `基准回归.rtf`
- baseline regression markdown companion -> `基准回归.md`
- robustness checks -> `稳健性检验.rtf`
- robustness checks markdown companion -> `稳健性检验.md`
- mechanism analysis -> `机制分析.rtf`
- mechanism analysis markdown companion -> `机制分析.md`
- endogeneity checks -> `内生性检验.rtf`
- endogeneity checks markdown companion -> `内生性检验.md`
- heterogeneity analysis -> `异质性分析.rtf`
- heterogeneity analysis markdown companion -> `异质性分析.md`

Apply the naming convention literally unless the user explicitly requests different file names.

Mandatory module-by-module export pattern:

```stata
* 基准回归：逐步加入控制变量与固定效应，检验核心解释变量对结果变量的主效应是否稳健存在
reghdfe ...
est store y1
reghdfe ...
est store y2
reghdfe ...
est store y3
esttab y1 y2 y3 using 基准回归.rtf,nogap compress replace star(* 0.1 ** 0.05 *** 0.01) b(3) t(3) stats(FirmFE YearFE N F r2 ,star(F) fmt(0 0 0 0 3))
esttab y1 y2 y3 using 基准回归.md, replace varwidth(30) modelwidth(15) star(* 0.1 ** 0.05 *** 0.01) b(3) t(3) mtitle("CR" "CR" "CR") stats(FirmFE YearFE N F r2 ,fmt(0 0 0 0 3))

* 切换到下一模块前清空已存模型，防止不同分析模块的结果串表
est clear
```

```stata
* 稳健性检验：通过替换变量口径或样本口径，确认主结论不是由特定设定偶然驱动
reghdfe ...
est store y1
reghdfe ...
est store y2
esttab y1 y2 using 稳健性检验.rtf,nogap compress replace star(* 0.1 ** 0.05 *** 0.01) b(3) t(3) stats(FirmFE YearFE N F r2 ,star(F) fmt(0 0 0 0 3))
esttab y1 y2 using 稳健性检验.md, replace varwidth(30) modelwidth(15) star(* 0.1 ** 0.05 *** 0.01) b(3) t(3) mtitle("CR" "CR") stats(FirmFE YearFE N F r2 ,fmt(0 0 0 0 3))

est clear
```

This isolation rule is mandatory. Do not merge outputs across modules for convenience.

For descriptive statistics and correlation analysis, the same dual-track law still applies. After generating the office-format output, immediately generate a matching `.md` companion file representing the same results. If the original command does not directly support `.md` export, you must add an `esttab`-based `.md` export or another deterministic Markdown-table export step right after the office-format export so downstream automation can read the same content in `.md` form. Do not end the block with office-format output only.

At the end of Phase 2, add a dedicated export-results block that generates a file named `Result_Index.md`.

`Result_Index.md` must:

1. list all generated Markdown table files
2. list all major office-format result files when useful
3. embed all exported PNG figures using Markdown image syntax
4. use relative paths for downstream writing workflows

Preferred structure:

```markdown
# Result Index

## Tables
- [描述性统计](./描述性统计.md)
- [相关性检验](./相关性检验.md)
- [基准回归](./基准回归.md)
- [稳健性检验](./稳健性检验.md)
- [机制分析](./机制分析.md)
- [内生性检验](./内生性检验.md)
- [异质性分析](./异质性分析.md)

## Figures
![平行趋势图](./figures/平行趋势图.png)
![安慰剂检验图](./figures/安慰剂检验图.png)
```

Generate this file automatically in code rather than leaving it as a manual post-processing task.

### DID And Event-Study Style

For standard DID:

```stata
reghdfe Y DID controls,absorb(stkcd year) vce(cluster stkcd)
```

For continuous-intensity DID, prefer:

```stata
bysort stkcd: egen AI_pre_raw = mean(cond(inrange(year,2017,2019), AI, .))
bysort stkcd: replace AI_pre_raw = AI_pre_raw[1]
egen AI_pre = std(AI_pre_raw)
gen byte post = year >= 2020
gen AI_post = AI_pre * post
```

Then estimate:

```stata
reghdfe EIR AI_pre i.post AI_post Size Lev Cashflow Growth TobinQ Mshare Occupy,absorb(stkcd indyear) vce(cluster stkcd)
```

For multi-period DID / event studies:

1. build `event_time`
2. create `pre/current/post` dummies
3. omit the base period explicitly
4. set control-group missing event dummies to zero when needed

Typical style:

```stata
gen temp_policy_year = year if DID == 1
bysort stkcd: egen event_year = min(temp_policy_year)
drop temp_policy_year
gen event_time = year - event_year
```

Then:

```stata
gen d_pre_4 = (event_time <= -4)
gen d_pre_3 = (event_time == -3)
gen d_pre_2 = (event_time == -2)
gen d_current = (event_time == 0)
gen d_post_1 = (event_time == 1)
...
```

And for control-group missing values:

```stata
foreach v of varlist d_pre_* d_current d_post_* {
    replace `v' = 0 if event_time == .
}
```

### Parallel Trend And Plotting Style

When event-study logic is used, default to plotting dynamic effects.

Preferred tools:

- `coefplot`
- `margins`
- `marginsplot`

Typical `coefplot` preferences:

- vertical layout
- zero line
- policy timing separator
- connected points
- visible confidence intervals

Typical plot formatting uses `///` heavily and expands options line by line.

Every plotting block must end with an explicit high-resolution PNG export.

Hard rules:

1. After `coefplot`, `marginsplot`, `twoway`, or any other graph command, immediately run `graph export`.
2. Export figures into a relative `figures/` directory unless the user explicitly asks for another path.
3. Use PNG format and high resolution by default.
4. Prefer a pattern such as:

```stata
graph export "figures/平行趋势图.png", replace as(png) width(2000)
```

5. Apply the same rule to inverted-U plots, moderation plots, placebo plots, heterogeneity comparison plots, and any other generated figure.

### Stata Figure Styling And Export Rules

Treat figure generation as a first-class deliverable rather than cosmetic cleanup.

Default styling stack:

1. use `schemepack` to set one coherent base scheme for the whole project
2. use `grstyle` to override background, grid, line width, legend, and text details when needed
3. use `palettes` and `colrspace` when custom colors or color-safe sequences are needed
4. use graph-specific commands such as `coefplot`, `marginsplot`, `eventdd`, `binsreg`, and `twoway` to match the statistical task

Hard rules:

1. Do not mix multiple unrelated visual styles in one paper. Once a project-level scheme is chosen, keep all main-text figures on the same scheme unless a strong reason is documented.
2. Prefer white or very light backgrounds, restrained gridlines, and high-contrast axes. Avoid dark backgrounds, decorative gradients, and saturated rainbow palettes.
3. Prefer short titles, explicit axis labels, and concise notes. Put variable definitions, sample restrictions, and estimation details in `note()` or the paper text rather than overloading the title.
4. Prefer one emphasis color plus neutral support colors. Do not assign a new bright color to every series unless categories truly need separate identities.
5. When confidence intervals are plotted, make them clearly visible but visually secondary to the point estimate. Prefer capped spikes, thin interval lines, or light shaded bands rather than thick opaque intervals.
6. Always think in final output size. A figure that looks acceptable in the Graph window may become unreadable after it is inserted into Word or LaTeX.
7. For bilingual figures on Windows, default to `Times New Roman` for English text and `SimSun` for Chinese text unless the user explicitly requests another typography standard.

Preferred package usage:

- `schemepack`: use it to improve the default visual baseline before graph-specific tuning begins
- `grstyle`: use it for project-level standardization of background, grid, margins, legend region, symbol size, and line thickness
- `palettes` and `colrspace`: use them when the paper needs a controlled color sequence instead of ad hoc named colors
- `coefplot`: default tool for coefficient plots, event-study coefficient paths, subgroup comparison plots, and many heterogeneity visualizations
- `margins` plus `marginsplot`: default tool for nonlinear effects, adjusted predictions, and interaction visualization
- `eventdd`: preferred packaged workflow for panel event-study estimation plus plotting when the design truly is an event-study design
- `binsreg` or `binscatter2`: preferred tools for binned scatter visualizations; prefer `binsreg` when inference, data-driven bin choice, or confidence bands are substantively important

Project-level figure defaults:

1. At the start of the figure section, check whether required graph packages are available using commands such as `cap which coefplot` and `cap which grstyle`.
2. If `schemepack` is installed, set the scheme once near the beginning of the figure block rather than repeating it before each graph.
3. If a graph still looks crowded after setting the scheme, adjust it with `grstyle` or graph-specific options instead of switching schemes repeatedly.
4. Prefer vector export for final manuscript figures when the destination supports it, especially `pdf` or `svg`; also export a high-resolution `png` copy for preview, markdown reports, or Word workflows.
5. Use stable filenames and consistent naming conventions such as `figures/baseline_coefplot.pdf`, `figures/event_study.png`, or `figures/margins_interaction.svg`.
6. When the figure contains Chinese text, prefer `pdf` plus high-resolution `png` as the default export pair. Do not default to `ps` or `eps` for Chinese figures.

Typography defaults for Stata graphs on Windows:

1. Set the English default font to `Times New Roman` at the beginning of the graph block using `graph set`.
2. When Chinese text appears in titles, notes, axis labels, or legend labels, explicitly wrap the Chinese text with `fontface "SimSun"` rather than assuming automatic bilingual font switching.
3. Keep English variable names, English axis text, and numeric labels in `Times New Roman` unless the user requests full-Chinese typography.
4. Keep Chinese explanatory notes concise because long Chinese text blocks are more likely to crowd the figure region.
5. If a figure is fully in English, there is no need to inject Chinese font markup.
6. Never assume a scheme such as `qlean`, `s1mono`, or `schemepack` will automatically produce the user's requested Chinese font. Scheme choice and Chinese font control are separate tasks.
7. On Windows, if the user explicitly wants Songti-style Chinese output, treat `SimSun` as mandatory: wrap Chinese substrings with `SimSun`, and if the user wants all visible text harmonized, set the graph default font itself to `SimSun`.
8. If the graph mixes English variable names with Chinese explanatory text, keep the English text in the default English font and wrap only the Chinese substrings with `SimSun`.
9. After exporting at least one key Chinese figure, visually verify that the Chinese glyphs are actually in the requested family rather than merely non-garbled.

Recommended bilingual font template:

```stata
graph set window fontface "Times New Roman"
graph set pdf    fontface "Times New Roman"
graph set svg    fontface "Times New Roman"

* Explicitly set Chinese text to SimSun so English text and numerals stay in Times New Roman
title(`"{fontface "SimSun":基准回归结果}"')
xtitle(`"{fontface "Times New Roman":Year}"')
ytitle(`"{fontface "SimSun":估计系数}"')
note(`"{fontface "SimSun":注：标准误按企业层面聚类。}"')
```

Recommended full-Chinese typography template when the user explicitly wants uniform Songti output:

```stata
graph set window fontface "SimSun"
graph set pdf    fontface "SimSun"
graph set svg    fontface "SimSun"

ytitle(`"{fontface "SimSun":企业韧性（CR）预测值}"')
legend(label(1 `"{fontface "SimSun":处理组}"') label(2 `"{fontface "SimSun":控制组}"'))
b1title(`"{fontface "SimSun":异质性对比图}"')
```

Default aesthetic preferences by graph family:

- coefficient plots: vertical layout, zero reference line, ordered coefficients, visually light confidence intervals, legend off unless multiple models are compared
- event-study plots: explicit event-time axis, clear baseline omission, zero line, policy timing marker, symmetric or substantively justified windows, and readable lead-lag labels
- margins plots: prefer `recast(line)` for continuous x-axes and `recastci(rarea)` or light interval lines when the interaction pattern matters more than individual markers
- binscatter or binsreg plots: separate the binned means from the fitted relationship clearly; do not use too many bins just to create a smooth-looking line
- grouped bar or mean comparison plots: use only when direct level comparison is the goal; keep bar counts limited and labels short

Detailed graph-family rules:

1. `coefplot`
   - Prefer `vertical` for event-study style or ordered coefficient displays.
   - Prefer a zero line such as `xline(0)` or `yline(0)` depending on orientation.
   - Use `keep()` or `drop()` aggressively so that only substantively relevant coefficients remain.
   - When plotting multiple models, make the comparison logic explicit by ordering models consistently and avoiding overloaded legends.
   - Prefer `ciopts()` to keep confidence intervals lighter than points or lines.

2. `margins` and `marginsplot`
   - Use `margins` to generate predictions, marginal effects, or contrasts after the correct fitted model rather than hand-computing fitted values when not necessary.
   - For continuous moderators or nonlinear terms, define a substantively meaningful evaluation grid in `at()`.
   - Prefer `marginsplot, recast(line)` for continuous x-axes and use `recastci(rarea)` only when the shaded interval improves readability.
   - When the graph is categorical, `recast(bar)` is acceptable, but do not default to bars if a profile line communicates the pattern more clearly.

3. `eventdd`
   - Prefer `eventdd` when the project uses a formal panel event-study design and the user wants estimation plus plotting in one workflow.
   - Use graph options to align the output with the project scheme rather than accepting the untouched default graph.
   - Make the omitted baseline period explicit in the surrounding comments and figure note.
   - Keep the event window interpretable; trimming extreme leads or lags is acceptable when justified and disclosed.

4. `binsreg` and `binscatter2`
   - Prefer `binsreg` when the figure is used as evidence rather than illustration, because it supports principled bin selection, inference, and confidence bands.
   - Use `binscatter2` for quick exploratory visuals when the project only needs a lighter descriptive graph.
   - Do not present a binscatter as if it were a fully nonparametric truth object; explain controls, residualization, and binning choices in comments or notes.

Figure-writing discipline:

1. Before each important graph block, add one or two Chinese comments explaining what the figure is meant to show in the empirical argument.
2. Do not output a graph without a corresponding sentence in the surrounding comments that explains why the graph exists.
3. If the graph is for the main text, prefer a cleaner and more conservative style than for appendix exploration.
4. If the graph supports a formal claim, ensure the code that produces the graph is reproducible from estimation results rather than manual spreadsheet edits.

Default export discipline:

1. For manuscript-quality output, export at least one vector file such as `pdf` or `svg` when supported by the downstream workflow.
2. Also export one high-resolution `png` copy for quick inspection and markdown embedding.
3. When using raster export, specify width or height explicitly rather than relying on a small default image.
4. If multiple graphs are open, use graph names carefully before export so that the wrong figure is not written out.
5. Save the graph command block and the export command block together so later reruns cannot regenerate the figure but forget to overwrite the file.
6. If the figure contains Chinese text, prefer `graph export "...pdf"` and `graph export "...png", width(2400)` as the default pair.
7. When a manuscript workflow only needs raster output, still set an explicit large width such as `2400` or `3200` so reruns do not silently downgrade image quality.
8. After a graph command that uses many `///` continuation lines, do not place inline `//` comments on the same continued option lines because they can break the continuation logic in Stata; if labels are long and bilingual, keep them concise rather than stacking fragile options into one command.

When the user asks for figures, the generated `.do` code should not stop at estimation. It should actively decide which plotting command family is the best fit, apply a coherent style layer, and export presentation-ready figures by default.

### Inverted-U And Moderation Style

Default inverted-U model:

```stata
reghdfe Y X X_sq controls, absorb(id year) vce(cluster id)
```

If formally testing the U-shape, prefer:

```stata
utest X X_sq
```

For plotting:

1. summarize X
2. get min and max
3. compute turning point `-b1/(2*b2)`
4. use `margins`
5. use `marginsplot`

For moderation:

- either explicit interaction variables
- or factor syntax like `c.X##c.M`

For nonlinear moderation, prefer:

```stata
reghdfe Y c.X##c.X##c.M controls, absorb(...) vce(cluster ...)
```

### Mediation, Parallel Mediation, Chain Mediation

Standard mediation default:

```stata
reghdfe Y X controls, absorb(...) vce(cluster ...)
reghdfe M X controls, absorb(...) vce(cluster ...)
reghdfe Y X M controls, absorb(...) vce(cluster ...)
```

Use `bootstrap: sgmediation` when appropriate:

```stata
bootstrap r(ind_eff)r(dir_eff),reps(500):sgmediation Y, mv(M) iv(X) cv(controls)
```

For chain mediation, prefer the path logic:

1. `X -> Y`
2. `X -> M1`
3. `X + M1 -> M2`
4. `X + M1 + M2 -> Y`

If needed, define a custom `program ..., rclass` to calculate direct, indirect, chain, and total indirect effects.

### Robustness, Endogeneity, And Heterogeneity

Default robustness menu:

- replace X
- replace Y
- adjust sample period
- drop special years
- add controls
- add FE dimensions
- lag X
- robust SE

Default endogeneity menu:

- `ivreghdfe`
- PSM / PSM-DID
- placebo with `permute`
- Heckman two-step

Preferred IV style:

```stata
ivreghdfe Y (X = IV) controls, absorb(stkcd year) first
```

Preferred PSM flow:

1. build treatment
2. `set seed`
3. `gen runiform()`
4. `sort`
5. `psmatch2`
6. `pstest`
7. matched-sample regression

Common heterogeneity cuts:

- SOE vs non-SOE
- firm size terciles
- east/mid/west
- financing constraints
- competition intensity
- innovation intensity

Firm size tercile style:

```stata
bys year:egen size33=pctile(Size),p(33)
bys year:egen size66=pctile(Size),p(66)
gen Size三分组=1 if Size<=size33
replace Size三分组=2 if Size<=size66&Size>size33
replace Size三分组=3 if Size>size66
```

### Formatting Rules

1. Use `///` for long commands.
2. Indent loop bodies.
3. Expand plot options line by line.
4. Keep comments tied to research logic and step numbering.

## Phase 3: Automated Execution And Self-Correction

After generating code, immediately enter this phase.

Hard rules:

1. Run the generated Stata code through `stata-mcp` or the available Stata execution path.
2. Do not ask the user whether to run it. Run it by default.
3. If Stata returns an error log, do not push the error back to the user immediately.
4. First inspect:
   - line number
   - syntax errors
   - missing variables
   - missing files
   - uninstalled commands
   - FE conflicts
   - duplicate panel keys
   - sample-empty issues
   - graph-option failures
   - export-path issues
5. Fix the code yourself and rerun.
6. Continue the read-error -> patch -> rerun loop until:
   - the code succeeds, or
   - the task is blocked by missing data, missing files, or unresolved contradictions that cannot be inferred safely
7. Before the first rerun, do a preflight check of the actual local data and file environment rather than assuming the original `.do` still matches the current workspace.
8. If the original `.do` depends on upstream merge steps, old relative paths, or a preloaded in-memory dataset that is no longer present, inspect the real available `.dta` files and reconstruct the safest rerun entry point instead of retrying blindly.
9. When the user asks not to change data or empirical results, restrict fixes to execution-layer repairs such as path correction, export augmentation, duplicate temporary-variable cleanup, graph styling, syntax repair, or optional skipping of user-approved costly steps such as `bootstrap`.
10. Prefer `capture drop` for temporary variables that may already exist across reruns so the rerun loop is idempotent.
11. For Stata-MCP work, keep a readable plain-text log inspection path in mind; if the packaged error summary is too thin, inspect the full text log and focus on the exact failing block before patching.
12. Treat graph errors, font mismatches, and export omissions as first-class execution failures, not cosmetic afterthoughts, when the user explicitly asked for polished output.

Only ask the user follow-up questions when a real external blocker exists, such as:

- required dataset missing
- required variable completely absent with no plausible alias
- logically incompatible design choices
- required external file missing and not reconstructible

If the problem is just syntax, command installation, FE specification, plotting options, temporary macros, or path formatting, repair it yourself.

Recommended preflight checklist before the first Stata rerun:

1. Confirm which dataset file actually exists locally and whether it already contains derived variables needed by the downstream models.
2. Confirm whether the original `.do` assumes prior in-memory state, prior merges, or hand-prepared temporary variables.
3. Confirm whether the export directory already exists and whether filenames should be overwritten.
4. Confirm whether the graph section contains Chinese text and therefore needs explicit `SimSun` handling, and whether any long graph command mixes `///` with inline comments that could break parsing.
5. Confirm whether third-party commands such as `reghdfe`, `esttab`, `winsor2`, `psmatch2`, `sgmediation`, `sum2docx`, or `corr2docx` are available before blaming the model logic.

At the end, report succinctly:

- which files were generated
- whether the run succeeded
- whether auto-fixes were applied
- which tables or figures were produced

## Final Discipline

Always do research design first, code second, execution third.

Always require blueprint confirmation before code generation.

Always follow the user's explicit-variable Stata style.

Always use `reghdfe` as the main regression engine unless the user explicitly requires a different command.

Always write reproducible, paper-ready, modular Stata code.

Always run and self-correct before handing work back.
