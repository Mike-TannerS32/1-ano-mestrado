# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:15:46 2024

@author: migci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("mnist_small.zip")

#print(df)

X = df.iloc[  : , :-1]
y = df.y
#print(X)
plt.plot(X, y)
plt.show()
row = df.iloc[100 , -1]
print(row)