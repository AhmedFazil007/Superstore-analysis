# Superstore Sales & Profit Analysis

**Excel · Power BI · Sales and profitability reporting**

I used a Superstore dataset to explore a question I kept coming back to: **does a region or category that sells more necessarily contribute more profit?**

I wanted the dashboard to be more than a ranking of top-selling products. My focus was on the relationship between sales, profit, regions and product categories—and what I would check before recommending a business change.

## Dashboard

![Superstore sales dashboard](assets/superstore%20dashboard.png)

## What I looked for

**Sales and profit can tell different stories.** A category may bring in substantial revenue without generating the same share of profit. I would compare both before calling it a strong performer.

**Regional totals need context.** If one region sells more than another, that doesn't automatically mean the lower-sales region is underperforming. I'd want to compare its product mix, discounts and profit margin.

**Discounts deserve a closer look.** Promotions may increase sales, but I would check whether discounted orders still contribute enough profit to justify them.

These are the business questions behind the dashboard. I haven't included exact rankings or percentages here because the reproducible profitability summaries still need to be run and checked against the source workbook.

## What I would recommend

I'd start with a **region-by-category sales and profit comparison**, then investigate segments where sales are strong but profit is weak. If discounts appear related to lower margins, I'd test a pricing change on a limited group rather than assume discounts caused the difference.

To judge whether a change helped, I'd track **profit, profit margin and sales**, not revenue alone.

## Files and reproduction

| File | What it's for |
|---|---|
| [Power BI report](powerbi/Superstore.pbix) | Interactive dashboard |
| [Excel dataset](data/Superstore.xlsx) | Source workbook |
| [Dashboard screenshot](assets/superstore%20dashboard.png) | Preview |
| [Python analysis](python/analyze_superstore.py) | Region, category and discount-band summaries |
| [Method notes](docs/PROFITABILITY_ANALYSIS.md) | Definitions and caveats |

To generate the Python summaries:

```bash
pip install pandas openpyxl
python python/analyze_superstore.py
```

If the data isn't on the first worksheet, the script supports `--sheet "Sheet Name"`. Generated CSVs appear under `analysis/`. I haven't presented their findings as verified until that run is checked.

## My takeaway

A dashboard can tell me where sales are coming from, but I need profit and cost context before I can suggest where a business should invest. That's the main lesson I wanted this project to show.

*Independent portfolio project. The recommendations are ideas to investigate, not changes implemented for a company.*
