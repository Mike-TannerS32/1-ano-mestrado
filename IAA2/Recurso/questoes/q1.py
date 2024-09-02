# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 11:37:47 2024

@author: migci
"""

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv("marks_exam.zip")


sum = df.isnull().sum()
print(sum)


#print(df)
X = pd.DataFrame(df).iloc[:, :4]
X = X.fillna(0)
y = df.test_score
y = y.fillna(0)
X_train,X_test, y_train,  y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LinearRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print('Mean Squared Error', mean_squared_error(y_test, y_pred))

