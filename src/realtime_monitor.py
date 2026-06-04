import torch
import pandas as pd
import numpy as np
import time

from model import AutoEncoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Using Device: {device}")


model = AutoEncoder(41).to(device)

model.load_state_dict(torch.load("../models/autoencoder.pth", map_location=device))

model.eval()

print("Model Loaded Successfully")


traffic_data = pd.read_csv("../data/processed_data.csv")

print(f"Traffic Records Loaded: {len(traffic_data)}")


THRESHOLD = 0.019

print(f"Detection Threshold: {THRESHOLD}")


print("\nStarting Monitoring...\n")

total_packets = 100

normal_count = 0
threat_count = 0

for i in range(total_packets):

    # 80% normal traffic
    if np.random.rand() < 0.80:

        random_index = np.random.randint(0, len(traffic_data))

        sample = traffic_data.iloc[random_index, :-1].values.reshape(1, 41)

    else:

        sample = np.random.rand(1, 41)

    tensor_sample = torch.tensor(sample, dtype=torch.float32).to(device)

    with torch.no_grad():

        reconstructed = model(tensor_sample)

        error = torch.mean((tensor_sample - reconstructed) ** 2)

    error = error.item()

    if error > THRESHOLD:

        status = "🚨 THREAT DETECTED"
        threat_count += 1

    else:

        status = "✅ NORMAL"
        normal_count += 1

    print(f"[{i+1:03d}] " f"Error: {error:.6f} | " f"{status}")

    time.sleep(1)


print("\n" + "=" * 50)

print("MONITORING SESSION COMPLETE")

print("=" * 50)

print(f"Total Packets Analysed : {total_packets}")

print(f"Normal Traffic         : {normal_count}")

print(f"Threats Detected       : {threat_count}")

print(f"Threat Percentage      : " f"{(threat_count/total_packets)*100:.2f}%")

print("=" * 50)
