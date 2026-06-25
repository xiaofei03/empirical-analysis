# Output Format Rules

## Required Stage 1 Outputs

When variables need checking or renaming:

1. Raw variable list
2. `变量名称修改建议表`
3. User confirmation request
4. `最终变量名对照表` after confirmation and renaming

## Table Format

Use the following table for suggestions:

| 原始变量名 | 参考变量含义 | 问题类型 | 建议变量名 | 修改理由 | 是否需用户确认含义 |
| ----- | ------ | ---- | ----- | ---- | --------- |

## If Names Already Comply

Output exactly:

`变量名称已通过规范化核验：未发现下划线、数字、中文变量名、特殊符号或明显不统一命名。可以进入第二阶段的数据结构与清洗处理。`

## Module Writing Style

- Keep `SKILL.md` as the controller.
- Keep detailed rules in reference files.
- Keep analysis outputs concise and explicit.
- Use Chinese logic comments before key empirical blocks.
