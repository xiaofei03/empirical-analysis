# Empirical Modeling Rules

## Workflow Order

After Stage 3, use this order when the blueprint has been confirmed:

1. baseline regression
2. parallel-trend test if applicable
3. placebo test if applicable
4. robustness checks
5. endogeneity checks
6. mechanism / mediation / moderation
7. heterogeneity analysis
8. further analysis if applicable

## Hard Rules

- Do not write full Stata `.do` code before blueprint confirmation.
- The model choice must be concrete: FE, DID, multi-period DID, inverted-U, mediation, IV, PSM, Heckman, or heterogeneity.
- If a module is in the blueprint, the code must implement it exactly.
- Do not silently skip promised modules.
- Do not downgrade a concrete agreed method into a placeholder.
- Use explicit variable lists rather than global shortcuts.
- Write Chinese logic comments before every key empirical block.

## Coding Preferences

- Prefer concise variable names first; rename raw names before modeling.
- Use strong module separators.
- Use explicit squared terms.
- Use explicit interaction terms or clear factor syntax.
- Keep baseline, robustness, endogeneity, mechanism, and heterogeneity blocks separate.

## Blueprint Output

Before code generation, output `【最终研究设计蓝图】` with:

- research question
- sample and data structure
- variable setup
- baseline model
- mechanism analysis
- robustness checks
- endogeneity checks
- heterogeneity analysis
- expected outputs

Then ask:

`请确认以上【最终研究设计蓝图】是否准确。只有在你回复“确认”后，我才会进入代码生成阶段。`
