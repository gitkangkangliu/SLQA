import torch
import torch.nn as nn
from torch.nn import Parameter


class VectorMatrixLinear(nn.Module):

    def __init__(self, left_dim: int, right_dim: int):
        super(VectorMatrixLinear, self).__init__()
        self._weight_vector = Parameter(torch.Tensor(left_dim, right_dim))
        # self._softmax = torch.nn.Softmax(dim=-1)
        torch.nn.init.xavier_normal(self._weight_vector)

    def forward(self, vector: torch.Tensor, matrix: torch.Tensor):
        # shape of vector(batch_size, left_dim)
        # shape of matrix(batch_size, right_dim, z)
        batch_size = vector.size(0)
        assert vector.size(0) == matrix.size(0)
        output = torch.bmm(torch.mm(vector, self._weight_vector).reshape((batch_size, 1, -1)), matrix).reshape(
            (batch_size, -1))
        # output = self._softmax(output)
        return output
