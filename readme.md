# F1 Dataset - Real-Time Telemetry Streaming System

A resilient data transmission system that streams Formula 1 telemetry data over UDP, demonstrating real-world scenarios for high-frequency, low-latency data pipelines in unstable network conditions.

## 🏎️ Overview

This project simulates a real-world engineering scenario where high-frequency telemetry data needs to be transmitted reliably from a source (e.g., racetrack) to a control center over an unreliable network connection. It uses actual F1 race telemetry data to create a realistic testing environment for resilient data streaming systems.

## 📊 Data Source

**Race:** 2023 F1 Italian Grand Prix  
**Source:** [FastF1](https://github.com/theOehrly/Fast-F1) - An open-source library for accessing publicly available F1 timing and telemetry data

### What the Data Contains

High-frequency car telemetry measurements including:
- **Timestamps** - Precise timing information
- **Speed** - Vehicle velocity (km/h)
- **Throttle** - Throttle position (0-100%)
- **Brake** - Brake pressure
- **Gear** - Current gear selection
- **RPM** - Engine revolutions per minute
- **Gap** - Time gap to car ahead
- **DRS** - Drag Reduction System status
- **And more...**

The dataset contains thousands of real measurements captured at high frequency during the race, providing an ideal test case for streaming data pipelines.

## 🎯 Use Cases

This system demonstrates solutions for:
- **Remote Monitoring** - Disaster sites, field research, remote laboratories
- **High-Performance Environments** - Racing, aerospace, industrial IoT
- **Unstable Networks** - Mobile data connections, satellite links, congested networks
- **Real-Time Analytics** - Stream processing, live dashboards, anomaly detection

## 🏗️ System Architecture

```
F1 Telemetry Data → UDP Sender → Network (unreliable) → UDP Receiver → WebTransport → Real-Time Visualization
```

### Components

1. **Data Collector** (`data.py`)
   - Fetches F1 telemetry using FastF1 library
   - Processes and structures race data
   - Prepares data for streaming

2. **UDP Sender** (`udp_sender.py`)
   - Streams telemetry packets over UDP
   - Simulates unreliable network conditions
   - Implements sequence numbering for packet tracking

3. **UDP Receiver** (`udp_receiver.py`)
   - Receives UDP packets
   - Detects packet loss using sequence numbers
   - Repairs missing data
   - Buffers and forwards data

4. **Data Cleaner** (`clean_data.py`)
   - Preprocesses raw telemetry
   - Handles missing values
   - Normalizes data formats

5. **Cache** (`f1_cache/`)
   - Stores processed telemetry data
   - Reduces API calls to FastF1
   - Improves performance

## 🚀 Getting Started

### Prerequisites

```bash
pip install fastf1 pandas numpy
```

### Installation

```bash
git clone https://github.com/vishux777/f1_dataset.git
cd f1_dataset
```

### Usage

1. **Fetch and Process F1 Data:**
```bash
python data.py
```

2. **Start the UDP Receiver:**
```bash
python udp_receiver.py
```

3. **Start Streaming Telemetry:**
```bash
python udp_sender.py
```

## 📁 Project Structure

```
f1_dataset/
├── data.py              # F1 data collection and processing
├── udp_sender.py        # UDP packet transmission
├── udp_receiver.py      # UDP packet reception and repair
├── clean_data.py        # Data preprocessing utilities
├── test.py              # Unit tests
├── f1_cache/            # Cached telemetry data
├── telemetry.csv        # Processed telemetry dataset
├── full_race_telemetry.csv  # Complete race data
├── diagram.md           # System architecture diagram
└── readme.md            # Project documentation
```

## 🔧 Key Features

- **Resilient Transmission** - Handles packet loss gracefully with sequence-based recovery
- **Real-World Data** - Uses authentic F1 telemetry from actual races
- **High Frequency** - Processes thousands of measurements per second
- **Low Latency** - Optimized for real-time streaming
- **Extensible** - Easy to adapt for other telemetry sources

## 📈 Dataset Characteristics

- **Frequency:** High-frequency sampling (multiple readings per second)
- **Volume:** Thousands of data points per race
- **Variety:** Multiple sensor types and measurements
- **Velocity:** Real-time streaming capability
- **Veracity:** Authentic race data from official sources

## 🔍 Problem Statement Alignment

This project addresses the challenge of transmitting high-volume, time-sensitive data over unreliable networks. It demonstrates:

1. **Packet Loss Recovery** - Sequence numbering and gap detection
2. **Real-Time Processing** - Low-latency data pipeline
3. **Scalability** - Handles high-frequency data streams
4. **Reliability** - Ensures data integrity despite network issues

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 🙏 Acknowledgments

- **FastF1** - For providing easy access to F1 timing and telemetry data
- **Formula 1** - For making timing data publicly available
- **2023 Italian Grand Prix** - For the telemetry data used in this project

## 📧 Contact

For questions or collaboration opportunities, please open an issue on GitHub.

---

**Note:** This project is for educational and demonstration purposes, showcasing resilient data transmission techniques using real-world telemetry data.