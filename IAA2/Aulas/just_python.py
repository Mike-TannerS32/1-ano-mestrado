# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:55:23 2024

@author: migci
"""
#import numpy as np

# inputs * weights + bias
inputs = [1,2,3, 2.5] #não se podem mudar os inputs

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

some_value = -0.5
weight= 0.7
bias = 0.7



#shape - por cada dimensão ,qual o tamanho dessa dimensão
#tensor - objeto que pode ser representado como um array
# usar dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]



layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output=0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)
