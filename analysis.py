import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ================================
# PATH SETUP (SAFE & ERROR-PROOF)
# ================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "transport_logs.csv")

OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
FIGURE_DIR = os.path.join(OUTPUT_DIR, "figures")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(FIGURE_DIR, exist_ok=True)

print("Looking for file at:", DATA_PATH)

# ================================
# LOAD DATA
# ================================
df = pd.read_csv(DATA_PATH)
print("Loaded rows:", len(df))


# ================================
# KPI CALCULATIONS
# ================================
kpis = {
    "total_records": len(df),
    "avg_delay_min": df["delay_min"].mean(),
    "pct_delayed (>5min)": (df["delay_min"] > 5).mean() * 100,
    "avg_passengers_per_stop": df["passenger_count"].mean(),
    "busiest_route_by_passengers": df.groupby("route")["passenger_count"].sum().idxmax()
}

kpi_path = os.path.join(OUTPUT_DIR, "kpis.csv")
pd.DataFrame([kpis]).to_csv(kpi_path, index=False)
print("Saved KPIs to:", kpi_path)


# ================================
# VISUALIZATION 1 — Delay Distribution
# ================================
plt.figure(figsize=(8, 5))
plt.hist(df["delay_min"], bins=30)
plt.title("Delay Distribution (Minutes)")
plt.xlabel("Delay (min)")
plt.ylabel("Frequency")
fig1_path = os.path.join(FIGURE_DIR, "delay_distribution.png")
plt.savefig(fig1_path)
print("Saved:", fig1_path)
plt.close()


# ================================
# VISUALIZATION 2 — Avg Delay by Hour
# ================================
hourly_delay = df.groupby("scheduled_hour")["delay_min"].mean()

plt.figure(figsize=(8, 5))
hourly_delay.plot(kind="line", marker="o")
plt.title("Average Delay by Hour")
plt.xlabel("Scheduled Hour")
plt.ylabel("Avg Delay (min)")
fig2_path = os.path.join(FIGURE_DIR, "avg_delay_by_hour.png")
plt.savefig(fig2_path)
print("Saved:", fig2_path)
plt.close()


# ================================
# STOP HOTSPOTS (Delays by stop)
# ================================
stop_hotspots = df.groupby("stop")["delay_min"].mean().sort_values(ascending=False)
hotspot_path = os.path.join(OUTPUT_DIR, "stop_hotspots.csv")
stop_hotspots.to_csv(hotspot_path)
print("Saved stop hotspots:", hotspot_path)


# ================================
# VISUALIZATION 3 — Top 10 stop delays
# ================================
plt.figure(figsize=(8, 5))
stop_hotspots.head(10).plot(kind="bar")
plt.title("Top Delay Hotspots (Stops)")
plt.ylabel("Avg Delay (min)")
fig3_path = os.path.join(FIGURE_DIR, "top10_stop_delay.png")
plt.savefig(fig3_path)
print("Saved:", fig3_path)
plt.close()


# ================================
# PASSENGER LOAD BY HOUR
# ================================
passenger_hour = df.groupby("scheduled_hour")["passenger_count"].sum()

plt.figure(figsize=(8, 5))
passenger_hour.plot(kind="line", marker="o")
plt.title("Passenger Load by Hour")
plt.xlabel("Scheduled Hour")
plt.ylabel("Passenger Count")
fig4_path = os.path.join(FIGURE_DIR, "passenger_load_by_hour.png")
plt.savefig(fig4_path)
print("Saved:", fig4_path)
plt.close()

passenger_csv_path = os.path.join(OUTPUT_DIR, "passenger_by_hour.csv")
passenger_hour.to_csv(passenger_csv_path)
print("Saved passenger_by_hour.csv")


# ================================
# INCIDENTS
# ================================
incidents = df[df["incident_flag"] == 1]
incident_path = os.path.join(OUTPUT_DIR, "incidents.csv")
incidents.to_csv(incident_path, index=False)
print("Saved incidents:", incident_path)


print("\nAnalysis complete!")
print("All outputs saved inside:", OUTPUT_DIR)
