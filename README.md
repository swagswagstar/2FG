# 2FG% 🏀

A Python script for calculating **2PT%**, **2FGM**, and **2FGA** from NBA box score data.  
Since the NBA doesn’t provide 2-point shooting splits directly, this script makes it easy to break down field goals into **2s vs 3s**.

---

## Example

```bash
# OUTPUT
PS C:\Users\Me\2FG> python main.py
Choose mode:
1. Manual entry
2. Import spreadsheet
Enter 1 or 2: 1
Enter player name: Nikola Jokic
Enter total FGM: 5
Enter total FGA: 9
Enter 3PM: 1
Enter 3PA: 2

--- 2PT Stats ---
Player: Nikola Jokic
2FGM: 4
2FGA: 7
2PT%: 57.14%
PS C:\Users\Me\2FG> 
```

## Installation
1. Clone the repo
```bash
git clone https://github.com/swagswagstar/2FG.git
cd 2FG
```
2. Install `pandas`, `openpyxl` and `xlrd`
```bash
pip install pandas openpyxl xlrd
```
3. Run with Python (3.9 and above)
```bash
python main.py
```

---
## Roadmap
- Connect to NBA Stats API for automatic data collection
- Add shot chart visualization (heatmaps, zones)
- Deploy as a web app (Flask + React)
