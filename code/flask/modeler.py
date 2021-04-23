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


with open('data/jsonout.json') as f:
      live_sel = json.load(f)

#print(live_sel)
live_sel = [y['PutRequest']['Item'] for x in live_sel for y in x["bus_data"]]

fieldNames=['adherence','block_abbr','block_id','direction','last_updated','latitude','longitude','route','stop_id'
    ,'timepoint','trip_id','vehicle']

inner = 0

def unfolder(di):
      diRet = []
      for x in fieldNames:
            diRet.append(di[x]["S"])
      return diRet


unfolded ={}

for x in live_sel:
      unfolded[str(inner)]=unfolder(x)
      inner += 1


data = pd.DataFrame.from_dict(unfolded,orient="index",columns=fieldNames)

#print(live_sel)


stop_constant = pd.read_csv("data\/stop_constant.csv")

#print(stop_constant)





model = load_model("data\/lstm.h5")







#Refactoring Column name
data.rename(columns = {'last_updated':"timeStamp"}, inplace = True)



#Recategorizing Iteration as a integer for comparisons later

#initial Data manip
#print(data.head(1).values)



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
x_live[["latitude","longitude","vehicle","direction","route"]].to_csv("data\/busData.csv")




#start prediction prepro ----

#index / column definition needed here
x_modi = pd.DataFrame()

#stop_constant["route"] = router

#this probably doesn't work waiting for testing data

#print(stop_constant,x_live)

#x_modi = pd.concat([x_live[["vehicle","route"]],stop_constant[["stop_id","route","stop_lat","stop_lon"]]])

x_modi = pd.DataFrame()


#Generating 2nd file format
#pandas.EXPLOSION!!!! lol
def shapeCharge(id,dic):
      shape = x_live[x_live["vehicle"]==id]
      charge = stop_constant[stop_constant["route"].isin(shape["route"].values)]
      #print(charge)
      shape["stop_id"] = shape["stop_id"].astype(str)
      #print(charge)
      for route,stop,lat,lon in charge[["route","stop_id","stop_lat","stop_lon"]].itertuples(index=False):
            #print(x)
            if(str(stop) in dic):
                  dic[str(stop)][4][str(id)]=None
            else:
                  dic[str(stop)]=[lat,lon,stop,route,{str(id):None}]
      return dic


emptyDict = {}

for x in x_live["vehicle"].unique():
      emptyDict = shapeCharge(x,emptyDict)

print(emptyDict)

'''
for index, row in x_live.iterrows():
      for boat in stop_constant[stop_constant["route"]==row["route"]]:
            print(row)
            row["stop_id"] = boat["stop_id"]
            x_modi.append(row)




#label encoding testable data
label_encoder = []

for i in ["vehicle","stop_id","route","direction"]:
      labeler = prepro.LabelEncoder()
      x[i] = labeler.fit_transform(x[i])
      label_encoder.append(labeler)


X_test = x.to_numpy().reshape(len(x),1,7)


y_pred = model.predict(X_test)


print(y_pred)
#TODO format output file 2


#output file h........

#deprecated from training code
#X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=5)

#X_train, X_test = X_train.to_numpy().reshape(len(X_train),1,7), X_test.to_numpy().reshape(len(X_test),1,7)


'''




