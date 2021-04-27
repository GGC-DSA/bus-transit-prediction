# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:34:47 2021

@author: rapte
"""

# TODO LIST
'''
secret key read in file .env
'''

import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash, json
from sklearn import preprocessing as prepro
import os.path
from datetime import date
import json as js
from dotenv import load_dotenv
import os

# =============================================================================

app = Flask(__name__, template_folder='templates')

# Flask secret key TODO set as env
load_dotenv(dotenv_path="data/key.env")
app.secret_key = os.getenv("SECRET_KEY_FLASK")


# =============================================================================


# home page --initial template adapted from w3schools css tutorial
@app.route('/')
@app.route('/Home')
@app.route('/home')
def home_builder():
    # ---- reading in live Data
    busData = pd.read_csv("data/busData.csv")

    with open("data/stopData.json") as f:
        stopData = js.load(f)

    with open("data/time.txt", "r") as f:
        update_time = f.read()

    # --- finished reading in

    lister = busData[["longitude", "latitude", "vehicle", "direction", "route"]].values.tolist()
    stops = stopData

    home_annoc = [str(len(lister)), str(len(busData["route"].unique()))]

    return render_template("home.html", value=lister, update_time=update_time,
                           home_annoc=home_annoc, stops=stops)


@app.route('/Data')
def data_builder():
    # TODO Turner -------
    # grab the arima model

    # calculate adherence for every hour for Today

    # model.predict(timeStamp....)

    # return as variable
    
    # load in CSV
    df = pd.read_csv('ArimaDataSetFinal.csv')

    # convert series to timedate and parse/change timeStamp to hour and minutes only
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], format='%d/%m/%Y %H:%M')
    df['timeStamp'] = df['timeStamp'].dt.strftime('%H:%M')

    # cast to dictionary and send as JSON string
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data)
    data = {'chart_data': chart_data}
    return render_template("data.html", data=data)


@app.route('/AboutUs')
def about_builder():
    return render_template("about.html")


@app.route('/Code')
def code_builder():
    return render_template("code.html")


app.run(debug=False)

# =============================================================================
