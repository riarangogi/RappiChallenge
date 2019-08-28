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

#cargar el dataset
data = pd.read_csv("./Data/Raw/orders.csv")
#leer la columna created_at como una fecha
data["created_at"] = pd.to_datetime(data["created_at"])
print(data.head())
print(data.info())

#subconjunto con las variables numericas
numericData = data[["to_user_distance", "to_user_elevation", "total_earning"]]
print(numericData.describe())

#funcion para graficar las variables numericas
def plotNumericData(variable, title):
#graficar el histografica
	fig = plt.figure()
	ax1 = plt.subplot(1, 2, 1)
	ax1.set_title("Histograma {}".format(title))
	numericData[variable].plot(kind="hist")
#graficar el box plot
	ax2 = plt.subplot(1, 2, 2)
	ax2.set_title("Box plot {}".format(title))
	numericData[variable].plot(kind="box")
#mostrar grafica
	plt.show()


#graficar la variable to_user_distance
plotNumericData("to_user_distance", "de la distancia al usuario")
#graficar la variable to_user_elevation
plotNumericData("to_user_elevation", "de la diferencia en altura del usuario")
#graficar la  variable total_earning
plotNumericData("total_earning", "del valor por el servicio de mensajeria")

#grafica de barras de la variable taken
plt.title("Cantidad de ordenes aceptadas y ordenes no tomadas")
takenTable = data["taken"].value_counts()
takenTable.plot(kind="bar")
plt.show()

#grafica de barras de la cantidad de servicios por dia
plt.title("Cantidad de solicitudes por día")
dayTable = pd.crosstab(columns=data["taken"], index=data["created_at"].dt.weekday)
dayTable.plot(kind="bar", stacked=True)
plt.show()

#grafica de barras de la cantidad de servicios por hora
plt.title("Cantidad de solicitudes por hora")
hourTable = pd.crosstab(index=data["created_at"].dt.hour, columns=data["taken"])
hourTable.plot(kind="bar", stacked=True)
plt.show()
