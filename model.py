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
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

np.random.seed(47)
df =  pd.read_csv("./Data/Tidy/dfFile.csv")

y = df["taken"]
X = df.drop(["taken", "toUserElevation"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=47)

logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)

y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="modelo 2, auc="+str(auc))
plt.legend(loc=4)
plt.show()

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
class_names=[0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
