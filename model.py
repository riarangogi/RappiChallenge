"""
Author: Ricardo Arango Giraldo
Date: 28/Aug/2019
Description: In  this script we create  various models (data mining)
techniques on the prepared variables in order to create models that possibly
provide the desired outcome.
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.7.3
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

np.random.seed(47)
df =  pd.read_csv("./Data/Tidy/dfFile.csv")

y = df["taken"]
X = df.drop("taken", axis=1)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=47)

logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)
