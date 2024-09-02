# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:20:52 2024

@author: migci
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

def g1():
    df = pd.read_csv("indian_liver_patient.csv")
    df=df.drop('Gender',axis=1)
    df.dropna(inplace=True)
    #print(df.columns)
    df_scale = df.copy()
    #print(df.describe())
    #df.hist(figsize=(10, 8))
    #plt.tight_layout()
    #plt.show()
    #cols = ['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Albumin', 'Alkaline_Phosphotase']
    #sns.pairplot(df, vars=['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Albumin', 'Alkaline_Phosphotase'])
    #plt.show()
    scaler_standard = StandardScaler()
    scaler_minmax = MinMaxScaler()
    #df_scale[cols] = scaler_standard.fit_transform(df_scale[cols])
    #df_scale[cols] = scaler_minmax.fit_transform(df_scale[cols])    
    #print(df_scale.describe())
    #df_scale.hist(figsize=(10, 8))
    #plt.tight_layout()
    #plt.show()
    X = df_scale.drop(columns=['Dataset'])
    y = df_scale['Dataset']
    X = scaler_standard.fit_transform(X)
    X = scaler_minmax.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
    knn = KNeighborsClassifier(n_neighbors=4)
    knn.fit(X_train, y_train)
    y_pred= knn.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    cr = classification_report(y_test, y_pred)
    print(cr)
#g1()

def g2():
    df = pd.read_csv("IRIS.csv")
    df.dropna(inplace= True)
    setosa = df[df['species']== 'Iris-setosa']
    set_len = setosa['sepal_length'].values
    set_wid = setosa['sepal_width'].values
    versicolor = df[df['species']== 'Iris-versicolor']
    ver_len = versicolor['sepal_length'].values
    ver_wid = versicolor['sepal_width'].values
    virginica = df[df['species']== 'Iris-virginica']
    vir_len = virginica['sepal_length'].values
    vir_wid = virginica['sepal_width'].values
    plt.scatter(set_len,set_wid, marker='o', color='orange')
    plt.scatter(ver_len, ver_wid, marker='+')
    plt.scatter(vir_len, vir_wid, marker='s',color='blue')
    plt.xlabel("sepal_length")
    plt.ylabel("sepal_width")
    plt.show()
    #print(df.head())
    scaler_standard = StandardScaler()
    scaler_minmax = MinMaxScaler()
    X = df.drop(columns=['species', 'petal_width', 'petal_length'])
    y = df['species']
    X = scaler_minmax.fit_transform(X)
    X = scaler_standard.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y ,random_state=42)
    knn = KNeighborsClassifier(n_neighbors=11)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
#g2()

def g3():
    df = pd.read_csv("IRIS.csv")
    df.dropna(inplace= True)
    scaler_standard = StandardScaler()
    scaler_minmax = MinMaxScaler()
    X = df.drop(columns=['species'])
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y ,random_state=0)
    knn = KNeighborsClassifier(n_neighbors=7)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
g3()