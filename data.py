import os
import fastf1
import pandas as pd
if not os.path.exists("f1_cache"):
    os.makedirs("f1_cache")
fastf1.Cache.enable_cache('f1_cache')
session = fastf1.get_session(2023, "Monza", "R")
session.load()
full_data = pd.DataFrame()
for drv in session.drivers:
    laps = session.laps.pick_driver(drv)
    for _, lap in laps.iterrows():
        tel = lap.get_telemetry()
        tel["Driver"] = drv
        full_data = pd.concat([full_data, tel], ignore_index=True)
full_data.to_csv("full_race_telemetry.csv", index=False)
print("Done! full_race_telemetry.csv created.")
