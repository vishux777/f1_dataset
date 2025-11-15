We use telemetry data from the 2023 F1 Italian Grand Prix.
Data is accessed legally using the open-source FastF1 library, which processes publicly available timing data.

What the data contains:
High-frequency car telemetry: timestamps, speed, throttle, brake, gear, RPM, gap to car ahead, and more.
This creates a dataset with thousands of real measurements.

Why we use it:
Telemetry is the perfect high-volume, low-latency data stream for testing our resilient transmission system.

How we use it:
We stream telemetry packets over unreliable UDP, repair losses using sequence numbers, and forward the data via WebTransport to visualize it in real time.

How it relates to the problem statement:
Our solution simulates a real engineering scenario (racetrack → control center) and demonstrates a fast, resilient data pipeline suitable for unstable connections, disaster sites, remote labs, and high-performance environments.