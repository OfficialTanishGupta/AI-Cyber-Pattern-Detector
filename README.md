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

# 🚀 Features

### ✅ Data Processing Pipeline

- NSL-KDD Dataset Support
- Feature Engineering
- Label Encoding
- Data Normalization
- Tensor Conversion

### ✅ Deep Learning Autoencoder

- Fully Connected Encoder Network
- Latent Space Compression
- Decoder Reconstruction
- Reconstruction Loss Optimization

### ✅ Anomaly Detection Engine

- Reconstruction Error Analysis
- Dynamic Threshold Detection
- Attack Probability Scoring
- Suspicious Traffic Identification

### ✅ Pattern Exploration

- PCA Visualization
- t-SNE Embedding Visualization
- Latent Space Analysis
- Traffic Cluster Discovery

### ✅ Professional Development Workflow

- Git Version Control
- Modular Project Structure
- Reproducible Training Pipeline
- Model Checkpointing

---

# 🧠 Project Architecture

```text
Raw Network Traffic
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
PyTorch Dataset
        │
        ▼
Autoencoder Training
        │
        ▼
Latent Space Learning
        │
        ▼
Reconstruction Error
        │
        ▼
Anomaly Detection
        │
        ▼
Threat Identification
```

---

# 📂 Project Structure

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
│   └── tsne_visualization.png
│
├── src/
│   ├── dataset.py
│   ├── preprocess.py
│   ├── dataset_loader.py
│   ├── model.py
│   ├── train.py
│   ├── anomaly_detection.py
│   └── visualize_embeddings.py
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

## NSL-KDD Dataset

The project uses the NSL-KDD dataset, one of the most widely used benchmark datasets for Intrusion Detection Systems.

### Dataset Includes

- Normal Network Traffic
- Denial of Service (DoS)
- Probe Attacks
- User-to-Root (U2R)
- Remote-to-Local (R2L)

### Features

- 41 Network Features
- Attack Labels
- Multiple Attack Categories

---

# 🔬 Machine Learning Pipeline

## Step 1 — Data Preprocessing

### Operations

- Remove unnecessary columns
- Encode categorical values
- Normalize numerical features
- Convert labels to binary classification

### Output

```text
Normal Traffic → 0
Attack Traffic → 1
```

---

## Step 2 — Autoencoder Training

The model learns compressed representations of network behavior.

### Encoder

```text
41 → 32 → 16 → 8
```

### Decoder

```text
8 → 16 → 32 → 41
```

### Latent Space

The 8-dimensional latent vector captures hidden traffic patterns learned by the AI.

---

## Step 3 — Reconstruction Error Analysis

The model attempts to reconstruct input traffic.

### Normal Traffic

```text
Input ≈ Reconstruction
Low Error
```

### Suspicious Traffic

```text
Input ≠ Reconstruction
High Error
```

The reconstruction error becomes the anomaly score.

---

# 📈 Visualization

The project visualizes learned traffic patterns using:

## PCA

Principal Component Analysis

Used to:

- Reduce dimensionality
- Visualize learned embeddings
- Discover traffic clusters

## t-SNE

t-Distributed Stochastic Neighbor Embedding

Used to:

- Reveal hidden structures
- Identify attack clusters
- Explore latent representations

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Cyber-Pattern-Detector.git

cd AI-Cyber-Pattern-Detector
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Usage

## 1. Preprocess Dataset

```bash
cd src

python preprocess.py
```

---

## 2. Create Dataset Loader

```bash
python dataset_loader.py
```

---

## 3. Train Autoencoder

```bash
python train.py
```

---

## 4. Run Anomaly Detection

```bash
python anomaly_detection.py
```

---

## 5. Generate Visualizations

```bash
python visualize_embeddings.py
```

---

# 📊 Sample Results

### Outputs Generated

```text
outputs/

├── anomaly_results.csv
├── pca_visualization.png
└── tsne_visualization.png
```

### Model Output

```text
Detected Anomalies: XXXX

Normal Traffic: XXXX

Anomaly Percentage: XX%
```

---

# 🛠️ Technologies Used

### Programming

- Python

### Deep Learning

- PyTorch

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib
- Scikit-Learn

### Development Tools

- Git
- GitHub
- VS Code

---

# 🎯 Learning Outcomes

This project demonstrates practical experience in:

### Cybersecurity

- Intrusion Detection Systems
- Threat Detection
- Traffic Analysis
- Anomaly Detection

### Machine Learning

- Deep Learning
- Autoencoders
- Feature Engineering
- Representation Learning

### PyTorch

- Custom Datasets
- DataLoaders
- Model Training
- GPU Acceleration
- Model Serialization

---

# 🚀 Future Improvements

### Planned Features

- Streamlit Dashboard
- Real-Time Packet Monitoring
- Live Network Sniffing
- Transformer-Based IDS
- Threat Classification
- Explainable AI Visualizations
- SIEM Integration
- Deployment on Cloud

---

# 📸 Screenshots

Add screenshots here after generating outputs.

### PCA Visualization

```text
Insert PCA Visualization Image
```

### t-SNE Visualization

```text
Insert t-SNE Visualization Image
```

### Dashboard Preview

```text
Coming Soon
```

---

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