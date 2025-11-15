import pandas as pd

# Load original telemetry
df = pd.read_csv("full_race_telemetry.csv")

# Columns to keep
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

# Keep clean dataframe
df_clean = df[cols_to_keep].copy()

# Add ES column with default 0
df_clean["ES"] = 0

# Set ES = 1 at row 10k and 60k
df_clean.loc[10000, "ES"] = 1
df_clean.loc[60000, "ES"] = 1

# Save to output CSV
df_clean.to_csv("telemetry.csv", index=False)
