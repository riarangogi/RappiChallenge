"""
Author: Ricardo Arango Giraldo
Date: 27/Aug/2019
Description: In  this script we understand the data and discovery relationship
between the variables
OS: elementary OS 5.0 Juno (64-bit), Basado en Ubuntu 18.04.2 LTS
Python Version: Anaconda 3.7.3
"""
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

data = pd.read_csv("./Data/Raw/orders.csv")
data["created_at"] = pd.to_datetime(data["created_at"])
print(data.head())
print(data.info())

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


plotNumericData("to_user_distance", "de la distancia al usuario")

plotNumericData("to_user_elevation", "de la diferencia en altura del usuario")

plotNumericData("total_earning", "del valor por el servicio de mensajeria")

plt.title("Cantidad de ordenes aceptadas y ordenes no tomadas")
takenTable = data["taken"].value_counts()
takenTable.plot(kind="bar")
plt.show()

plt.title("Cantidad de solicitudes por día")
dateTable = data["created_at"].dt.weekday.value_counts()
dateTable.plot(kind="bar")
plt.show()
