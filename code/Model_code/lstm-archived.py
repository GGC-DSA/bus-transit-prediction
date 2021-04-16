# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 23:15:49 2021

@author: rapte
"""

import numpy as np
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import seaborn as sns
from pylab import rcParams
import matplotlib.pyplot as plt
from matplotlib import rc
from sklearn.model_selection import train_test_split
from pandas.plotting import register_matplotlib_converters
from sklearn import preprocessing as prepro




data=pd.read_json("\\Users\\rapte\\git-AI\/Busdata.json",orient="values")



#Refactoring Column name
data.rename(columns = {'last_updated':"timeStamp"}, inplace = True)



#prepro
#Recategorizing Iteration as a integer for comparisons later

#initial Data manip
data["iteration"] = data["iteration"].astype(int)

data['timeStamp'] = pd.to_datetime(data['timeStamp'], format="%Y-%m-%d %H:%M:%S.%f")

print(data.columns)

#handling dups
data.drop_duplicates(subset=["timeStamp","vehicle"],inplace=True)

print(data)

#sorting and re indexing data
data.sort_values('timeStamp', inplace=True, ascending=True)
data=data.reset_index()


data["timeStamp"] = data["timeStamp"].dt.hour + data["timeStamp"].dt.minute/60


x = data[["timeStamp","vehicle","stop_id","route","direction","longitude","latitude"]]
y = data["adherence"]

print(x,y)


#transforming data ----------------------------------------------------------------------


#label encoding
label_encoder = []

for i in ["vehicle","stop_id","route","direction"]:
      labeler = prepro.LabelEncoder()
      x[i] = labeler.fit_transform(x[i])
      label_encoder.append(labeler)

print(x.size)


print(x)

#normalizing  -- do later see if improves things
#normalizer_list = []

#for i in ["longitude","latitude"]:
      







#----------------------------------------------------------------------------------------

#analysis


X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=5)

X_train, X_test = X_train.to_numpy().reshape(len(X_train),1,7), X_test.to_numpy().reshape(len(X_test),1,7)




#print(X_train.shape)


print(y_train.values)



model = keras.Sequential()
model.add(
  keras.layers.Bidirectional(
    keras.layers.LSTM(
      units=128, 
      input_shape=(X_train.shape[1],X_train.shape[2])
    )
  )
)
model.add(keras.layers.Dropout(rate=0.2))
model.add(keras.layers.Dense(units=1))
model.compile(loss='mean_squared_error', optimizer='adam')




history = model.fit(
    X_train, y_train.values, 
    epochs=30, 
    batch_size=32, 
    validation_split=0.1,
    shuffle=False
)

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend();
plt.show()
