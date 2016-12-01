import psycopg2
import sys

def main():
    conn_string = "host='localhost' port='5432' dbname='testdb' user='andrew' password='password'"

    print("Connecting to database\n ->%s" % (conn_string))

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    print ("Connected!\n")

if __name__ == "__main__":
    main()

def insert(satisfaction):
    cur = conn.cursor()

    cur.execute('INSERT INTO FeedBack (satisfaction) VALUES (%)', (satisfaction))
    cur.close()

def close():
    conn.close()
