"""
Author: Ricardo Arango Giraldo
Date: 27/Aug/2019
Description: In  this script we understand the data and discovery relationship
between the variables
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.7.3
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./Data/Raw/orders.csv")
print(data.head())
print(data.columns)

numericData = data[["to_user_distance", "to_user_elevation", "total_earning"]]
print(numericData.describe())

def plotNumericData(variable, title):

	fig = plt.figure()
	ax1 = plt.subplot(1, 2, 1)
	ax1.set_title("Histograma {}".format(title))
	numericData[variable].plot(kind="hist")

	ax2 = plt.subplot(1, 2, 2)
	ax2.set_title("Box plot {}".format(title))
	numericData[variable].plot(kind="box")

	plt.show()
