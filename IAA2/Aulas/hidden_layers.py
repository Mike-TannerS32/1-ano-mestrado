# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:09:45 2024

@author: migci
"""

import numpy as np
import nnfs
import keras 
#print(keras.__version__)
nnfs.init()

X = [[1, 2, 3, 2.5], 
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

'''
inputs = [0,2,-1, 3.3, -2.7, 1.1, 2.2, -100]
output = []


for i in inputs:
    output.append(max(0,i))

print(output)
'''

class layer_dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 *np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = (np.dot(inputs, self.weights) + self.biases)


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer1 = layer_dense(4,5)
layer2 = layer_dense(5,2)

layer1.forward(X)
#print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)
