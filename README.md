# 2FG% 🏀

A Python script for calculating **2PT%**, **2FGM**, and **2FGA** from NBA box score data.  
Since the NBA doesn’t provide 2-point shooting splits directly, this script makes it easy to break down field goals into **2s vs 3s**.

---

## Example

```python
from twofg import calculate_two_point_stats

# Example: Player goes 10/20 FG, 3/8 from 3
fgm, fga = 10, 20
three_pm, three_pa = 3, 8

stats = calculate_two_point_stats(fgm, fga, three_pm, three_pa)
print(stats)
```

## Installation
1. Clone the repo
```bash
git clone https://github.com/swagswagstar/2FG.git
cd 2FG
```
2. Run with Python (3.9 and above)
```bash
python main.py
```

---
## Roadmap
- Support multiple players from JSON/CSV box scores
- Connect to NBA Stats API for automatic data collection
- Add shot chart visualization (heatmaps, zones)
- Deploy as a web app (Flask + React)
