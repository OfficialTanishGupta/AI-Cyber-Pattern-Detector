import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

st.markdown(
    """
<style>

[data-testid="stMetric"]{
    border:1px solid #333;
    padding:15px;
    border-radius:10px;
}

</style>
""",
    unsafe_allow_html=True,
)

st.set_page_config(page_title="AI Cyber Threat Detector", page_icon="🛡️", layout="wide")


st.sidebar.title("🛡️ Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Dataset Overview",
        "Anomaly Detection",
        "Real-Time Monitor",
        "SOC Dashboard",
        "Visualizations",
        "About",
    ],
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


elif page == "Real-Time Monitor":

    import numpy as np
    import time

    st.title("🛡️ Real-Time Threat Monitoring")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Traffic Packets", np.random.randint(1000, 5000))

    with col2:
        st.metric("Threats Detected", np.random.randint(1, 100))

    with col3:
        st.metric("System Status", "ACTIVE")

    chart = st.line_chart()

    status_box = st.empty()

    values = []

    for i in range(100):

        threat_score = np.random.uniform(0, 0.05)

        values.append(threat_score)

        chart.add_rows(pd.DataFrame({"Threat Score": [threat_score]}))

        if threat_score > 0.02:

            status_box.error(f"🚨 Threat Score: {threat_score:.4f}")

        else:

            status_box.success(f"✅ Threat Score: {threat_score:.4f}")

        time.sleep(0.1)


elif page == "SOC Dashboard":

    import os

    st.title("🛡️ Security Operations Center")

    log_file = "../outputs/live_monitor_log.csv"

    if os.path.exists(log_file):

        df = pd.read_csv(log_file)

        if len(df) > 0:

            total_packets = len(df)

            threats = df["status"].str.contains("THREAT").sum()

            normals = total_packets - threats

            threat_percent = (threats / total_packets) * 100

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Packets", total_packets)

            with col2:
                st.metric("Threats", threats)

            with col3:
                st.metric("Normal", normals)

            with col4:
                st.metric("Threat %", f"{threat_percent:.2f}%")

            st.subheader("Recent Events")

            st.dataframe(df.tail(50))

            st.subheader("Anomaly Score Trend")

            st.line_chart(df["error"])

        else:

            st.warning("No packet logs yet.")

    else:

        st.warning("Run live_packet_monitor.py first.")


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
