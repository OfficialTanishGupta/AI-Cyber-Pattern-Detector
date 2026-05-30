import torch
import torch.nn as nn
import pandas as pd
import numpy as np

from model import AutoEncoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using Device:", device)


data = pd.read_csv("../data/processed_data.csv")

X = data.iloc[:, :-1].values

X = torch.tensor(X, dtype=torch.float32).to(device)


model = AutoEncoder(41).to(device)

model.load_state_dict(torch.load("../models/autoencoder.pth", map_location=device))

model.eval()

print("Model Loaded Successfully")


with torch.no_grad():

    reconstructed = model(X)


errors = torch.mean((X - reconstructed) ** 2, dim=1)

errors = errors.cpu().numpy()

print("\nFirst 10 Reconstruction Errors:\n")

for i in range(10):
    print(errors[i])


threshold = np.percentile(errors, 95)

print(f"\nAnomaly Threshold: {threshold:.6f}")


anomalies = errors > threshold

print("\n========== RESULTS ==========")

print(f"Total Samples: {len(errors)}")

print(f"Detected Anomalies: {anomalies.sum()}")

print(f"Normal Traffic: {len(errors)-anomalies.sum()}")

print(f"Anomaly Percentage: " f"{(anomalies.sum()/len(errors))*100:.2f}%")


results = pd.DataFrame({"reconstruction_error": errors, "anomaly": anomalies})

results.to_csv("../outputs/anomaly_results.csv", index=False)

print("\nResults saved to outputs")
