from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
from datetime import date
import os
from plot_co2 import plot_co2
from get_table import get_table


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
    
@app.route("/graph")
def graph():
    plot_co2()
    return render_template("graph.html")

@app.route("/chart")
def chart():
    table = get_table()
    return render_template("chart.html", tables=[table])

    

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(port=7618, host='192.168.0.109', debug=True)
