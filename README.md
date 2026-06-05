# 🛡️ AI Cyber Threat Pattern Detector

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red.svg)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Anomaly%20Detection-green.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Autoencoder-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

### Intelligent Network Traffic Analysis using Deep Learning and Anomaly Detection

Detect suspicious network activity by learning normal traffic behavior through Autoencoders, Latent Space Representation Learning, and Pattern Discovery.

</div>

---

# 📌 Overview

Traditional Intrusion Detection Systems (IDS) rely heavily on predefined rules and attack signatures.

This project takes a different approach.

Using Deep Learning and PyTorch, the model learns the normal behavior of network traffic and identifies suspicious activity based on reconstruction error.

Instead of asking:

> "Is this a known attack?"

The system asks:

> "Does this traffic pattern look abnormal?"

This approach enables detection of previously unseen threats and zero-day attack patterns.

---

## 🚀 Features

### Data Processing Pipeline

- NSL-KDD Dataset Support
- Feature Engineering
- Label Encoding
- Data Normalization
- Tensor Conversion

### Deep Learning Autoencoder

- Encoder-Decoder Architecture
- Latent Space Representation Learning
- Reconstruction Error Analysis
- Anomaly Scoring

### Threat Detection Engine

- Unsupervised Anomaly Detection
- Dynamic Thresholding
- Suspicious Traffic Identification
- Threat Percentage Reporting

### Visualization & Analytics

- PCA-Based Embedding Visualization
- t-SNE Cluster Analysis
- Traffic Pattern Exploration
- Latent Space Analysis

### Interactive Dashboard

- Streamlit-Based User Interface
- Dataset Exploration
- Threat Statistics
- Anomaly Detection Results
- Real-Time Monitoring Simulation

### Live Packet Monitoring

- Packet Capture using Scapy
- Live Traffic Inspection
- Source/Destination IP Tracking
- Real-Time Anomaly Scoring
- Experimental IDS Prototype

---

## 📂 Updated Project Structure

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
│   ├── pca_visualization.png
│   ├── tsne_visualization.png
│   └── live_monitor_log.csv
│
├── src/
│   ├── preprocess.py
│   ├── dataset_loader.py
│   ├── model.py
│   ├── train.py
│   ├── anomaly_detection.py
│   ├── visualize_embeddings.py
│   ├── realtime_monitor.py
│   ├── live_packet_monitor.py
│   └── app.py
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore

```

---

## ⚠️ Live Packet Monitoring Disclaimer

The live packet monitoring module demonstrates real-time packet acquisition using Scapy and integration with the trained anomaly detection model.

The Autoencoder was trained using the NSL-KDD dataset, which contains connection-level engineered features. Live packet capture currently uses an approximate feature mapping derived from packet metadata such as protocol, packet size, and TCP flags.

Therefore:

- Real packet capture is fully functional.
- Live anomaly scoring is functional.
- The live IDS should be considered a prototype implementation.
- Production-grade accuracy would require full NSL-KDD-style connection feature extraction.

This module is included to demonstrate practical integration of deep learning models with real network traffic.

---

## 🚀 Future Improvements

### Planned Enhancements

- Real-Time Dashboard Streaming
- Live Threat Alerts
- Packet Logging Database
- Advanced Packet Feature Engineering
- Connection-Level Traffic Analysis
- Transformer-Based Anomaly Detection
- Explainable AI (XAI) Visualizations
- Cloud Deployment
- SIEM Integration
- Enterprise SOC Dashboard

---

## 🎯 Current Capabilities

✅ Data Preprocessing Pipeline

✅ PyTorch Autoencoder Training

✅ Reconstruction Error-Based Detection

✅ Anomaly Detection Engine

✅ PCA Visualization

✅ t-SNE Visualization

✅ Interactive Streamlit Dashboard

✅ Real-Time Traffic Simulation

✅ Live Packet Capture using Scapy

✅ Experimental AI-Powered IDS Prototype

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 📢 Share with others

---

# 👨‍💻 Author

### Tanish Gupta

AI Engineer | Machine Learning Enthusiast | Cybersecurity Explorer

Passionate about building intelligent systems using AI, Deep Learning, Cybersecurity, Robotics, and IoT technologies.

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute for educational and research purposes.
