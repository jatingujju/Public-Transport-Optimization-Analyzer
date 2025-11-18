# Public-Transport-Optimization-Analyzer
Analyze vehicle GPS + passenger count logs for multiple bus routes to identify peak hours, delay hotspots, route inefficiencies, and give operational recommendations to optimize schedules and reduce wait time.


**Domain:** Urban Mobility / Operations Analytics  
**Goal:** Analyze scheduled vs actual bus arrivals, detect delay hotspots, identify peak passenger loads, and provide recommendations to optimize schedules.

## Contents
- `src/generate_data.py` — synthetic transit log generator
- `src/analysis.py` — analysis, KPIs, plots, hotspot detection
- `data/transit_logs.csv` — generated dataset (after running generator)
- `outputs/figures/` — saved charts
- `outputs/*.csv` — KPI and summary CSVs

## How to run
1. Create virtual environment and install:
```bash
pip install -r requirements.txt
