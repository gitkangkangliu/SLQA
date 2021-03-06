import torch
from torch import nn

class SelfAttentionLayer(nn.Module):
    def __init__(self, input_dim):
        super(SelfAttentionLayer, self).__init__()
        self._input_dim = input_dim
        self._linear = torch.nn.Linear(in_features=input_dim, out_features=input_dim, bias=False)

    def forward(self, d):
        # d: (batch_size, length, encoding_dim)
        # return D W D^T
        return torch.bmm(self._linear(d), d.transpose(2, 1))
