# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:15:08 2023

@author: migci
"""
import torch
import torch.nn as nn
import torch.utils.data.dataloader
import numpy as np
from sklearn.model_selection import train_test_split
#import matplotlib.pyplot as plt

'''class My_Dataset(Dataset):
    def __init__(self, data, transform=None, target_transform=None):
        self.data = data
        self.transform = transform
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        X = self.data[idx, :-1]; y = self.data[idx, -1]
        if self.transform: # only checking for feature transformation
            X = self.transform(X)
        return X, y
#test_loader pertence à classe Dataloader
'''
x = np.arange(1, 25).reshape(12, 2) 
y = np.array([0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
x_train, x_test, y_train, y_test = train_test_split(x, y)
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
train_loader = Dataloader()
accuracy = 0
model.eval()
with torch.no_grad():
    for X, y in test_loader:
        yhat = model.forward(X)
        test_losses.append(criterion(yhat, y).item())
        preds = yhat.argmax(dim=1)
        accuracy += (preds == y).sum().item()
print("Loss:", sum(test_losses)/len(test_losses))
print("Accuracy:", accuracy/len(test_set))