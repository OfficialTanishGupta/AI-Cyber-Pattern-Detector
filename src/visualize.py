import torch
import pandas as pd
import matplotlib.pyplot as plt

# from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from model import AutoEncoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using Device:", device)


data = pd.read_csv("../data/processed_data.csv")

X = data.iloc[:, :-1].values

y = data.iloc[:, -1].values

X = torch.tensor(X, dtype=torch.float32).to(device)


model = AutoEncoder(41).to(device)

model.load_state_dict(torch.load("../models/autoencoder.pth", map_location=device))

model.eval()

print("Model Loaded")


with torch.no_grad():

    latent_vectors = model.get_latent_features(X)

latent_vectors = latent_vectors.cpu().numpy()

print("Latent Shape:", latent_vectors.shape)

"""
pca = PCA(n_components=2)

pca_result = pca.fit_transform(latent_vectors)

print("PCA Completed")
"""


plt.figure(figsize=(10, 8))

# plt.scatter(pca_result[:, 0], pca_result[:, 1], c=y, alpha=0.5)

plt.title("Cyber Traffic Pattern Visualization")

# plt.xlabel("PCA Component 1")
# plt.ylabel("PCA Component 2")

tsne = TSNE(n_components=2, random_state=42)

tsne_result = tsne.fit_transform(latent_vectors)

plt.colorbar(label="Attack Label")

plt.scatter(tsne_result[:, 0], tsne_result[:, 1], c=y, alpha=0.5)

# plt.savefig("../outputs/pca_visualization.png")

plt.savefig("../outputs/t-SNE_visualization.png")

plt.show()
