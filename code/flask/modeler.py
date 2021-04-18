# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:40:43 2021

@author: rapte
"""

import numpy as np
import tensorflow as tf
import keras
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.model_selection import train_test_split
from pandas.plotting import register_matplotlib_converters
from sklearn import preprocessing as prepro
import json

from keras.models import load_model



checkDat = pd.read_json("data\/testData.json",orient="values")

print(checkDat.head())


model = load_model("data\/lstm.h5")




#to change to rawBusdata.json
data=pd.read_json("data\/testData.json",orient="values")






#Refactoring Column name
data.rename(columns = {'last_updated':"timeStamp"}, inplace = True)



#prepro
#Recategorizing Iteration as a integer for comparisons later

#initial Data manip
print(data.head(1).values)





data['timeStamp'] = pd.to_datetime(data['timeStamp'], format="%Y-%m-%d %H:%M:%S.%f")

#print(data.columns)

#handling dups
data.drop_duplicates(subset=["timeStamp","vehicle"],inplace=True)

#print(data)

#sorting and re indexing data
data.sort_values('timeStamp', inplace=True, ascending=True)
data=data.reset_index()


data["timeStamp"] = data["timeStamp"].dt.hour + data["timeStamp"].dt.minute/60


x_live = data[["timeStamp","vehicle","stop_id","route","direction","longitude","latitude"]]


#transforming/extending data ----------------------------------------------------------------------

#Saving first file neccesary for app.py
x_live[["latitude","longitude","vheicle","direction","route"]].to_csv("data\/busData.csv")




#start prediction prepro ----

#label encoding testable data
label_encoder = []

for i in ["vehicle","stop_id","route","direction"]:
      labeler = prepro.LabelEncoder()
      x[i] = labeler.fit_transform(x[i])
      label_encoder.append(labeler)


X_test = x.to_numpy().reshape(len(x),1,7)








#deprecated from training code
#X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=5)

#X_train, X_test = X_train.to_numpy().reshape(len(X_train),1,7), X_test.to_numpy().reshape(len(X_test),1,7)







