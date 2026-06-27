# Radiator Performance Monitoring & Analytics
# Overview
A Python-based real-time monitoring system for analyzing radiator performance using sensor-generated data. The application processes streaming CSV data, visualizes operational metrics, and detects abnormal operating conditions through configurable threshold analysis.

The project focuses on software-driven analytics while using externally collected sensor data as the input source.

# Features
Real-time data visualization
Live temperature monitoring
RPM trend analysis
Gear position tracking
Threshold-based anomaly detection
Automatic warning generation
CSV data processing
Continuous dashboard refresh
Dashboard

(Insert screenshots here)

images/dashboard.png
Software Stack
Python
Pandas
NumPy
Matplotlib
Data Pipeline
Sensor Data
      ↓
CSV Dataset
      ↓
Python Data Processing
      ↓
Threshold Analysis
      ↓
Visualization
      ↓
Warning Generation
Project Structure
src/
data/
images/
requirements.txt
README.md
How it Works
Reads sensor-generated CSV data.
Extracts
Water Temperature
Oil Temperature
RPM
Gear Position
Detects abnormal operating conditions using configurable thresholds.
Updates graphical dashboards every 30 seconds.
Displays warning status in real time.
Results

The system provides

Continuous monitoring
Automatic anomaly detection
Visual performance analysis
Easy identification of overheating and abnormal operating conditions
Future Improvements
Interactive web dashboard
Machine Learning-based fault prediction
Cloud-based monitoring
MQTT/IoT integration
Historical analytics
Hardware Used (Minimal)

This project uses sensor-generated data collected through a Raspberry Pi-based data acquisition setup. The repository focuses on the software components responsible for processing, analyzing, and visualizing the collected data.

Installation
git clone https://github.com/yourusername/radiator-performance-monitor.git

cd radiator-performance-monitor

pip install -r requirements.txt

python src/main.py
