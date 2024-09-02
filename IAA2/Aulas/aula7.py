# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:03:11 2024

@author: migci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# DON'T MODIFY THIS FUNCTION!!!
def plot_svc_boundary(model, ax=None, plot_margin=True, plot_support=True):
    """Plot the decision boundary for a 2D SVC"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 50)
    y = np.linspace(ylim[0], ylim[1], 50)
    Y, X = np.meshgrid(y, x)

    # shape data
    xy = np.vstack([X.ravel(), Y.ravel()]).T

    # get the decision boundary
    P = model.decision_function(xy).reshape(X.shape)

    # plot decision boundary and margins
    if plot_margin:
        levels=[-1, 0, 1]
        linestyles=['--', '-', '--']
    else:
        levels=[0]
        linestyles=['-']
    ax.contour(X, Y, P, colors='k', levels=levels, alpha=0.5, linestyles=linestyles)


    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
                   s=300, linewidth=1, facecolors='none', edgecolors='k')

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

    return ax  # in case plot was created here


C_values = [0.01, 0.1, 1, 10, 100]
gamma_values = [0.01, 0.1, 1, 10, 100]
 # IMPLEMENT YOUR SOLUTIONS BELOW THIS LINE
def g1():
    df = pd.read_csv("crazy_dataset.csv")
    #print(df.head())
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    C = 1.0
    gamma = 1.0
    
    clf= SVC(kernel='rbf', C=C, gamma=gamma)
    clf.fit(X, y)
    #y_pred = clf.predict(X)
    ax = plt.gca()
    ax.set_xlim([-2.0, 2.0])
    ax.set_ylim([-2.0, 2.0])
    # Plot the decision boundary
    plt.figure()
    plot_svc_boundary(clf,ax=ax ,plot_margin=False, plot_support=False)
    plt.title(f"SVM Decision Boundary (C={C}, gamma={gamma})")
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()
g1()