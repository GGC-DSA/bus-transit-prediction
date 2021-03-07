#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:55:00 2021

@author: daniel
"""

from marta.api import get_buses, get_trains
import csv
from datetime import datetime
import sys
import boto3
from os import path
from collections import defaultdict
import json

 #TODO utilize and test upon api key activation
fieldNames=['adherence','block_abbr','block_id','direction','last_updated','latitude','longitude','route','stop_id'
	,'timepoint','trip_id','vehicle']
now = datetime.now()

dataDict = get_buses()

print(datetime.now())
print(dataDict[0])

id=0
iteration=0

if(not path.exists("ids.txt")):
	with open("ids.txt","w+") as file:
		file.write("id,{},iteration".format(str(datetime.now())))
else:
	with open("ids.txt","r") as file:
		last_line = ""
		for last_line in file:
			pass
		last_data=last_line.split(',')
		id=int(last_data[0])
		iteration=int(last_data[-1])+1


mydict = lambda: defaultdict(mydict)
new_ids = mydict()


with open("ids.txt","a") as file:
	for row in dataDict:
		id=id+1
		new_ids[id]["iteration"]=iteration
		for x,y in [(getattr(row,x),x) for x in fieldNames]:
			new_ids[id][y]=x
		file.write("\n{},{},{}".format(id,str(now),iteration))

with open("jsonout.json","w+") as fp:
	json.dump(new_ids, fp, default=str)


#print(new_ids)

'''
with open(r'{}'.format(sys.argv[1]), 'a',newline='') as f:
    for row in dataDict:
        fields = [getattr(row,x) for x in fieldNames]
        writer = csv.writer(f)
        writer.writerow(fields)
'''
