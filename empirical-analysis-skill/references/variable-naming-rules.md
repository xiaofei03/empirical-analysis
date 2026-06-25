# Variable Naming Rules

## Core Rules

- Default to English.
- Keep names short, standard, consistent, and readable.
- Actual variable names may use normalized academic casing when that better matches paper conventions.
- Preserve common acronym forms such as `AI`, `ROA`, `ROE`, `CEO`, `SOE`, and `RD`.
- Allow PascalCase or acronym-plus-PascalCase forms such as `AIwashing`, `AIPatent`, `AIwashingSq`, `FirmSize`, `TradeCredit`, `AgencyCost`, and `TobinQ`.
- Do not use Chinese names in actual dataset variable names.
- Do not use underscores in actual dataset variable names.
- Do not use digits in actual dataset variable names.
- Do not end actual dataset variable names with digits.
- Do not use spaces in actual dataset variable names.
- Do not use special symbols in actual dataset variable names.
- Do not use overly long names.
- Do not use vague names such as `x`, `a`, `b`, `data`, or `var`.
- Prefer common empirical abbreviations when they are clear.
- Do not misclassify normalized acronym capitalization as inconsistent case.
- Treat `AI`, `ROA`, `ROE`, `CEO`, `SOE`, `RD`, and `TobinQ` as valid normalized academic names.
- Reserve `大小写不统一` for genuinely mixed or messy naming such as `FirmSIZE`, `aiWashing`, `AIWashing`, or `NetPROFITGrowth`.
- If raw names are uppercase, title case, or camelCase, normalize them to a clean academic style rather than forcing lowercase.
- If multiple raw names would collide after normalization, resolve the conflict by meaning, not by adding digits or underscores.
- If meaning cannot be determined, mark it `需用户确认含义`.

## Character Rule

- Actual variable names may contain only English letters.
- Actual variable names must not contain digits, underscores, spaces, Chinese characters, or special symbols.
- Validity should be checked with a letter-only pattern such as `^[A-Za-z]+$`.

## Digit Exception Boundary

- The digit ban applies only to actual variable names in the dataset and to newly generated variable names.
- The digit ban does not apply to formulas, mathematical notation, model descriptions, or paper presentation text.
- In formulas, model setup, paper explanations, table labels, or mathematical expression, superscript digits such as `age²`, `size²`, or `X²` are allowed.
- In Stata modeling, prefer explicit expressions such as `c.age#c.age` for squares instead of forcing a generated variable like `age2`.
- If a squared variable must be generated, use an `Sq` or `sq` suffix such as `AIwashingSq`, `FirmSizeSq`, `levsq`, or `roasq`.
- Do not use numeric suffixes for generated square terms.
- When checking variable names, do not misread superscript digits in formulas or mathematical expressions as dataset variable-name violations.

## Required Stage 1 Output

If any variable name is noncompliant, the assistant must:

1. Show a `变量名称修改建议表`.
2. Ask the user to confirm the changes.
3. Wait for explicit confirmation before renaming.
4. Print a `最终变量名对照表` after renaming.

## Table Format

| 原始变量名 | 参考变量含义 | 问题类型 | 建议变量名 | 修改理由 | 是否需用户确认含义 |
| ----- | ------ | ---- | ----- | ---- | --------- |

## Allowed Problem Labels

- 含下划线
- 含数字
- 结尾含数字
- 中文变量名
- 中英文混用
- 大小写不统一
- 命名过长
- 命名不清楚
- 与参考表不一致
- 可能导致代码或回归公式不稳定
- 与其他变量命名风格不统一
- 删除数字后可能重名
- 需结合测量方式判断

## Confirmation Wording

Use this wording when variables need renaming:

`我发现当前数据中的部分变量名称不符合你的命名规范，主要问题包括下划线、数字、结尾数字、大小写不统一或与常见控制变量名称不一致。根据你提供的参考表，我整理了下面的变量名修改建议。请确认是否同意这些修改；确认后我再执行重命名，并进入后续数据分析阶段。`
