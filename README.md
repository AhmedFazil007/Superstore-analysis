# Superstore Sales Analysis

**Excel · Power BI · Sales reporting**

I started with a Superstore dataset and a question that matters more than the sales total: **Which parts of the business are contributing to performance, and where should a manager investigate further?**

The goal was to bring sales trends, product categories and regional comparisons into one place, so it's easier to spot differences that might get lost in a spreadsheet.

## Dashboard

![Superstore dashboard](assets/superstore%20dashboard.png)

## Questions I explored

- Which regions contribute the most sales?
- How does performance vary across product categories?
- Are there periods or segments worth investigating more closely?
- What should a manager look at alongside revenue before making decisions?

The dashboard is a starting point for those conversations. A high-sales category isn't automatically the most profitable, and a lower-performing region isn't automatically an opportunity without understanding costs and demand.

## Business takeaway

If I were presenting this to a retail manager, I'd recommend reviewing **sales and profit together**, then drilling down by region, category and time. That would help distinguish growth opportunities from areas where revenue looks healthy but profitability needs attention.

I'd follow any proposed action with KPIs such as **gross margin, repeat purchases and sales growth by segment**, rather than claiming an improvement from the dashboard alone.

## Reproduce the profitability analysis

The repository includes a [Python analysis script](python/analyze_superstore.py) and [methodology notes](docs/PROFITABILITY_ANALYSIS.md) to compare sales, profit and discount bands using the Excel workbook. The script needs to be run and checked before presenting its output as verified findings.

## Project files

| File | What's inside |
|---|---|
| [Power BI dashboard](powerbi/Superstore.pbix) | Interactive sales report |
| [Excel workbook](data/Superstore.xlsx) | Source data and analysis |
| [Dashboard screenshot](assets/superstore%20dashboard.png) | Report preview |

## Scope

This is a portfolio case study showing how I approach sales analysis and reporting. It doesn't represent a measured improvement at an employer.

---

[Ahmed Fazil](https://github.com/AhmedFazil007)
