# Output Format Rules

## Operating-Mode Output Logic

The output requirements depend on the operating mode.

### Full Analysis Mode

Formal outputs should include:

1. `最终变量名对照表`
2. `结果展示名对照表`
3. `实证分析方案确认表`
4. formal do-files
5. formal result tables in both `rtf` and `markdown`
6. formal figures
7. `result_manifest`
8. `consistency_check`

### Result Refactor Mode

Formal outputs should include:

1. `最终变量名对照表`
2. `结果展示名对照表`
3. `结果口径差异确认表` when needed
4. standardized do-files
5. regenerated or synchronized `rtf` and `markdown` tables
6. standardized figures
7. `result_manifest`
8. `consistency_check`

## Dual-Layer Naming Output

The assistant must distinguish:

- analysis variable names
- display variable names

Required tables:

### `最终变量名对照表`

| 原始变量名 | 分析变量名 | 变量含义 | 是否已确认 |
| --- | --- | --- | --- |

### `结果展示名对照表`

| 分析变量名 | 展示变量名 | 适用对象 | 是否已确认 |
| --- | --- | --- | --- |

`适用对象` should indicate one or more of:

- table
- figure
- manuscript

## Legacy Drift Output

When legacy drift exists, the assistant must output:

### `结果口径差异确认表`

| 对比对象A | 对比对象B | 差异类型 | 具体差异 | 当前建议基线 | 是否需用户确认 |
| --- | --- | --- | --- | --- | --- |

Allowed difference types include:

- 样本量不一致
- 系数不一致
- t值不一致
- 显著性不一致
- 变量口径不一致
- 列顺序不一致
- do文件与结果表不一致
- 论文表与结果表不一致

## Markdown-First Rule

Markdown is the only formal table source for downstream manuscript writing.

- Every formal table must be exported to both `rtf` and `markdown`.
- `markdown` is the writing-source truth.
- `rtf` is a parallel formatting artifact.
- If `rtf` and `markdown` differ, the assistant must stop and perform consistency audit before proceeding.

## Figure Final Format

Final empirical figures must satisfy all of the following:

- English only
- Times New Roman only
- no Chinese axis title
- no Chinese legend
- no Chinese annotation
- no raw variable names with underscores or numeric suffixes
- no overlapping tick labels in final delivery

Preferred route:

- Stata computes values
- Python handles final plotting

## Formal Deliverable Module

Every formal empirical delivery should include these artifacts when applicable:

- master do-file
- module do-files
- `rtf` result tables
- `markdown` result tables
- plotting-data files or figure-source files
- final figure files
- `result_manifest.md`
- `consistency_check.md`

### `result_manifest.md`

Should record:

- output name
- output type
- data source
- do-file source
- sample definition
- baseline source
- whether synchronized from legacy result
- whether consistency audit passed

### `consistency_check.md`

Should record:

- checked outputs
- comparison source
- whether sample size matches
- whether coefficient values match
- whether t values match
- whether significance markers match
- whether display names match
- whether figure labels match
- final pass or fail status

## Required Stage Outputs

### Full Analysis Mode Stage 1

1. Raw variable list
2. `变量名称修改建议表` if needed
3. user confirmation request
4. `最终变量名对照表`
5. `结果展示名对照表`
6. `实证分析方案确认表`

### Result Refactor Mode Stage R1-R2

1. Raw variable list
2. `变量名称修改建议表` if needed
3. `最终变量名对照表`
4. `结果展示名对照表`
5. `结果口径差异确认表` if needed

## If Names Already Comply

Output exactly:

`变量名称已通过规范化核验：未发现下划线、数字、中文变量名、特殊符号或明显不统一命名。可以进入第二阶段的数据结构与清洗处理。`

## Module Writing Style

- Keep `SKILL.md` as the controller.
- Keep detailed rules in reference files.
- Keep analysis outputs concise and explicit.
- Use Chinese logic comments before key empirical blocks.
- Use stable English file names for formal result outputs.
