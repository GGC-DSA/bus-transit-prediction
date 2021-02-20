#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:55:00 2021

@author: daniel
"""

from marta.api import get_buses, get_trains
import csv 
from datetime import datetime


 #TODO utilize and test upon api key activation


fieldNames=['adherence','block_abbr','block_id','direction','last_updated','latitude','longitude','route','stop_id'
    ,'timepoint','trip_id','vehicle']


dataDict = get_buses()

print(datetime.now())
print(dataDict[0])


with open(r'liveData.csv', 'a',newline='') as f:
    for row in dataDict:
        fields = [getattr(row,x) for x in fieldNames]
        writer = csv.writer(f)
        writer.writerow(fields)
    
