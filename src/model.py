import torch
import torch.nn as nn
from torchsummary import summary



class AutoEncoder(nn.Module):

    def __init__(self, input_dim):

        super(AutoEncoder, self).__init__()



        self.encoder = nn.Sequential(

            nn.Linear(input_dim, 32),
            nn.ReLU(),

            nn.Linear(32, 16),
            nn.ReLU(),

            nn.Linear(16, 8),
            nn.ReLU()
        )



        self.decoder = nn.Sequential(

            nn.Linear(8, 16),
            nn.ReLU(),

            nn.Linear(16, 32),
            nn.ReLU(),

            nn.Linear(32, input_dim),
            nn.Sigmoid()
        )



    def forward(self, x):

        encoded = self.encoder(x)

        decoded = self.decoder(encoded)

        return decoded




if __name__ == "__main__":

    input_dimension = 41

    model = AutoEncoder(input_dimension)

    print(model)

    sample_input = torch.rand((1, 41))

    output = model(sample_input)

    print("\nInput Shape:")
    print(sample_input.shape)

    print("\nOutput Shape:")
    print(output.shape)
    
    
    
summary(model, (41,))