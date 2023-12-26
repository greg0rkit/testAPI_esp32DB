from flask import Flask, render_template
import psycopg2
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly
import json

app = Flask(__name__)


@app.route('/')
def tempChart():
    conn=psycopg2.connect(host="raspkit.duckdns.org", dbname="esp32", user="esp32", password="esp32pass")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TEMPERATURES")
    time_results = cur.fetchall()
    cur.close()
    conn.close()
    print(time_results)
    return "debug"