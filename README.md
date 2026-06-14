# 🛡️ AI Cyber Threat Pattern Detector

An advanced Cybersecurity Analytics Platform built using PyTorch, Streamlit, Scapy, and Machine Learning.

The system learns normal network traffic behavior using a Deep Autoencoder and identifies suspicious activities through anomaly detection.

It also provides real-time packet monitoring, threat intelligence, attack analytics, geolocation visualization, PDF reporting, and interactive network attack graphs.

---

# 🚀 Features

## 🔍 Deep Learning Anomaly Detection

- PyTorch Autoencoder
- Unsupervised Learning
- Reconstruction Error Analysis
- Cyber Threat Detection

---

## 📊 Dataset Analysis

Uses the NSL-KDD cybersecurity dataset.

Features:

- Data Cleaning
- Feature Engineering
- Label Encoding
- Normalization
- Train/Test Splitting

---

## 🚨 Threat Detection Engine

Detects abnormal traffic using:

```text
Input Traffic
       ↓
Autoencoder
       ↓
Reconstruction Error
       ↓
Threat Classification
```

---

## 📈 Latent Space Visualization

Visualize learned traffic patterns using:

### PCA

- Dimensionality Reduction
- Cluster Visualization

### t-SNE

- Pattern Exploration
- Traffic Separation

---

## 🖥️ Streamlit Dashboard

Interactive cybersecurity dashboard featuring:

### Home

- Project Overview
- Model Information
- System Status

### Dataset Overview

- Dataset Statistics
- Attack Distribution
- Sample Records

### Anomaly Detection

- Detection Results
- Threat Metrics
- Traffic Classification

### Visualizations

- PCA Visualization
- t-SNE Visualization

### Real-Time Monitor

- Simulated Threat Scores
- Live Monitoring Dashboard

---

# 🌐 Real Packet Monitoring

Built using:

- Scapy
- PyTorch
- Autoencoder

Features:

- Live Packet Capture
- Real-Time Analysis
- Threat Detection
- CSV Logging

Example:

```text
192.168.1.8 -> 20.52.64.201
Status = THREAT
Error = 51570.29
```

---

# 🛡️ Security Operations Center (SOC)

Professional SOC-style dashboard.

Includes:

- Total Packets
- Threat Count
- Normal Traffic
- Threat Percentage
- Threat Timeline
- Source IP Analysis
- Latest Threat Activity

---

# 🌍 Threat Intelligence Feed

Identify the most dangerous IP addresses.

Features:

- Risk Scoring
- Threat Count Analysis
- High / Medium / Low Risk Classification
- Threat Leaderboard

Example:

| Source IP      | Threat Count | Risk   |
| -------------- | ------------ | ------ |
| 20.52.64.201   | 650          | HIGH   |
| 51.116.246.106 | 220          | MEDIUM |
| 204.79.197.203 | 50           | LOW    |

---

# 🗺️ Global Attack Map

Visualize threat origins worldwide.

Features:

- Geo-IP Lookup
- Country Detection
- Interactive World Map
- Top Threat Countries

Technologies:

- Plotly
- IP Geolocation API

---

# 📈 Attack Timeline Analytics

Analyze attack trends over time.

Features:

- Threat Timeline
- Peak Attack Time
- Attack Frequency
- Threat Trends
- Top Attack Hours

Metrics:

- Total Threats
- Peak Threat Count
- Average Threats
- Peak Activity Window

---

# 🌐 Network Attack Graph

Interactive visualization of network communications.

Features:

- Source → Destination Mapping
- Interactive Graph
- Zoom Support
- Drag-and-Drop Nodes
- Threat Relationships

Built using:

- NetworkX
- PyVis

Example:

```text
192.168.1.8
     ↓
20.52.64.201
     ↓
51.116.246.106
     ↓
204.79.197.203
```

---

# 📄 Threat Intelligence Reports

Generate downloadable PDF reports.

Includes:

- Threat Summary
- Top Source IPs
- Top Destination IPs
- Recent Threat Activity
- Security Metrics

One-click PDF Export from Streamlit.

---

# 🏗️ Project Structure

```text
AI-Cyber-Pattern-Detector/
│
├── data/
│   ├── KDDTrain+.txt
│   ├── KDDTest+.txt
│   └── processed_data.csv
│
├── models/
│   └── autoencoder.pth
│
├── outputs/
│   ├── anomaly_results.csv
│   ├── live_monitor_log.csv
│   ├── threat_report.pdf
│   ├── pca_visualization.png
│   ├── tsne_visualization.png
│   └── network_graph.html
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── anomaly_detection.py
│   ├── visualize.py
│   ├── realtime_monitor.py
│   ├── live_packet_monitor.py
│   ├── geo_lookup.py
│   ├── threat_intelligence.py
│   ├── network_graph.py
│   ├── report_generator.py
│   └── app.py
│
└── README.md
```

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/OfficialTanishGupta/AI-Cyber-Pattern-Detector.git

cd AI-Cyber-Pattern-Detector
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Data Preprocessing

```bash
python preprocess.py
```

## Train Autoencoder

```bash
python train.py
```

## Detect Anomalies

```bash
python anomaly_detection.py
```

## Visualizations

```bash
python visualize.py
```

## Live Packet Monitoring

```bash
python live_packet_monitor.py
```

## Launch Dashboard

```bash
streamlit run app.py
```

---

# 🧠 Technologies Used

### Machine Learning

- PyTorch
- NumPy
- Pandas
- Scikit-Learn

### Cybersecurity

- Scapy
- NSL-KDD Dataset

### Visualization

- Matplotlib
- Plotly
- PCA
- t-SNE
- NetworkX
- PyVis

### Dashboard

- Streamlit

### Reporting

- ReportLab

---

# 🎯 Learning Outcomes

This project demonstrates:

- Deep Learning
- Unsupervised Learning
- Anomaly Detection
- Cybersecurity Analytics
- Network Monitoring
- Packet Inspection
- Threat Intelligence
- Data Visualization
- Dashboard Development
- Security Reporting

---

# 👨‍💻 Author

### Tanish Gupta

AI • Machine Learning • Cybersecurity • IoT • Robotics

GitHub:

https://github.com/OfficialTanishGupta

---

# ⭐ Future Enhancements

- Threat Severity Levels
- Email Alert System
- Docker Deployment
- AWS Deployment
- Threat Intelligence APIs
- SIEM Integration
- Advanced IDS Features
- Malware Traffic Detection
