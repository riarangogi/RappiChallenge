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

toUserDistanceMedian = data["to_user_distance"].median()
IQR = data["to_user_distance"].quantile(0.75)-data["to_user_distance"].quantile(0.25)
LS = data["to_user_distance"].quantile(0.75)+1.5*IQR
LI = data["to_user_distance"].quantile(0.25)-1.5*IQR

for i in range(len(data)):
	if (data.loc[i, "to_user_distance"]>=LS):
		data.loc[i, "toUserDistance"] = toUserDistanceMedian
	if (data.loc[i, "to_user_distance"]<=LI):
		data.loc[i, "toUserDistance"] = toUserDistanceMedian
	else:
		data.loc[i, "toUserDistance"] = data.loc[i,"to_user_distance"]


toUserElevationMedian = data["to_user_elevation"].median()
IQR = data["to_user_elevation"].quantile(0.75)-data["to_user_elevation"].quantile(0.25)
LS = data["to_user_elevation"].quantile(0.75)+1.5*IQR
LI = data["to_user_elevation"].quantile(0.25)-1.5*IQR

for i in range(len(data)):
	if (data.loc[i, "to_user_elevation"]>=LS):
		data.loc[i, "toUserElevation"] = toUserElevationMedian
	if (data.loc[i, "to_user_elevation"]<=LI):
		data.loc[i, "toUserElevation"] = toUserElevationMedian
	else:
		data.loc[i, "toUserElevation"] = data.loc[i,"to_user_elevation"]


totalEarningMedian = data["total_earning"].median()
IQR = data["total_earning"].quantile(0.75)-data["total_earning"].quantile(0.25)
LS = data["total_earning"].quantile(0.75)+1.5*IQR
LI = data["total_earning"].quantile(0.25)-1.5*IQR

for i in range(len(data)):
	if (data.loc[i, "total_earning"]>=LS):
		data.loc[i, "totalEarning"] = totalEarningMedian
	if (data.loc[i, "total_earning"]<=LI):
		data.loc[i, "totalEarning"] = totalEarningMedian
	else:
		data.loc[i, "totalEarning"] = data.loc[i,"total_earning"]


print(data.head())
