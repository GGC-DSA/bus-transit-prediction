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



#Generating 2nd file format
#pandas.EXPLOSION!!!! lol
def shapeCharge(id,dic,lister):
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
            lister.append({"timeStamp":shape["timeStamp"],"vehicle":str(id),"stop_id":stop,"route":route,"direction":shape["direction"],
                                                    "longitude":shape["longitude"],"latitude":shape["latitude"]})
                                                   
            #print(len(lister))      
      
      return dic,lister


x_modi = pd.DataFrame()
emptyDict = {}
x_modi_lister = []
for x in x_live["vehicle"].unique():
      emptyDict, x_modi_lister = shapeCharge(x,emptyDict,x_modi_lister)

x_modi = pd.DataFrame(x_modi_lister,columns=["timeStamp","vehicle","stop_id","route","direction","longitude","latitude"])
print(len(x_modi))


#print(emptyDict)
#print(x_modi)

#timeStamp, vehicle, stop_id, route, direction, longitude, latitude

 





label_encoder = []
for i in ["vehicle","stop_id","route","direction"]:
      x_modi[i] = x_modi[i].astype(str)
      labeler = prepro.LabelEncoder()
      x_modi[i] = labeler.fit_transform(x_modi[i])
      label_encoder.append(labeler)

#print(x_modi)

X_test = x_modi.to_numpy().reshape(len(x_modi),1,7)


y_pred = model.predict(X_test)


x_modi["adherence"] = y_pred

#print(x_modi)
x_modi["stop_id"] = pd.Series(label_encoder[1].inverse_transform(x_modi["stop_id"])).astype(str)
x_modi["vehicle"] = pd.Series(label_encoder[0].inverse_transform(x_modi["vehicle"])).astype(str)




for stop_id, vehicle, adherence in x_modi[["stop_id","vehicle","adherence"]].itertuples(index=False):
 
      emptyDict[stop_id][4][vehicle]= adherence 
   



emptyDict = [emptyDict[x] for x in emptyDict]

print(emptyDict)

with open("data/stopData.json",'w+') as f:
      json.dump(emptyDict,f)
      

''' Code to test whether None spaces are left in adherence dict
testList = []
otherlist =[]
for x in emptyDict:
      for y in emptyDict[x][4]:
            if( emptyDict[x][4][y] == None):  
                  testList.append(y)
                  otherlist.append(x)


for x in range(0,10):
      print(x_modi[x_modi["stop_id"]==otherlist[x]][x_modi["vehicle"]==testList[x]])
                  
'''               
        


'''
output=[]
for x in testList:
      if x not in output:
            output.append(x)
#print(output)
'''




