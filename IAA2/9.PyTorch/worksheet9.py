# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:39:48 2023

@author: migci
"""

import torch
import numpy as np
import random
import pandas as pd
import torch.nn as nn
from sklearn.model_selection import train_test_split
import torch.optim as optim
import matplotlib.pyplot as plt
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import random_split
from torch.utils.data import DataLoader


seed = 0
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)


def load_process():
    df = pd.read_csv("breast-cancer-dataset.zip")
    df.dropna(inplace=True)
    X= df.iloc[:, 2:]
    y= df.diagnosis
    
    
    X = (X- X.mean())/ X.std()
    y.replace("B", 0, inplace=True)
    y.replace("M", 1, inplace=True)
    
    X= torch.tensor(X.to_numpy(), dtype=torch.float32)
    y= torch.tensor(y, dtype=torch.float32)
    y= y.reshape(-1, 1) #alterar a shape do tensor
   
    
    return X, y

#load_process()

def g1q2():
    model = nn.Sequential(nn.Linear(30, 1), nn.Sigmoid())
    
    X, y = load_process()
    
    X_train, X_test, y_train, y_test= train_test_split(X, y, train_size=0.8, random_state=0, stratify=y)
    
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    
    epocs = 20
    train_losses= []; test_losses= []; xaxis_values= []
    
    for e in range(epocs+1):
        optimizer.zero_grad()
        y_pred = model(X_train)
        loss = criterion(y_pred, y_train)
        loss.backward() #calcular gradientes do erro
        optimizer.step() #o optimizador atualiza os valores
        
        if e%1==0:
            model.eval()
            with torch.no_grad():
                train_losses.append(loss.item())
                y_pred = model(X_test)
                loss = criterion(y_pred, y_test)
                test_losses.append(loss.item())
                xaxis_values.append(X)
                print(f'Epoch {e}: Train loss[{train_losses[-1]}] Test loss[{test_losses[-1]} ]')

    fig, ax = plt.subplots(tight_layout= True)
    ax.plot(train_losses,label='Train')
    ax.plot(test_losses, label='Test')
    ax.grid()
    ax.set_xlabel("Epoch"); ax.set_ylabel("loss")
    ax.legend()
    
    model.eval()
    with torch.no_grad():
        y_pred= model(X_test)
        y_pred = y_pred.round()
        total_guesses = (y_pred == y_test).sum().item()
        accuracy = total_guesses / len(y_test)
        print("Accurary", accuracy)
    #print(train_losses)
#g1q2()


def g2q1():
    tx = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5,),(0.5,))])
    
    trainset = datasets.FashionMNIST('/migci/Downloads/Images/Train', train=True, download=True, transform=tx)
    #testset= datasets.FashionMNIST('/migci/Downloads/Images/Test',train=False, download=True, transform=tx)
    
    print(len(trainset))
    #print(len(testset))
    
    #depois de obter dataset é preciso dataloader
    n_train = int(0.8*len(trainset))
    n_val = len(trainset) - n_train
    
    train_set, val_set = random_split(trainset, [n_train, n_val])
    
    train_loader = DataLoader(train_set, batch_size=64, shuffle = True)
    val_loader = DataLoader(val_set, batch_size=64, shuffle= True)
    
    n_input = 784
    
    model = nn.Sequential(nn.Linear(n_input, 128), nn.ReLU(),
                          nn.Linear(128, 10), nn.LogSoftmax())
    
    epochs= 12 #12
    
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.parameters(),lr=0.001)
    train_losses = []; val_losses = []
    for e in range(epochs+1):
        print(f'Epoch {e}: loading....')
        running_loss =0
        for X, y in train_loader:
            optimizer.zero_grad()
            X = X.reshape(X.shape[0], -1)
            #print(X.shape); return
            y_pred = model(X)
            loss = criterion(y_pred, y)
            running_loss += loss.detach().item()
            #train_losses.append(loss.detach().item())
            loss.backward()
            optimizer.step()
        train_losses.append(running_loss / len(train_loader))
        
        print("Evaluating ...")
        model.eval()
        with torch.no_grad():
            running_loss =0
            for X, y in val_loader:
                y_hat= model(X.reshape(X.shape[0],-1))
                loss = criterion(y_hat, y)
                running_loss += loss.item()
                
            val_losses.append(running_loss/ len(val_loader))
    
    
    x_axis_values = list(range(1, epochs+1))
    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(x_axis_values,train_losses, label="Train")
    ax.plot(x_axis_values, val_losses, label="Val")
    ax.legend()
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.grid()
    
    torch.save(model.state_dict(),"apagar.pt")
g2q1()

def g2q9():
    n_input = 784
    
    model = nn.Sequential(nn.Linear(n_input, 128), nn.ReLU(),
                          nn.Linear(128, 10), nn.LogSoftmax())
    
    model.load_state_dict(torch.load("apagar.pt"))
    
    tx = transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5,),(0.5,))])
    testset= datasets.FashionMNIST('/migci/Downloads/Images/Test',train=False, download=True, transform=tx)
    test_loader = DataLoader(testset, batch_size=10,shuffle=False)
    
    correct =0
    
    model.eval()    
    with torch.no_grad():
        for X, y in test_loader:
            y_preds = model(X)
            preds = torch.argmax(y_preds, dim=1)
            correct += (preds == y).sum().item()
    
    accuracy = correct / len(testset)
    print("Accuracy:", accuracy)

#g2q9()








