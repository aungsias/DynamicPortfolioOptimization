import torch
import pandas as pd

from .metrics import neg_sharpe_ratio, portfolio_risk
from typing import Callable

class LSTMPortfolioOptimizer(torch.nn.Module):
    """
    A neural network model designed for portfolio optimization using LSTM layers.
    
    Attributes / Layers:
    - lstm (torch.nn.LSTM): LSTM layer for sequence modeling.
    - fc (torch.nn.Linear): Fully connected layer for transforming LSTM outputs.
    - softmax (torch.nn.Softmax): Softmax layer for producing probability distributions.
    """
    
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        """
        Initializes the PortfolioOptimizationNN with the given dimensions.
        
        Parameters:
        - input_size (int): The number of input features.
        - hidden_size (int): The number of hidden LSTM units.
        - output_size (int): The size of the output.
        """
        super().__init__()
        self.lstm = torch.nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = torch.nn.Linear(hidden_size, output_size, bias=True)
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Defines the forward pass of the model.
        
        Parameters:
        - x (torch.Tensor): The input tensor with shape (batch_size, sequence_length, input_size).
        
        Returns:
        - output (torch.Tensor): The output probability distributions for each sample in the batch.
        """
        lstm_out, _ = self.lstm(x)
        lstm_out_last = lstm_out[:, -1, :]
        fc_out = self.fc(lstm_out_last)
        output = self.softmax(fc_out)
        return output