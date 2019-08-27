"""
Author: Ricardo Arango Giraldo
Date: 26/Aug/2019
Description: In  this script we load the csv file
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.7.3
"""
import pandas as pd

data = pd.read_csv("./Data/Raw/orders.csv")

print(data.head())
print(data.shape)
print(data.columns)
