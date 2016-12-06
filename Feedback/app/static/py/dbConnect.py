import psycopg2
import sys

def submit():
    print("started")
    conn_string = "host='localhost' port='5432' dbname='testdb' user='andrew' password='password'"

    print("Connecting to database\n ->%s" % (conn_string))

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    print ("Connected!\n")

    cur = conn.cursor()
    print("cursor opened")
    #cur.execute('INSERT INTO FeedBack (id, satisfaction) VALUES (1, 5);')
    cur.close()

    print("done")
