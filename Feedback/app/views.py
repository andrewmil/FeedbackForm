from flask import render_template, redirect, request
from app import app
from .forms import Feedback
from random import randint
from Tests.unitTest1 import connectTest
from app.static.py.dbConnect import dbConnect, sendData
import psycopg2

@app.route('/')
@app.route('/index')
def index():
    form = Feedback()
    return render_template('index.html',
                           form=form)

@app.route('/database_Send', methods=['POST'])
def database_Send():
    form = Feedback()
    import psycopg2
    import sys
    from datetime import datetime

    conn_string = "host='172.28.78.195' port='5432' dbname='feedback2' user='andrew' password='password'"
    conn = dbConnect(conn_string)

    satisfaction = form.satisfaction.data
    feedback = form.feedback.data
    date = datetime.now()

    sendData(conn, satisfaction, date, feedback)

    conn.close()
    print("done")

    return render_template('index.html', form=form)
