from datetime import datetime
import psycopg2

dbId = 1
dbSatisfaction = "not set"
dbTimeEntered = "2016-01-24"
dbComment = "unnassigned"

def dataFromDB():
    conn = "host='172.28.78.195' port='5432' dbname='feedback2' user='andrew' password='password'"


def correctData(int id, string satsfaction, datetime timeEntered, string comment):
