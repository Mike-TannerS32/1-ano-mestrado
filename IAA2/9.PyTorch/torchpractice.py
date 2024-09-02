# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:26:27 2023

@author: migci
"""

import torch
import torch.nn as nn

'''
neuron  = nn.Sequential(
    nn.Linear(2, 1),
    nn.Sigmoid()
)

x= torch.tensor([1.,2.])
yhat= neuron(x)
print(yhat.item())
'''
class Neuron(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 1)
        self.activation = nn.Sigmoid()
    def forward(self, x):
        logit = self.linear(x)
        yhat = self.activation(logit)
        return yhat

neuron = Neuron()
x = torch.tensor([1., 2.])
yhat = neuron(x)
print(yhat.item())