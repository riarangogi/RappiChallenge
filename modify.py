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

data["primeTime"] = np.where((data["hour"]<=19) & (data["hour"]>=11), 1, 0)

print(data)
