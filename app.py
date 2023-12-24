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
    cur.execute("SELECT TIME FROM TEMPERATURES WHERE DATE='22-12-2023' ORDER BY TIME ASC")
    time_results = cur.fetchall()
    cur.close()
    cur = conn.cursor()
    cur.execute("SELECT TEMPERATUREVALUE FROM TEMPERATURES WHERE DATE='22-12-2023' ORDER BY TIME ASC")
    temperature_results = cur.fetchall()
    cur.close()
    conn.close()
    time_results_list = [r[0] for r in time_results]
    temperature_results_list = [float(r[0]) for r in temperature_results]
    dict = {"Time":time_results_list, "Temperature":temperature_results_list}
    df = pd.DataFrame(data=dict)
    fig = px.line(df, x='Time', y='Temperature')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('tempChart.html', graphJSON=graphJSON)