# 🚗 Radiator Performance Monitoring & Analytics System

> A Python-based real-time monitoring and analytics system that processes sensor-generated data to visualize radiator performance, detect abnormal operating conditions, and provide actionable insights through dynamic dashboards.

---

## 📌 Overview

This project is a **real-time data analytics and visualization application** developed in Python to monitor radiator performance using sensor-generated operational data.

The system continuously reads data from CSV files, analyzes critical operating parameters, detects abnormal conditions using configurable thresholds, and visualizes the results through interactive dashboards.

While the data is collected using a Raspberry Pi-based acquisition setup, the primary focus of this repository is the **software pipeline** for data processing, analytics, and visualization.

---

## ✨ Features

- 📊 Real-time performance monitoring
- 🌡️ Water & Oil temperature analysis
- ⚙️ RPM trend visualization
- 🚘 Gear position monitoring
- 🚨 Threshold-based anomaly detection
- 📈 Automatic warning generation
- 🔄 Continuous dashboard refresh
- 📂 CSV-based data processing
- 🧹 Modular and reusable Python code

---

## 🏗️ System Architecture
<img width="976" height="732" alt="image" src="https://github.com/user-attachments/assets/72b31698-f8c8-423f-bd2d-1ad2a7e9ba82" />


---

| Temperature Analysis | RPM Analysis |
|----------------------|--------------|
| ![](images/tempVStime.jpg) | ![](images/RpmandGearVStime.jpg) |

| Warning Status |
|----------------|
| ![](images/warning.jpg) |

---
---

## ⚙️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Input | CSV Files |
| Monitoring | Threshold-Based Analytics |

---

## 📈 Data Processing Workflow

The application performs the following tasks:

- Reads real-time sensor-generated CSV data
- Converts timestamps into datetime format
- Extracts operational parameters
- Performs threshold analysis
- Detects abnormal operating conditions
- Generates warning status
- Creates live graphical dashboards
- Refreshes visualizations periodically

---

## 📊 Parameters Monitored

| Parameter | Description |
|-----------|-------------|
| 🌡️ Water Temperature | Cooling system temperature |
| 🔥 Oil Temperature | Lubrication system temperature |
| ⚙️ RPM | Engine rotational speed |
| 🚘 Gear Position | Current operating gear |
| 🚨 Warning Status | Indicates abnormal conditions |

---

## 🚨 Anomaly Detection

The application continuously evaluates system health using configurable thresholds.

Current thresholds:

| Parameter | Threshold |
|-----------|-----------|
| Water Temperature | 200°C |
| Oil Temperature | 200°C |
| RPM | 2000 |

If any threshold is exceeded, the dashboard automatically highlights the condition for quick identification.

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/radiator-performance-monitor.git
```

---

### Navigate to the Project

```bash
cd radiator-performance-monitor
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📋 Sample Input

The application expects a CSV file containing the following columns:

```text
DateTime
Water Temperature
Oil Temperature
RPM
Gear Position
```

Example:

```csv
DateTime,WaterTemp,OilTemp,RPM,Gear
2024-11-12 10:00,84,91,1600,2
2024-11-12 10:01,85,93,1750,2
2024-11-12 10:02,89,95,1900,3
```

---

## 📈 Results

The software provides:

- Real-time operational monitoring
- Dynamic graphical dashboards
- Automatic anomaly detection
- Continuous trend visualization
- Improved interpretation of radiator performance data

---

## 🔮 Future Improvements

- 🌐 Web-based dashboard using Flask or Streamlit
- ☁️ Cloud database integration
- 📱 Mobile monitoring interface
- 🤖 Machine Learning-based predictive maintenance
- 📊 Historical trend analytics
- 📡 MQTT/IoT integration

---

## 🔧 Hardware (Data Collection)

The dataset used by this application is generated using a Raspberry Pi-based data acquisition setup with temperature and operational sensors.

This repository primarily focuses on the **software components** responsible for processing, analyzing, and visualizing the collected data.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Authors

**Harini S**

B.Tech Electronics and Computer Science Engineering

Vellore Institute of Technology, Chennai

---

## ⭐ If you found this project useful, consider giving it a star!
