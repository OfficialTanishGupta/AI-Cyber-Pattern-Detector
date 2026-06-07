import torch
import numpy as np
import csv
import os
from datetime import datetime

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

from model import AutoEncoder

# ==========================================
# DEVICE SETUP
# ==========================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Using Device: {device}")


# ==========================================
# LOG FILE
# ==========================================

LOG_FILE = "../outputs/live_monitor_log.csv"


def initialize_log_file():

    os.makedirs("../outputs", exist_ok=True)

    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:

        with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(["timestamp", "src_ip", "dst_ip", "error", "status"])


def save_log(src_ip, dst_ip, error, status):

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([datetime.now(), src_ip, dst_ip, float(error), status])


initialize_log_file()


# ==========================================
# LOAD MODEL
# ==========================================

model = AutoEncoder(41).to(device)

model.load_state_dict(torch.load("../models/autoencoder.pth", map_location=device))

model.eval()

print("Autoencoder Loaded Successfully")


# ==========================================
# THRESHOLD
# ==========================================

THRESHOLD = 0.019


packet_count = 0
threat_count = 0


# ==========================================
# FEATURE EXTRACTION
# ==========================================


def packet_to_features(packet):

    features = np.zeros(41)

    # Duration
    features[0] = 0

    # Protocol Type
    if packet.haslayer(TCP):
        features[1] = 0

    elif packet.haslayer(UDP):
        features[1] = 1

    elif packet.haslayer(ICMP):
        features[1] = 2

    # Packet Length
    features[4] = len(packet)

    # TCP Flags
    if packet.haslayer(TCP):
        features[5] = packet[TCP].flags.value

    return features


# ==========================================
# PACKET PROCESSING
# ==========================================


def process_packet(packet):

    global packet_count
    global threat_count

    if not packet.haslayer(IP):
        return

    try:

        packet_count += 1

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        features = packet_to_features(packet)

        tensor = torch.tensor(features, dtype=torch.float32).unsqueeze(0).to(device)

        with torch.no_grad():

            reconstructed = model(tensor)

            error = torch.mean((tensor - reconstructed) ** 2)

        error = float(error.item())

        if error > THRESHOLD:

            threat_count += 1
            status = "THREAT"

        else:

            status = "NORMAL"

        save_log(src_ip, dst_ip, error, status)

        print(
            f"[{packet_count}] "
            f"{src_ip} -> {dst_ip} | "
            f"Error={error:.6f} | "
            f"Status={status}"
        )

    except Exception as e:

        print(f"Packet Processing Error: {e}")


# ==========================================
# START MONITORING
# ==========================================

print("\nStarting Live Packet Monitoring...")
print("Press CTRL+C to Stop\n")

try:

    sniff(prn=process_packet, store=False)

except KeyboardInterrupt:

    print("\nMonitoring Stopped")

    print("\n========== SUMMARY ==========")

    print(f"Packets Analysed: {packet_count}")

    print(f"Threats Detected: {threat_count}")

    print(f"Threat Percentage: " f"{(threat_count/max(packet_count,1))*100:.2f}%")
