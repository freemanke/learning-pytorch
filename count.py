import torch
from torch import nn

class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.parameter(torch.rand(1))
        self.bias = nn.parameter(torch.rand(1))

    def forward(self, input):
        return (input*self.weight)+self.bias

if __name__ == "__main__":
    model = LinearModel()
    x = torch.tensor(3)
    y = model(x)