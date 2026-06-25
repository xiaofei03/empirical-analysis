# Data Cleaning Rules

## Stage Order

Do not start any cleaning before Stage 1 variable-name confirmation is complete.

## Required Cleaning Logic

- Apply sample screening explicitly.
- State time window, industry filter, region filter, ownership filter, listing-status filter, and special-year exclusions clearly.
- Drop missing values with explicit variable loops.
- Winsorize only continuous variables.
- Use `egen` for grouped statistics and summary inputs.
- Use `gen` for final constructed variables, dummies, interaction terms, and transformed indicators.
- Clear duplicated panel keys before `xtset` when needed.
- Set panel structure only after cleaning is done.

## Preferred Checks

- sample period
- manufacturing filter when needed
- ST/PT exclusion when needed
- delisted firm exclusion when needed
- one-observation firm exclusion when needed

## Safe Defaults

- Do not force `clear all`.
- Do not force `set more off`.
- Keep intermediate datasets when useful.
- Keep renamed variables stable before modeling.
