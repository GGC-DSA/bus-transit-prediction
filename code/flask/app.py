# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:34:47 2021

@author: rapte
"""

#TODO LIST
'''
1. implement different icons based on directionality [[having issues (maybe image size idk)--ask for help maybe ]] 
2. fix scheme on rhs column (working on)  <exact interface still in flux>
3. color scheme?
4. other pages (not homepage)
5. build live data in --need pipeline to do. [is test data a option for presentation?]
6. Create .env secret key [minimum priority]
7. Install into ec2 instance
8. Create domain with r53
9. Configure dns? (need to look into how)
'''


import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash, json
from sklearn import preprocessing as prepro
import os.path


app = Flask(__name__, template_folder='templates')

#Flask secret key TODO set as env
app.secret_key = 'asdgagaweawsfasdfaqw'








# Map Data Gathered here-------------  


busData = pd.read_csv("data/busData.csv")
stopData = pd.read_json("data/stopData.json")








'''  DATA FORMAT
# Bus Data: lat lon, vehicle id, dir, route
lister=[[-84.362307,33.82584490,"1710","Northbound",4],[-84.5896475,33.5589891,"1841","Eastbound",6]
        ,[-83.22,33.995,"1654","Southbound",4]];
update_time="04/04/2021 7:56 P.m."

#Stop Data : lat, long, stopID, routeID, dictionary of {'vehicleId':adherence}
stops = [[-84.5896475,36.5589891,1456,5],[-84.5896475,30.5589891,155424,4,{'1710':-4,'1654':-7}],
         [-84.5896475,32.5589891,123432,4,{'1710':6,'1654':0.0}],[-84.5896475,34.5589891,12341,4,{'1710':10,'1654':3}]]
'''



#data prepro here --------




#unused labeling
#----------------------------------------------------------------------------------- 
#directionality encoder defined
#dirList=["Southbound","Northbound","Eastbound","Westbound"]
#encoder = prepro.LabelEncoder()
#encoder.fit(dirList)

#to ensure proper image displaying (encoder doesn't seem to have consistent starting position)
#key = encoder.transform([x for x in dirList])


#for i in range(0,len(lister)):
 #     lister[i][3]=encoder.transform([lister[i][3]])[0]
#print(lister)
#----------------------------------------------------------------------------------




#sent data defined starting here-------


# number of bus, number of routes
home_annoc = [str(len(lister)),str(2)]

#home page --initial template adapted from w3schools css tutorial
@app.route('/')
@app.route('/Home')
@app.route('/home')
def home_builder():
      
      
      
      
      
      
      return render_template("home.html",value =lister,update_time=update_time,
                             home_annoc=home_annoc,stops=stops)


@app.route('/Data')
def data_builder():
      
      #TODO Turner -------
      #grab the arima model
      
      #calculate adherence for every hour for Today
      
      #model.predict(timeStamp....) 
      
      #return as variable
      
      
      values = []
      
      return render_template("data.html",values=values)


@app.route('/AboutUs')
def about_builder():
      return render_template("about.html")


@app.route('/Code')
def code_builder():
      return render_template("code.html")



app.run(debug=False)