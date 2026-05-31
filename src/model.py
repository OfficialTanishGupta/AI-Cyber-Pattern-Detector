import torch
import torch.nn as nn

# Optional: Install using
# pip install torchinfo
from torchinfo import summary


class AutoEncoder(nn.Module):
    def __init__(self, input_dim):
        super(AutoEncoder, self).__init__()

        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
        )

        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(8, 16),
            nn.ReLU(),
            nn.Linear(16, 32),
            nn.ReLU(),
            nn.Linear(32, input_dim),
            nn.Sigmoid(),
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

    def get_latent_features(self, x):
        return self.encoder(x)


if __name__ == "__main__":

    print("Creating Model...")

    input_dimension = 41

    model = AutoEncoder(input_dimension)

    print("\nModel Architecture:")
    print(model)

    sample_input = torch.rand((1, 41))

    output = model(sample_input)

    print("\nInput Shape:")
    print(sample_input.shape)

    print("\nOutput Shape:")
    print(output.shape)

    print("\nLatent Feature Shape:")
    latent = model.get_latent_features(sample_input)
    print(latent.shape)

    print("\nModel Summary:")
    summary(model, input_size=(1, 41))

    print("\nModel Test Completed Successfully!")
