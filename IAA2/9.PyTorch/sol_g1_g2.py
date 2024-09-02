import torch
import numpy as np
import random
import pandas as pd
import torch.nn as nn
from sklearn.model_selection import train_test_split
import torch.optim as optim
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

import torchvision.datasets as datasets
import torchvision.transforms as transforms




seed = 0
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)


def load_preprocess():
    df = pd.read_csv("/home/aanjos/Documents/Datasets/breast-cancer.zip")
    df.dropna(inplace=True)
    
    X = df.iloc[:, 2:]
    y = df.diagnosis
    
    X = (X - X.mean()) / X.std()
    
    y.replace("B", 0, inplace=True)
    y.replace("M", 1, inplace=True)
    
    X = torch.tensor(X.to_numpy(), dtype=torch.float32)
    y = torch.tensor(y.to_numpy(), dtype=torch.float32)
    y = y.reshape(-1, 1)
    
    return X, y


#load_preprocess()



# no batches are used in this group (i.e., no Dataset or DataLoader instances used)
def g1q2():
    model = nn.Sequential(nn.Linear(30, 1), nn.Sigmoid())
    
    X, y = load_preprocess()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, stratify=y, random_state=seed)
    
    criterion = nn.BCELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    epochs = 2050
    
    train_losses = []
    test_losses = []
    
    x_axis_values = []
    
    for e in range(1, epochs+1):
        model.train()

        y_hat = model.forward(X_train)
        loss = criterion(y_hat, y_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if e % 10 == 0:
            x_axis_values.append(e)
            model.eval()
            train_losses.append(loss.detach().item())
            with torch.no_grad():
                y_hat = model(X_test)
                loss = criterion(y_hat, y_test)
                test_losses.append(loss.detach().item())
                
            print(f"Epoch {e}, Train loss {round(train_losses[-1], 4)}, Test loss {round(test_losses[-1], 4)}")
        
    
    # accuracy
    model.eval()
    with torch.no_grad():
        y_pred = model(X_test)
        t = 0.5
        y_pred[y_pred < t] = 0
        y_pred[y_pred >= t] = 1
        #preds = y_pred.numpy().round()  # this is an alternative to the two lines above

        #total_correct = (y_test == y_pred).sum().item()
        #acc = total_correct / len(y_test)
        acc = accuracy_score(y_test, y_pred) # this is an alternative to the two lines above
        print("Accuracy:", acc)

    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(x_axis_values, train_losses, label="Train")
    ax.plot(x_axis_values, test_losses, label="Test")
    ax.legend()
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.grid()
                
    print(confusion_matrix(y_test, y_pred))


#g1q2()


# here we do things as they are supposed to be done (i.e., using a validation set)
def g2q1():
    tx = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    trainset = datasets.FashionMNIST("~/.pytorch/F_MNIST_data/", train=True, download=True, transform=tx)
    #testset = datasets.FashionMNIST("~/.pytorch/F_MNIST_data/", train=False, download=True, transform=tx)
    
    val_size = int(0.2*len(trainset))
    train_size = len(trainset) - val_size
    trainset, valset = torch.utils.data.random_split(trainset, [train_size, val_size])
    
    train_loader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
    val_loader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=False)
    
    input_size = 28*28
    
    model = nn.Sequential(nn.Linear(input_size, 128), nn.ReLU(),
                          nn.Linear(128, 10), nn.LogSoftmax())
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    n = 12#40
    
    train_losses = []
    val_losses = []
    
    for e in range(1, n+1):
        print(f"Epoch {e}; Training ...")
        model.train()
        running_loss = 0
        for X, y in train_loader:
            X = X.reshape(X.shape[0], -1)
            y_pred = model(X)
            loss = criterion(y_pred, y)  # average loss per batch
            running_loss += loss.detach().item()  # sum of losses of all batches
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        train_losses.append(running_loss/len(train_loader))  # average loss per epoch
        
        print("Evaluating ...")
        model.eval()
        with torch.no_grad():
            running_loss = 0
            for X, y in val_loader:
                y_hat = model(X.reshape(X.shape[0], -1))
                loss = criterion(y_hat, y)
                running_loss += loss.item()
            
            val_losses.append(running_loss/len(val_loader))
        
        print(f"Train loss {round(train_losses[-1], 3)}, Val loss {round(val_losses[-1], 3)}")
        
    x_axis_values = list(range(1, n+1))
    fig, ax = plt.subplots(tight_layout=True)
    ax.plot(x_axis_values, train_losses, label="Train")
    ax.plot(x_axis_values, val_losses, label="Val")
    ax.legend()
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.grid()
    
    torch.save(model.state_dict(), f"./model_{n}.pt")
    

#g2q1()


# Report the accuracy (or other performance metrics) using the test set
def g2q9():
    input_size = 28*28
    model = nn.Sequential(nn.Linear(input_size, 128), nn.ReLU(),
                          nn.Linear(128, 10), nn.LogSoftmax())
    model.load_state_dict(torch.load("./model_12.pt"))
    
    tx = transforms.Compose([transforms.ToTensor(), transforms.Normalize(0.5, 0.5)])    
    testset = datasets.FashionMNIST("~/.pytorch/F_MNIST_data/", train=False, download=True, transform=tx)
    test_loader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)
    
    correct = 0
    
    model.eval()
    with torch.no_grad():
        for X, y in test_loader:
            X = X.reshape(X.shape[0], -1)
            y_preds = model(X)
            preds = torch.argmax(y_preds, dim=1)
            correct += (preds == y).sum().item()
    
    accuracy = correct / len(testset)
    print("Accuracy:", accuracy)


#g2q9()


