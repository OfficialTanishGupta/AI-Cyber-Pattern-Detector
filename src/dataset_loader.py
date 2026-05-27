import pandas as pd
import torch

from torch.utils.data import Dataset
from torch.utils.data import DataLoader



class CyberDataset(Dataset):

    def __init__(self, csv_file):

       
        self.data = pd.read_csv(csv_file)

        self.X = self.data.iloc[:, :-1].values


        self.y = self.data.iloc[:, -1].values


        self.X = torch.tensor(
            self.X,
            dtype=torch.float32
        )

        self.y = torch.tensor(
            self.y,
            dtype=torch.float32
        )


    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]




dataset = CyberDataset(
    "../data/processed_data.csv"
)

print("Dataset Loaded Successfully")


dataloader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)

print("DataLoader Created Successfully")



for batch_X, batch_y in dataloader:

    print("\nBatch Features Shape:")
    print(batch_X.shape)

    print("\nBatch Labels Shape:")
    print(batch_y.shape)

    print("\nFirst Sample:")
    print(batch_X[0])

    break



# =========================
# DEVICE CONFIGURATION
# =========================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print("Using Device:", device)