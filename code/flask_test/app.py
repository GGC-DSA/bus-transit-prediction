# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:39:55 2021

@author: rapte
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:34:47 2021

@author: rapte
"""

from flask import Flask, render_template, request, redirect, url_for, flash, json

import os.path


app = Flask(__name__, template_folder='templates')

#Flask secret key TODO set as env
app.secret_key = 'asdgagaweawsfasdfaqw'


#home page --initial template adapted from w3schools css tutorial
@app.route('/')
def home_builder():
      return render_template("home.html")

app.run()