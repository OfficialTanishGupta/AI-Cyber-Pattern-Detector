import pandas as pd

# Load dataset
train_path = "../data/KDDTrain+.txt"

df = pd.read_csv(train_path, header=None)

print(df.head())

print("\nDataset Shape:")
print(df.shape)