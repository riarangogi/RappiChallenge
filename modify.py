"""
Author: Ricardo Arango Giraldo
Date: 27/Aug/2019
Description: In  this script we create and transform variables in preparation
for data modeling.
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.7.3
"""
import pandas as pd
import numpy as np

data = pd.read_csv("./Data/Raw/orders.csv")
data["created_at"] = pd.to_datetime(data["created_at"])
data["hour"] = data["created_at"].dt.hour
tmp = []

print(data.info())

toUserDistanceMedian = data["to_user_distance"].median()
IQR = data["to_user_distance"].quantile(0.75)-data["to_user_distance"].quantile(0.25)
LS = data["to_user_distance"].quantile(0.75)+1.5*IQR
LI = data["to_user_distance"].quantile(0.25)-1.5*IQR

print(LS, LI, toUserDistanceMedian)
"""
df = pd.DataFrame({"a": [1,2,3], "b": [5,5,7], "c": ["q", "a", "p"]})
col = []
col.reshape(3, 1)
df["d"]=col
print(df)
print(len(df))
for i in range(len(df)):
	if (df.loc[i, "a"]>=2):
		col.append(df.loc[i, "c"])
	else:
		col.append(0)

print(col)

print(len(tmp))"""

for i in range(len(data)):
	if (data.loc[i, "to_user_distance"]>=LS):
		tmp.append(toUserDistanceMedian)
	if (data.loc[i, "to_user_distance"]<=LI):
		tmp.append(toUserDistanceMedian)
	else:
		tmp.append(data.loc[i,"to_user_distance"])

print(len(tmp))
print(data.head())
