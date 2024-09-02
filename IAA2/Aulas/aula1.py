import numpy as np
from numpy.linalg import pinv
import pandas as pd
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
#from sklearn.preprocessing import LabelEncoder 
from sklearn.metrics import mean_squared_error
import pickle

def question1():
    df = pd.read_csv("kc_house_data.csv")
    #print(df.columns)
    features = df.drop('price', axis=1)
    #print(df.shape[0], df.shape[1])
    #print(df.columns)
    #print(df.head(5))
    #print(df.corr())
    #print(df[123:124].max())
    #print(df.tail())
    #print(df.describe())
    print(features.shape[1])
    #print(df.isnull().sum())
    print(df.shape)
    print(df.isnull().sum())
#question1()

def question2():
    df = pd.read_csv("kc_house_data.csv")
    df = df.drop('date', axis=1)
    #df = df.drop('yr_built', axis=1)
    #print(df.head())
    #corr= df.corrwith( df.sqft_lot15 ,axis=0)
    #sorted_corr = corr.unstack().sort_values()
    #print(sorted_corr)
    print(df.corr())
    df_corr_impact_action_yn = df[df.columns[0:17]].corr()['sqft_living'][:-1]
    #set fig size
    fig, ax = plt.subplots(figsize=(30,25))
    #plot matrix
    #sns.heatmap(df_corr_impact_action_yn.to_frame(),annot=True, annot_kws={'size':12},cmap="GnBu")
    plt.show()
#question2()

def question3():
    df = pd.read_csv("kc_house_data.csv")
    #areas = df.sqft_living.values
    #ones = np.ones(len(areas))
    #X = np.vstack([ones, areas]).T
    X = df.sqft_living.values.reshape(-1,1)
    y = df.price.values.reshape(-1,1)
    
    X_bias = np.c_[np.ones((len(X),1)),X]
    
    theta_pinv = pinv(X_bias).dot(y)
    
    print(theta_pinv)
    
    plt.scatter(X, y, alpha=0.5)
    plt.plot(X, X_bias.dot(theta_pinv), color='red', linewidth=2)
    plt.title('Linear Regression Model using pinv')
    plt.xlabel('Sqft Living')
    plt.ylabel('Price')
    plt.show()  
    #Thetas = pinv(X)@y
    #theta0 = Thetas[0,0] #b
    #theta1 = Thetas[1,0] #m
#question3()

def question1_g2():
    df = pd.read_csv("kc_house_data.csv")
    X = df.sqft_living
    y = df.price.values.reshape(-1,1)
    X = X.values.reshape(-1,1)
    #X_train, X_tesmt, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=0)
    model = LinearRegression()
    model.fit(X, y)
    print(model.score(X, y))
    #print(model.coef_)
    #print(model.intercept_)
    #print(model.predict([[2000]]))
    fig, ax = plt.subplots(1, 1)
    ax.scatter(X,y, s=1)
    min_area = X.min()
    max_area = y.max()
    xs = np.arange(min_area,max_area)
    ys = model.predict(xs.reshape(-1,1))
    ax.plot(xs, ys, c='r')
    ax.scatter(2000, model.predict([[2000]]).flatten())
    plt.show()
    
    #y_pred = model.predict(X_test)
    #mse = mean_squared_error(y_test, y_pred)
    #r2 = r2_score(y_test, y_pred)
    #model.evaluate(X_test, y_test, verbose=2)
    #print("MSE: ", mse)
    #print("R2: ", r2)
    #plt.scatter(X_test, y_test, color='black')
    #plt.plot(X_test, y_pred, color='blue', linewidth=3)
    #plt.xlabel('sqft_living')
    #plt.ylabel('Price')
    #plt.title('Linear Regression: sqft_living vs. Price')
    #plt.show()
    with open("model_pickle2","wb") as f:
        pickle.dump(model, f)
question1_g2()
def question4():
    with open("model_pickle", "rb") as f:
        modelo = pickle.load(f)
    
  