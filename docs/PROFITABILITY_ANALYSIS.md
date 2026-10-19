# Profitability and Discount Analysis

I added a Python script that makes the sales dashboard easier to check and extend. It groups sales and profit by **region and category**, and—if the workbook has a Discount column—compares **observed profit margins by discount band**.

Run:

```bash
pip install pandas openpyxl
python python/analyze_superstore.py
```

Use `--sheet "Sheet Name"` if the data is not in the first worksheet. Outputs appear in `analysis/` after a successful run.

A region with high sales can still have weak profit. Discount-band comparisons may reveal differences worth investigating, but they do not establish that discounting caused those differences. The script has been added to the repository; it still needs to be executed against the Excel workbook and its outputs reviewed.
