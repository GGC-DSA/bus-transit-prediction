# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:34:47 2021

@author: rapte
"""



import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash, json
from sklearn import preprocessing as prepro
import os.path
from flask_cors import CORS
from datetime import date
import json as js
from dotenv import load_dotenv
import os



app = Flask(__name__, template_folder='templates')
CORS(app)


load_dotenv(dotenv_path="data/key.env"
app.secret_key =  os.getenv("SECRET_KEY_FLASK")

#----------------------------------------------------





#home page --initial template adapted from w3schools css tutorial
@app.route('/')
@app.route('/Home')
@app.route('/home')
def home_builder():
      

      busData = pd.read_csv("data/busData.csv")

      with open("data/stopData.json") as f:
            stopData = js.load(f) 
      
      
       
      with open("data/time.txt","r") as f:
            update_time=f.read()
      
      #--- finished reading in
      
      
      lister = busData[["longitude","latitude","vehicle","direction","route"]].values.tolist()
      stops=stopData
      
      
      
      home_annoc = [str(len(lister)),str(len(busData["route"].unique()))]
           
      
      
      
      
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


if __name__ == '__main__':
	from gevent.pywsgi import WSGIServer
	app.debug = False
	http_server = WSGIServer(('',8000),app)
	http_server.serve_forever()
	#app.run(debug=False,host='127.0.0.1',port=8000)
