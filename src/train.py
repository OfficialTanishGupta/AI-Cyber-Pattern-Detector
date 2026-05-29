import torch
import torch.nn as nn
import torch.optim as optim

from torch.utils.data import DataLoader

from dataset_loader import CyberDataset
from model import AutoEncoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using Device:", device)


dataset = CyberDataset("../data/processed_data.csv")

dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

print("Dataset Loaded")


input_dimension = 41

model = AutoEncoder(input_dimension).to(device)

print("\nModel Loaded")


criterion = nn.MSELoss()


optimizer = optim.Adam(model.parameters(), lr=0.001)


num_epochs = 20

print("\nTraining Started...\n")

for epoch in range(num_epochs):

    running_loss = 0.0

    for batch_X, _ in dataloader:

        # Move to GPU/CPU
        batch_X = batch_X.to(device)

        outputs = model(batch_X)

        loss = criterion(outputs, batch_X)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    epoch_loss = running_loss / len(dataloader)

    print(f"Epoch [{epoch+1}/{num_epochs}] " f"Loss: {epoch_loss:.6f}")

print("\nTraining Completed")


torch.save(model.state_dict(), "../models/autoencoder.pth")

print("\nModel Saved Successfully")
