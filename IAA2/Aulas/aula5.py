# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:08:58 2024

@author: migci
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree
from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier


def g1():
    df = pd.read_csv("IRIS.csv")
    #print(df.head())
    df.dropna(inplace= True)
    scaler_standard = StandardScaler()
    scaler_minmax = MinMaxScaler()
    X = df.drop(columns=['species'])
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y ,random_state=0)
    dtree = DecisionTreeClassifier(random_state=0)
    dtree.fit(X_train, y_train)
    y_pred = dtree.predict(X_test)
    conf = confusion_matrix(y_test, y_pred)
    classif = classification_report(y_test, y_pred)
    print("Confusion matrix: \n", conf)
    print("Classification report: \n", classif)
    #tree.plot_tree(dtree)
    print(dtree.get_depth())
#g1()

def g1_4():
    df = pd.read_csv("IRIS.csv")
    #print(df.head())
    df.dropna(inplace= True)
    #scaler_standard = StandardScaler()
    #scaler_minmax = MinMaxScaler()
    X = df.drop(columns=['species'])
    y = df['species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y ,random_state=0)
    dtree = DecisionTreeClassifier(random_state=0)
    dtree.fit(X_train, y_train)
    cv = cross_validate(dtree, X, y, cv=10, return_train_score=True)
    print("Cross-Validation Results:")
    print("Test: ",cv['test_score'])
    print("Mean Test Accuracy:", cv['test_score'].mean())
    print("Train scores:", cv['train_score'])
    print("Mean Train Accuracy:", cv['train_score'].mean())
#g1_4()
    
def pre_processed_liver():
    df = pd.read_csv("indian_liver_patient.csv")
    df=df.drop('Gender',axis=1)
    df.dropna(inplace=True)
    df['Dataset'] = df['Dataset'].replace(2,0)
    df = df.rename(columns={'Dataset': 'Disease'})
    X = df.drop(columns='Disease')
    y = df['Disease']
    scaler_standard = StandardScaler()
    X_scaled = scaler_standard.fit_transform(X)
    return X_scaled, y

def g2():
    X,y = pre_processed_liver()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y ,random_state=0)
    dtree = DecisionTreeClassifier(random_state=0)
    dtree.fit(X_train, y_train)
    y_pred = dtree.predict(X_test)
    conf = confusion_matrix(y_test, y_pred)
    classif = classification_report(y_test, y_pred)
    #print("Confusion matrix: \n", conf)
    #print("Classification report: \n", classif)
    #tree.plot_tree(dtree)
    #   print(dtree.get_depth())
    dtree2 = DecisionTreeClassifier(random_state=0, max_depth=20)
    dtree2.fit(X_train, y_train)
    y_pred = dtree2.predict(X_test)
    conf = confusion_matrix(y_test, y_pred)
    classif = classification_report(y_test, y_pred)
    print("Confusion matrix: \n", conf)
    print("Classification report: \n", classif)
    tree.plot_tree(dtree2)
    print(dtree2.get_depth())
#g2()
    
def g3():
    X,y = pre_processed_liver()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y ,random_state=0)
    rand_f= RandomForestClassifier(random_state=0, n_estimators=500)
    rand_f.fit(X_train, y_train)
    y_pred = rand_f.predict(X_test)
    conf = confusion_matrix(y_test, y_pred)
    classif = classification_report(y_test, y_pred)
    print("Confusion matrix: \n", conf)
    print("Classification report: \n", classif)
    #print("Default number of trees: ",rand_f.n_estimators)
g3()    
    
    
    