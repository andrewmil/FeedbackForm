from flask import render_template, redirect, request, flash
from app import app
from .forms import Feedback
from random import randint
from Tests.unitTest1 import connectTest
from app.static.py.validation import feedbackValidation, satisfactionValidation
from app.static.py.dbConnect import dbConnect, sendData
import psycopg2

@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    form = Feedback()
    result = request.form
    return render_template('index.html', form=form)

@app.route('/database_Send', methods=['GET', 'POST'])
def database_Send():
    import psycopg2
    import sys
    from datetime import datetime

    form = Feedback()
    conn_string = "host='172.28.78.195' port='5432' dbname='feedback2' user='andrew' password='password'"
    conn = dbConnect(conn_string)

    ## retrieves data from form ##
    satisfaction = form.satisfaction.data
    feedback = form.feedback.data
    date = datetime.now()

    ## validation ##
    if (feedbackValidation(feedback) or satisfactionValidation(satisfaction)):
        return redirect('/index')

    sendData(conn, satisfaction, date, feedback)

    conn.close()
    print("done")

    return render_template('end.html')
