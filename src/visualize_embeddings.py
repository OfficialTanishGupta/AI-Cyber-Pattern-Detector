import torch
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from model import AutoEncoder

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using Device:", device)


df = pd.read_csv("../data/processed_data.csv")

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X = torch.tensor(X, dtype=torch.float32).to(device)


model = AutoEncoder(41).to(device)

model.load_state_dict(torch.load("../models/autoencoder.pth", map_location=device))

model.eval()

print("Model Loaded")


with torch.no_grad():
    latent_vectors = model.get_latent_features(X)

latent_vectors = latent_vectors.cpu().numpy()

print("Latent Vector Shape:", latent_vectors.shape)


print("\nRunning PCA...")

pca = PCA(n_components=2)

pca_result = pca.fit_transform(latent_vectors)

plt.figure(figsize=(10, 8))

plt.scatter(pca_result[:, 0], pca_result[:, 1], c=y, alpha=0.5)

plt.title("PCA Visualization of Cyber Traffic")

plt.xlabel("Component 1")
plt.ylabel("Component 2")

plt.colorbar(label="Attack")

plt.savefig("../outputs/pca_visualization.png")

print("PCA image saved.")

plt.close()


print("\nRunning t-SNE...")

# Use subset because t-SNE is slow
sample_size = min(5000, len(latent_vectors))

latent_subset = latent_vectors[:sample_size]
label_subset = y[:sample_size]

tsne = TSNE(n_components=2, random_state=42, perplexity=30)

tsne_result = tsne.fit_transform(latent_subset)

plt.figure(figsize=(10, 8))

plt.scatter(tsne_result[:, 0], tsne_result[:, 1], c=label_subset, alpha=0.5)

plt.title("t-SNE Visualization of Cyber Traffic")

plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")

plt.colorbar(label="Attack")

plt.savefig("../outputs/tsne_visualization.png")

print("t-SNE image saved.")

plt.close()

print("\nVisualization Complete!")
