import torch
import pandas as pd
import numpy as np
import time

from model import AutoEncoder

# ==========================
# DEVICE
# ==========================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ==========================
# LOAD MODEL
# ==========================

model = AutoEncoder(41).to(device)

model.load_state_dict(
    torch.load(
        "../models/autoencoder.pth",
        map_location=device
    )
)

model.eval()

print("Model Loaded Successfully")

# ==========================
# THRESHOLD
# ==========================

THRESHOLD = 0.02

# ==========================
# SIMULATION LOOP
# ==========================

while True:

    sample = np.random.rand(1, 41)

    tensor_sample = torch.tensor(
        sample,
        dtype=torch.float32
    ).to(device)

    with torch.no_grad():

        reconstructed = model(
            tensor_sample
        )

        error = torch.mean(
            (tensor_sample - reconstructed) ** 2
        )

    error = error.item()

    if error > THRESHOLD:
        status = "🚨 THREAT DETECTED"
    else:
        status = "✅ NORMAL"

    print(
        f"Error: {error:.6f} | {status}"
    )

    time.sleep(1)