# Empirical Analysis Plan Rules

## Stage 1B Requirement

After variable names are confirmed in Stage 1A, the assistant must confirm the empirical analysis plan before any cleaning, statistics, regression, or visualization begins.

## Minimum Confirmation Items

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

## Required Behavior

- If the user has already provided enough information, organize it into a `实证分析方案确认表` and ask for confirmation.
- If information is incomplete, ask focused questions first.
- Do not move to data cleaning or later stages until the user explicitly confirms the plan.

## Suggested Confirmation Table

| 项目 | 用户信息 | 当前判断 | 是否已确认 |
| --- | --- | --- | --- |
| 被解释变量 |  |  |  |
| 核心解释变量 |  |  |  |
| 控制变量 |  |  |  |
| 中介/调节/机制变量 |  |  |  |
| 异质性分组变量 |  |  |  |
| 个体维度 |  |  |  |
| 时间维度 |  |  |  |
| 固定效应 |  |  |  |
| 标准误聚类 |  |  |  |
| 基准模型 |  |  |  |
| 稳健性/机制/异质性 |  |  |  |

## Confirmation Wording

Use a concise prompt such as:

`我已经整理出实证分析方案确认表。请确认被解释变量、核心解释变量、控制变量、面板维度、固定效应、标准误聚类方式和基准模型是否正确；确认后我才会进入第二阶段。`
