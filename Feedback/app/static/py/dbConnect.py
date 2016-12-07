import psycopg2
import sys
from ../Tests/gemTest import *

def dbConnect(conn_string):
    ##### Connects to database #####
    print("Connecting to database\n ->%s" % (conn_string))
    conn = psycopg2.connect(conn_string)
    print ("Connected!\n")
    return conn

def sendData(conn, satisfaction, date, feedback):
    ##### Sends data to database #####
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (satisfaction, timeEntered, comment, surveyID) VALUES ('%s', '%s', '%s', 1);" % (satisfaction, date, feedback))
    conn.commit()
    cur.close()
    print ("data sent")
    ####Test if data entered correctly####
    dataFromDB()
    correctData(satisfaction, date, feedback)
