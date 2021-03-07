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

 #Field names and datatype specifications
fieldNames=[('adherence',"N"),('block_abbr',"S"),('block_id',"S"),('direction',"S"),('last_updated',"S"),('latitude',"N"),('longitude',"N"),('route',"S"),('stop_id',"S")
	,('timepoint',"S"),('trip_id',"S"),('vehicle',"S")]
now = datetime.now()

dataDict = get_buses()

#print(datetime.now())
#print(dataDict[0])

id=0
iteration=0

#checking whether id file exists, if it does read in the next available id
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


new_ids = {}
dictList=[]


#Reformatting Data into a list of dictionaries with ids & appending the new ids to the id text file
with open("ids.txt","a") as file:
	for row in dataDict:
		id=id+1
		new_ids["id"]={"S":f'{id:08}'}
		new_ids["iteration"]={"S":str(iteration)}
		for x,y,z in [(getattr(row,x[0]),x[0],x[1]) for x in fieldNames]:
			new_ids[y]={"{}".format(z):str(x)}
		file.write("\n{},{},{}".format(f'{id:08}',str(now),iteration))
		dictList.append(new_ids)
		
		print(new_ids["id"]["S"]+"  "+new_ids["timepoint"]["S"])
		new_ids={}
#print([{"hi":x} for x in dictList])


for i in range(-1,len(dictList)-1,25):
	#print(dictList)
	
	#Handling Dictionary Splitting
	if(len(dictList)<i+24):
		print("reached the end")
		formatedpone=[{"PutRequest":{"Item":x}} for x in dictList[i+1:]]
	else:
		formatedpone=[{"PutRequest":{"Item":x}} for x in dictList[i+1:i+26]]
	
	for q in formatedpone:
		print(q["PutRequest"]["Item"]["id"]["S"])
	formdictList={"bus_data":formatedpone}
	#print(formdictList)
	with open("data/jsonout{}.json".format(i),"w+") as fp:
		json.dump(formdictList, fp, default=str)

#print(new_ids)

'''
with open(r'{}'.format(sys.argv[1]), 'a',newline='') as f:
    for row in dataDict:
        fields = [getattr(row,x) for x in fieldNames]
        writer = csv.writer(f)
        writer.writerow(fields)
'''
