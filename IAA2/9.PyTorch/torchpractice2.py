# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:39:03 2023

@author: migci
"""

import torch.nn as nn

class My_Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(2, 2) # layer 1
        self.linear2 = nn.Linear(2, 1) # output
        self.activation = nn.Sigmoid()
    def forward(self, x):
        h = self.linear1(x)
        h = self.activation(h)
        yhat = self.linear2(h)
        return self.activation(yhat)
    
model = My_Model()
x = torch.tensor([1., 2.])
yhat = model(x) # i.e., forward pass
print(yhat.item())