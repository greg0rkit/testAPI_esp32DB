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
    cur.execute("SELECT TIME FROM TEMPERATURES WHERE DATE='22-12-23' ORDER BY TIME")
    time_results = cur.fetchall()
    cur.close()
    time_results_list= [r[0] for r in time_results]
    cur = conn.cursor()
    cur.execute("SELECT TEMPERATUREVALUE FROM TEMPERATURES WHERE DATE='22-12-2023' ORDER BY TIME")
    temp_results = cur.fetchall()
    cur.close()
    temp_results_list = [t[0] for t in temp_results]
    conn.close()
    
    df = pd.DataFrame({'Time':time_results_list, 'Temperature':temp_results_list})
    fig = px.line(df, x='Time', y='Temperature')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('tempChart.html', graphJSON=graphJSON) 