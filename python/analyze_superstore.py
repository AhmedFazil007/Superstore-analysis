"""Create sales and profitability summaries from the Superstore Excel workbook.
Usage: pip install pandas openpyxl
       python python/analyze_superstore.py
Sheet can be selected using --sheet "Sheet Name" (default first).
"""
from pathlib import Path
import argparse
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument("--sheet",default="0")
args=parser.parse_args()
sheet=int(args.sheet) if args.sheet.isdigit() else args.sheet
df=pd.read_excel(ROOT/"data/Superstore.xlsx",sheet_name=sheet)
df.columns=[str(c).strip() for c in df.columns]
print("Source columns:",list(df.columns))
def field(*aliases):
    mapping={c.lower().replace("_"," ").strip():c for c in df.columns}
    return next((mapping[a.lower()] for a in aliases if a.lower() in mapping),None)
sales=field("Sales");profit=field("Profit");region=field("Region")
category=field("Category");discount=field("Discount")
if not sales or not profit: raise SystemExit("Expected Sales and Profit columns; select the correct worksheet.")
for c in (sales,profit):
    df[c]=pd.to_numeric(df[c],errors="coerce")
df=df.dropna(subset=[sales,profit])
out=ROOT/"analysis";out.mkdir(exist_ok=True)
for name,col in (("region",region),("category",category)):
    if col:
        summary=df.groupby(col,dropna=False).agg(
            records=(sales,"size"),sales=(sales,"sum"),profit=(profit,"sum")).reset_index()
        summary["profit_margin_pct"]=100*summary["profit"]/summary["sales"].where(summary["sales"]!=0)
        summary.to_csv(out/f"{name}_profitability.csv",index=False)
if discount:
    df[discount]=pd.to_numeric(df[discount],errors="coerce")
    df["discount_band"]=pd.cut(df[discount],[-0.001,0,0.1,0.2,1.0],
                               labels=["0%","0–10%","10–20%",">20%"])
    result=df.groupby("discount_band",observed=True).agg(
        records=(sales,"size"),sales=(sales,"sum"),profit=(profit,"sum"))
    result["margin_pct"]=100*result.profit/result.sales.where(result.sales!=0)
    result.to_csv(out/"discount_profitability.csv")
print("Exported analysis CSVs to analysis/.")
print("Discount comparisons are observational; product mix can confound results.")
