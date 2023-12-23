from flask import Flask
import psycopg2
from datetime import datetime

app = Flask(__name__)


#fixed root endpointf
@app.route('/')
def hello():
    date_now = datetime.utcnow()
    date_now_formated = date_now.strftime("%d-%m-%Y")
    conn=psycopg2.connect(host="raspkit.duckdns.org", dbname="esp32", user="esp32", password="esp32pass")
    cur = conn.cursor()
    cur.execute("SELECT temperaturevalue FROM TEMPERATURES WHERE DATE=%s ORDER BY TIME DESC LIMIT 1", (date_now_formated,))
    result =cur.fetchall()
    result_list = [r[0] for r in result]
    cur.close()
    conn.close()
    return_string = "Hello i am alive!! Last temperature reading was:".join(result[0])
    
    return return_string
    