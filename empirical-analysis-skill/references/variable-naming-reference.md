# Variable Naming Reference

Use this file as a meaning-and-measurement reference for common empirical variables. Do not copy names mechanically.

## Common Controls

- `size`: firm size, usually log total assets
- `lev`: leverage, usually total liabilities / total assets
- `roa`: return on assets
- `ebitroa`: EBIT-based return on assets
- `roe`: return on equity
- `grossprofit`: gross profit margin
- `netprofit`: net profit margin
- `profitgrowth`: net profit growth
- `assetgrowth`: total asset growth
- `cashflow`: operating cash flow ratio
- `tobinq`: Tobin's Q
- `bm`: book-to-market
- `pb`: price-to-book
- `growth`: revenue growth
- `liquid`: current ratio
- `quick`: quick ratio
- `rec`: receivables ratio
- `inv`: inventory ratio
- `fixed`: fixed asset ratio
- `intangible`: intangible asset ratio
- `tangible`: tangible asset ratio
- `ctr`: comprehensive tax rate
- `itr`: income tax rate
- `cap`: capital intensity
- `cmir`: capital preservation and appreciation rate
- `rca`: capital accumulation rate
- `fl`: financial leverage
- `ol`: operating leverage
- `cl`: combined leverage
- `loss`: loss dummy

## Firm Basics

- `firmage`: firm age
- `listage`: listing age
- `listedyear`: listing year
- `estyear`: founding year
- `delistyear`: delisting year
- `industry`: industry name
- `industrycode`: industry code
- `industrycat`: industry category
- `province`: province
- `city`: city
- `lng`: longitude
- `lat`: latitude
- `soe`: state ownership indicator

## Financing Constraints

- `sa`: SA index
- `ww`: WW index
- `fc`: FC index
- `kz`: KZ index

## Governance And Ownership

- `board`: board size
- `indep`: independent director ratio
- `dual`: CEO-chair duality
- `topone`: first shareholder ownership
- `topthree`: top three shareholder ownership
- `topfive`: top five shareholder ownership
- `topten`: top ten shareholder ownership
- `balanceone`: balance ratio using the second shareholder
- `balancefive`: balance ratio using shareholders two to five
- `balanceten`: balance ratio using shareholders two to ten
- `hthree`: Herfindahl index for top 3 shareholders
- `hfive`: Herfindahl index for top 5 shareholders
- `hten`: Herfindahl index for top 10 shareholders
- `separate`: control-rights minus cash-flow-rights separation
- `opinion`: standard audit opinion dummy
- `auditfee`: audit fee
- `bigfour`: big four auditor dummy
- `bigthree`: big three auditor dummy

## Management

- `employee`: employee count
- `tmtage`: average management age
- `tmtpay`: top three executive pay
- `totaltmtpay`: total executive pay
- `finback`: financial background dummy
- `overseaback`: overseas background dummy
- `female`: female management ratio

## R&D And Investment

- `rdincome`: R&D intensity relative to revenue
- `rdasset`: R&D intensity relative to assets
- `rdperson`: R&D personnel ratio
- `lnrd`: log R&D expenditure
- `lnrdperson`: log R&D personnel
- `invest`: investment level
- `acqinvest`: acquisition-related investment
- `netinvest`: net investment
- `fullinvest`: full investment

## Heterogeneity Groups

- `east`: eastern region dummy
- `west`: western region dummy
- `mid`: central region dummy
- `hightech`: high-tech industry dummy
- `pollute`: heavy-pollution industry dummy
- `labor`: labor-intensive industry dummy
- `tech`: technology-intensive industry dummy
- `asset`: asset-intensive industry dummy

## Normalization Examples

- `Size` -> `size`
- `Lev` -> `lev`
- `ROA1` -> `roa`
- `ROA2` -> `ebitroa`
- `EM1` -> `em`
- `EM2` -> `avgem`
- `CTR1` -> `ctr`
- `CTR2` -> `ctrp`
- `Invest1` -> `invest`
- `Invest2` -> `acqinvest`
- `Invest3` -> `netinvest`
- `Invest4` -> `fullinvest`
- `Top1` -> `topone`
- `Top3` -> `topthree`
- `Top5` -> `topfive`
- `Top10` -> `topten`
- `Balance1` -> `balanceone`
- `Balance2` -> `balancefive`
- `Balance3` -> `balanceten`
- `Herfindahl3` -> `hthree`
- `Herfindahl5` -> `hfive`
- `Herfindahl10` -> `hten`
- `FirmAge` -> `firmage`
- `ListAge` -> `listage`
- `ListedYear` -> `listedyear`
- `EstablishYear` -> `estyear`
- `DelistedYear` -> `delistyear`
- `IndustryName` -> `industry`
- `Industry1` -> `industrycode`
- `Industry2` -> `industrycat`
- `RD_Income` -> `rdincome`
- `RD_Asset` -> `rdasset`
- `RD_Person` -> `rdperson`
- `lnRDs` -> `lnrd`
- `lnRDp` -> `lnrdperson`
- `HighTech_1` -> `hightech`
- `HighTech_2` -> `hightechtwo`
- `HighTech_3` -> `hightechthree`
- `Pollute_1` -> `pollute`
- `Pollute_2` -> `pollutetwo`
- `Pollute_3` -> `pollutethree`
- `TMTPay1` -> `tmtpay`
- `TMTPay2` -> `totaltmtpay`
- `TMTAge` -> `tmtage`
- `FinBack` -> `finback`
- `OverseaBack` -> `overseaback`
- `AuditFee` -> `auditfee`
- `Big4` -> `bigfour`
- `Big3` -> `bigthree`
