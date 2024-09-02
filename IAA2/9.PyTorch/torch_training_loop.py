# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:42:07 2023

@author: migci
"""

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

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
criterion = nn.BCELoss() # expects a Sigmoid in the output layer
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
train_losses = []

for epoch in range(100):
    running_loss = 0
    
    for X, y in train_loader:
        yhat = model(X) # forward pass
        loss = criterion(yhat, y)
        running_loss += loss.detach().item() # average loss per batch
        optimizer.zero_grad() # reset gradients
        loss.backward() # backward pass (new gradients of loss)
        optimizer.step() # update weights with new gradients
    train_losses.append(running_loss/len(train_loader)) # avg loss per epoch

plt.plot(train_losses, label='train')
plt.legend()
plt.show()