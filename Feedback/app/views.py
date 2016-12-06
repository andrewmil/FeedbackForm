from flask import render_template, flash, redirect, request
from app import app
from .forms import Feedback
from random import randint

@app.route('/')
@app.route('/index')
def index():
    form = Feedback()
    flash("satsfaction '%s'" % (form.satisfaction.data))
    if form.validate_on_submit():
        return redirect('/results')
    return render_template('index.html',
                           form=form)

@app.route('/database_Send', methods=['POST'])
def database_Send():
    form = Feedback()
    satisfaction = request.form['satisfaction']
    import psycopg2
    import sys
    from datetime import datetime

    print("started")
    conn_string = "host='172.28.78.195' port='5432' dbname='feedback2' user='andrew' password='password'"

    print("Connecting to database\n ->%s" % (conn_string))

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    print ("Connected!\n")

    satisfaction = form.satisfaction.data
    feedback = form.feedback.data

    cur = conn.cursor()
    print("cursor opened")
    id_ = randint(1001, 1000000)
    date = datetime.now()
    cur.execute("INSERT INTO feedback (id, satisfaction, timeEntered, comment, surveyID) VALUES ('%s', '%s', '%s', '%s', 1);" % (id_, satisfaction, date, feedback))

    conn.commit()
    cur.close()
    conn.close()
    print("done")

    return render_template('index.html',
                           form=form)
