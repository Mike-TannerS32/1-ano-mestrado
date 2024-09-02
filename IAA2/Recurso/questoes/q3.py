# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:31:27 2024

@author: migci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("mnist_small.zip")

X  = df.iloc[: , :-1]
y = df.y
X = (X- X.mean()) / X.std()

X_train,X_test, y_train,  y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))
print("F1-score", f1_score(y_test, y_pred,average='weighted'))