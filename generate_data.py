import os
import pandas as pd
import numpy as np

# Ensure correct folder (no path errors)
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

np.random.seed(42)

num_rows = 12000
routes = ['R1', 'R2', 'R3']
stops = ['S1', 'S2', 'S3', 'S4', 'S5']
schedule_hours = np.random.randint(5, 23, num_rows)
actual_hours = schedule_hours + np.random.choice([0, 1], num_rows)
delay_minutes = np.random.normal(2, 1.5, num_rows)
delay_minutes = np.clip(delay_minutes, 0, None)
passenger_count = np.random.randint(5, 60, num_rows)
incident_flag = np.random.choice([0, 1], num_rows, p=[0.97, 0.03])
route_list = np.random.choice(routes, num_rows)
stop_list = np.random.choice(stops, num_rows)

df = pd.DataFrame({
    "route": route_list,
    "stop": stop_list,
    "scheduled_hour": schedule_hours,
    "actual_hour": actual_hours,
    "delay_min": delay_minutes,
    "passenger_count": passenger_count,
    "incident_flag": incident_flag
})

output_path = os.path.join(data_dir, "transport_logs.csv")
df.to_csv(output_path, index=False)

print("Dataset generated!")
print("Saved to:", output_path)
