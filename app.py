from flask import Flask
import psycopg2
from datetime import datetime

app = Flask(__name__)


# root endpoint is broken i have to fix it
@app.route('/')
def hello():
    date_now = datetime.utcnow()
    date_now_formated = date_now.strftime("%d-%m-%Y")
    conn=psycopg2.connect(host="raspkit.duckdns.org", dbname="esp32", user="esp32", password="esp32pass")
    cur = conn.cursor()
    cur.execute("SELECT temperaturevalue FROM TEMPERATURES WHERE DATE=%s ORDER BY DESC LIMIT 1", (date_now_formated))
    #result =cur.fetchall()
    cur.close()
    conn.close()
    #return "Hello i am alive!! Last temperature reading was:".join(result)
    return "cur.execute() methods executed successfully"