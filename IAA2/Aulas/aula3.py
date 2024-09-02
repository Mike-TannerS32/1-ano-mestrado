
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold
import seaborn as sns

def g1():
    df= pd.read_csv("indian_liver_patient.csv")
    #print(df.Dataset) # é o que prevê a presença ou ausencia de doença do figado
    #print("1 indica a presença da doença \n2 indica a auseência da doença")
    #print(df.columns)
    sum1 = 0
    sum2 = 0
    df.dropna(inplace=True)
    f = df.Dataset.values
    for i in range(len(f)):
        if f[i] == 1:
            sum1 += 1
        if f[i] == 2:
            sum2 += 1
    print(sum1/(sum1+sum2))
    X = df.drop(columns = ['Dataset'])
    y = df.Dataset
    
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=3)
    sum1 = 0
    sum2 = 0
    #print(y_train.shape)
    #print(y_test.shape)
    for i in range(len(y_train.values)):
        if y_train.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    print(sum1/(sum1+sum2))
    sum1 =0
    sum2 = 0
    for i in range(len(y_test.values)):
        if y_test.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    print(sum1/(sum1+sum2))
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=3,stratify=y)
    sum1 = 0
    sum2 = 0
    #print(y_train.shape)
    #print(y_test.shape)
    for i in range(len(y_train.values)):
        if y_train.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    print(sum1/(sum1+sum2))
    sum1 =0
    sum2 = 0
    for i in range(len(y_test.values)):
        if y_test.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    print(sum1/(sum1+sum2))
#g1()

def g2():
    df = pd.read_csv("IRIS.csv")
    #print(df.head())
    #print(df["species"].value_counts())
    #print(50/150)
    df['species'].replace(['Iris-setosa','Iris-versicolor','Iris-virginica'], [1,2,3], inplace=True)
    #print(df.corr())
    X = df.drop('species',axis=1)
    y = df.species
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
    #print(df.hist('species'))
    sum1=0
    sum2=0
    f = df.species.values
    for i in range(len(f)):
        if f[i] == 1:
            sum1 += 1
        if f[i] == 2:
            sum2 += 1
    #print(sum1/(sum1+sum2))
    sum1=0
    sum2=0
    #print(y_train.shape, y_test.shape)
    for i in range(len(y_train.values)):
        if y_train.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    #print(sum1/(sum1+sum2))
    sum1 =0
    sum2 = 0
    for i in range(len(y_test.values)):
        if y_test.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    #print(sum1/(sum1+sum2))
    
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0,stratify=y)
    sum1=0
    sum2=0
    print(y_train.shape, y_test.shape)
    for i in range(len(y_train.values)):
        if y_train.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    print(sum1/(sum1+sum2))
    sum1 =0
    sum2 = 0
    for i in range(len(y_test.values)):
        if y_test.values[i] == 1:
            sum1 += 1
        else:
            sum2 += 1
    print(sum1/(sum1+sum2))
#g2()

def g3():
    df = pd.read_csv("IRIS.csv")
    X = df.drop('species',axis=1)
    y = df.species
    kfold = KFold(n_splits=3, shuffle=True, random_state=0)
    for fold, (train_indices, test_indices) in enumerate(kfold.split(X, y), 1):
        X_train, X_test = X.iloc[train_indices], X.iloc[test_indices]
        y_train, y_test = y.iloc[train_indices], y.iloc[test_indices]
        print("====Fold ",fold,"=====")
        print("=Train=")
        print(y_train.value_counts())
        print("=Test=")
        print(y_test.value_counts())
#g3()    

def g4():
    df = pd.read_csv("IRIS.csv")
    X = df.drop('species',axis=1)
    y = df.species
    kfold= StratifiedKFold(n_splits=3, shuffle=True, random_state=0)
    for fold, (train_indices, test_indices) in enumerate(kfold.split(X, y), 1):
        X_train, X_test = X.iloc[train_indices], X.iloc[test_indices]
        y_train, y_test = y.iloc[train_indices], y.iloc[test_indices]
        print("====Fold ",fold,"=====")
        print("=Train=")
        print(y_train.value_counts())
        print("=Test=")
        print(y_test.value_counts())
g4()