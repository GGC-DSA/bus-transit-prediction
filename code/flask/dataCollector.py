# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:38:18 2021

@author: rapte
"""



#TODO Waiting for index to spinup on AWS 

import datetime
import matplotlib.dates as md
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import boto3
from boto3.dynamodb.conditions import Key
import json
from boto3.dynamodb.types import TypeSerializer


#Specifying which tool of AWS we are interacting with
dynamodb = boto3.resource("dynamodb","us-east-2")

#Specifying the table we are interacting with
table = dynamodb.Table('bus_data')

scanReq=[]

serializer = TypeSerializer()

getList = [{"id":str(f'{x:08}')} for x in range(1,169666)]

for i in range(-1,len(getList)-1,60):
    if(len(getList)-1 < i+60):
        reqItem = {"bus_data": {"Keys": getList[i+1:]}}
    else:
        reqItem = {"bus_data": {"Keys": getList[i+1:i+61]}}
        
    #print(reqItem)
    scanReq.append(dynamodb.batch_get_item(RequestItems=reqItem))


scanReq_prior = [x["Responses"]["bus_data"] for x in scanReq]
#https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-list-of-lists?rq=1
scanReq_form = [item for sublist in scanReq_prior for item in sublist]
print(scanReq_form[0])

with open("Busdata.json","w+") as fi:
    json.dump(scanReq_form,fi)
    
