import pandas as pd
df = pd.read_csv("full_race_telemetry.csv")
cols_to_keep = [
    "Date",
    "SessionTime",
    "Time",
    "RPM",
    "Speed",
    "nGear",
    "Throttle",
    "Brake",
    "Status",
    "Driver"
]
df_clean = df[cols_to_keep]
df_clean.to_csv("telemetry.csv", index=False)