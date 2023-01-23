from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
from datetime import date
import os
from plot_co2 import plot_co2


app = Flask(__name__)

@app.route("/")
def graph():
    plot_co2()
    return render_template("graph.html")

if __name__ == "__main__":
    app.run(debug=True)
