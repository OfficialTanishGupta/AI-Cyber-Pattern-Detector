import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

st.set_page_config(page_title="AI Cyber Threat Detector", page_icon="🛡️", layout="wide")


st.sidebar.title("🛡️ Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Home", "Dataset Overview", "Anomaly Detection", "Visualizations", "About"],
)


if page == "Home":

    st.title("🛡️ AI Cyber Threat Pattern Detector")

    st.markdown("""
    ### Intelligent Network Traffic Analysis Using Deep Learning

    This project uses a PyTorch Autoencoder to learn normal
    network traffic patterns and identify suspicious behavior
    through reconstruction error analysis.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "Autoencoder")

    with col2:
        st.metric("Framework", "PyTorch")

    with col3:
        st.metric("Use Case", "Anomaly Detection")

    st.success("Project Successfully Loaded")


elif page == "Dataset Overview":

    st.title("📊 Dataset Overview")

    try:

        df = pd.read_csv("../data/processed_data.csv")

        st.write("Dataset Shape:", df.shape)

        st.dataframe(df.head())

        attack_count = df["attack"].value_counts()

        st.subheader("Attack Distribution")

        st.bar_chart(attack_count)

    except Exception as e:

        st.error(f"Error Loading Dataset: {e}")


elif page == "Anomaly Detection":

    st.title("🚨 Threat Analysis")

    try:

        results = pd.read_csv("../outputs/anomaly_results.csv")

        total_samples = len(results)

        anomalies = results["anomaly"].sum()

        normal = total_samples - anomalies

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Total Samples", total_samples)

        with col2:
            st.metric("Anomalies", anomalies)

        with col3:
            st.metric("Normal Traffic", normal)

        st.subheader("Detection Results")

        st.dataframe(results.head(20))

    except Exception as e:

        st.error(f"Error Loading Results: {e}")


elif page == "Visualizations":

    st.title("📈 Traffic Pattern Visualizations")

    pca_path = "../outputs/pca_visualization.png"

    tsne_path = "../outputs/tsne_visualization.png"

    if os.path.exists(pca_path):

        st.subheader("PCA Visualization")

        st.image(pca_path, use_container_width=True)

    if os.path.exists(tsne_path):

        st.subheader("t-SNE Visualization")

        st.image(tsne_path, use_container_width=True)


elif page == "About":

    st.title("ℹ️ About Project")

    st.markdown("""
    ## AI Cyber Threat Pattern Detector

    Developed using:

    - PyTorch
    - Streamlit
    - Autoencoders
    - NSL-KDD Dataset

    Features:

    - Pattern Discovery
    - Anomaly Detection
    - Latent Space Visualization
    - Cybersecurity Analytics

    Developed by Tanish Gupta
    """)
