# Connected & Left Behind: Internet Access Across the World

A scrollytelling web story remixing a MakeoverMonday data visualization into a narrative piece. Built for a journalism class assignment.

## What it is

A single-page scrolling story about global internet access in 2022, broken into three charts and accompanying text. The original dashboard (by Chimdi Nwosu, via MakeoverMonday Wk45) shows all 193 countries at once — this piece breaks it into three focused moments with a narrative arc.

## Files

| File | What it is |
| `internet-access-story.html` | The story. Self-contained — all chart images are embedded as base64, no external dependencies |
| `remake_charts.py` | Python script of the charts |
| `ai2html-config.json` | Font mapping config for ai2html place in same folder as your .ai file
| `Countries_data.csv`  | CSV data file downloaded from Tableau

## How it was made

1. Data from the World Bank via [MakeoverMonday Wk45](https://public.tableau.com/app/profile/chimdi.nwosu/viz/MakeoverMondayWk45-InternetAccessAcrosstheWorld_2003to2022/Dashboard1)
2. Data inputted and charts drafted in Python
3. Edited in Adobe Illustrator
4. Exported as HTML + PNG using ai2html
5. Embedded into the scrolling story page

## Sources

- Data: World Bank, internet penetration rates 2022
- Original visualization: Chimdi Nwosu / MakeoverMonday
