# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:25:13 2024

@author: migci
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import cross_validate

def pre_process_breast():
    df = pd.read_csv("breast-cancer.csv")
    df.dropna(inplace=True)
    scaler_standard = StandardScaler()
    scaler_minmax = MinMaxScaler()
    X = df.drop(columns = 'diagnosis')
    y = df['diagnosis']
    X_scaled = scaler_minmax.fit_transform(X) #este dá melhor generalização dos dados
    return X_scaled,y

#pre_process_breast()


def g1():
    X, y = pre_process_breast()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,stratify=y ,random_state=0)
    log = LogisticRegression()
    log.fit(X_train, y_train)
    y_pred = log.predict(X_test)
    conf = confusion_matrix(y_test, y_pred)
    classif = classification_report(y_test, y_pred)
    print("Confusion matrix: \n", conf)
    print("Classification report: \n", classif)
    metrics = cross_validate(log, X, y, cv=10, scoring=["accuracy", "f1_macro"],return_train_score=True)
    print("Cross-Validation Results:")
    print("Mean Macro F1: ", metrics['test_f1_macro'].mean())
    print("Accuracy: ", metrics['test_accuracy'].mean())
#g1()

def g2_1():
    df = pd.read_csv("indian_liver_patient.csv")
    df=df.drop('Gender',axis=1)
    df.dropna(inplace=True)
    scaler_standard = StandardScaler()
    scaler_minmax = MinMaxScaler()
    X = df.drop(columns= 'Dataset')
    y = df['Dataset']
    #X_scaled = scaler_standard.fit_transform(X)
    #X_scaled = scaler_minmax.fit_transform(X_scaled)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y ,random_state=0)
    log = LogisticRegression(random_state=0, max_iter=1000)
    metrics = cross_validate(log, X, y, cv=10, scoring=["accuracy", "f1_macro"],return_train_score=True)
    print("Cross-Validation Results:")
    print("Mean Macro F1: ", metrics['test_f1_macro'].mean())
    print("Mean Accuracy: ", metrics['test_accuracy'].mean())
#g2_1()

def g2_2():
    df = pd.read_csv("indian_liver_patient.csv")
    df.dropna(inplace=True)
    df = pd.get_dummies(df, drop_first= True,columns=['Gender'])
    numeric_cols = ['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase',
                    'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']
    scaler_standard = StandardScaler()
    df[numeric_cols]= scaler_standard.fit_transform(df[numeric_cols])
    X = df.drop(columns='Dataset')
    y = df['Dataset']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y ,random_state=0)
    log = LogisticRegression(random_state=0)
    metrics = cross_validate(log, X, y, cv=10, scoring=["accuracy", "f1_macro"],return_train_score=True)
    print("Cross-Validation Results:")
    print("Mean Macro F1: ", metrics['test_f1_macro'].mean())
    print("Mean Accuracy: ", metrics['test_accuracy'].mean())
g2_2()
    
    
    