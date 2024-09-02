# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:59:17 2024

@author: migci
"""
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
#import pickle
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def question1():
    df = pd.read_csv("kc_house_data.csv")
    X = df.sqft_living.values.reshape(-1,1)
    y = df.price.values.reshape(-1,1)
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)
    print(mean_squared_error(y, y_pred))
#question1()

def question1_g2():
    df = pd.read_csv("kc_house_data.csv")
    numeric_df = df.select_dtypes(include=[np.number])
    correlationmatrix = numeric_df.corr()
    correlation_price = correlationmatrix['price'].abs().sort_values(ascending=False)
    
    toptwovars= correlation_price[1:3]
    print(toptwovars)
#question1_g2()

def question2_3_g2():
    df = pd.read_csv("kc_house_data.csv")
    features = ["sqft_living", "grade"]
    X = df[features].values
    X_bias = np.c_[np.ones((len(X), 1)), X]
    y = df['price'].values.reshape(-1,1)
    theta_ols = np.linalg.inv(X_bias.T.dot(X_bias)).dot(X_bias.T).dot(y)
    print(theta_ols)
    
    new = df[features].head().values
    new_bias = np.c_[np.ones((len(new), 1)),new]
    pred = new_bias.dot(theta_ols)
    print("Predictions ")
    print(pred)
    sqft_living = df['sqft_living'].values
    grade = df['grade'].values
    #fig, axs = plt.subplots(1, 1, subplot_kw=dict(projection='3d'))
    #axs.scatter(sqft_living,grade, y)
    
    #sqft_axis = np.linspace(sqft_living.min(), sqft_living.max(), 100)
    #grade_axis = np.linspace(grade.min(), grade.max(), 100)
    #sqfts, grades = np.meshgrid(sqft_axis, grade_axis)
    #prices = theta_ols[0] + theta_ols[1]*sqfts + theta_ols[2]*grades
    
    #axs.plot_surface(sqfts, grades, prices, alpha=0.5, cmap = 'viridis')
    sqft_living_new = 2000
    grade_new = 7
    new= np.array([1,sqft_living_new, grade_new])
    pred_price = new.dot(theta_ols)
    print("Predicted price: ",pred_price[0])
#question2_3_g2()

def question1_g3():
    df = pd.read_csv("kc_house_data.csv")
    features = ["sqft_living", "grade"]
    X = df[features].values
    X_bias = np.c_[np.ones((len(X), 1)), X]
    y = df['price'].values.reshape(-1,1)
    theta_ols = np.linalg.inv(X_bias.T.dot(X_bias)).dot(X_bias.T).dot(y)
    
    model = LinearRegression()
    model.fit(X,y)
    new= np.array([[2000,7]])
    pred_price = model.predict(new)
    sqft_living = df['sqft_living'].values
    grade = df['grade'].values
    print("Predicted price: ", pred_price)
    print("Coefficients ", model.coef_)
    print("Intercept ",model.intercept_)
    fig, axs = plt.subplots(1, 1, subplot_kw=dict(projection='3d'))
    axs.scatter(sqft_living,grade, y)
    
    sqft_axis = np.linspace(sqft_living.min(), sqft_living.max(), 100)
    grade_axis = np.linspace(grade.min(), grade.max(), 100)
    sqfts, grades = np.meshgrid(sqft_axis, grade_axis)
    prices = theta_ols[0] + theta_ols[1]*sqfts + theta_ols[2]*grades
    
    axs.plot_surface(sqfts, grades, prices, alpha=0.5, cmap = 'viridis')
    #print("Mean squared error: ", mean_squared_error(y, pred_price))
question1_g3()

def group4():
    df = pd.read_csv("kc_house_data.csv")
    features = ["sqft_living", "grade","waterfront",
                "sqft_basement", "sqft_lot", "view",
                "yr_built", "bedrooms", "condition",
                "yr_renovated", "bathrooms", "sqft_living15",
                "floors", "sqft_above", "sqft_lot15"]
    X = df[features].values
    y = df['price'].values.reshape(-1,1)
    model = LinearRegression()
    model.fit(X,y)
    #new= np.array([[2000,7]])
    pred_price = model.predict(X)
    print("Predicted price: ", pred_price)
    print("Coefficients ", model.coef_)
    print("Intercept ",model.intercept_)
    print("Mean squared error: ", mean_squared_error(y, pred_price))
#group4()