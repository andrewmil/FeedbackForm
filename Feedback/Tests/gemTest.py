from datetime import datetime
import psycopg2

#dbId = 1
dbSatisfaction = ""
dbTimeEntered = "2016-01-24"
dbComment = "unnassigned"



def dataFromDB():
    global dbId
    global dbSatisfaction
    global dbTimeEntered
    global dbComment

    conn = psycopg2.connect("host='172.28.78.195' port='5432' dbname='feedback2' user='andrew' password='password'")
    cursor = conn.cursor();

    conn.commit()

    try:

        cursor.execute("SELECT * FROM feedback ORDER BY timeEntered DESC LIMIT 1")
        results = cursor.fetchall()
        for row in results:
            #dbId = row[0]
            dbSatisfaction = row[2]
            dbTimeEntered = row[3]
            dbComment = row[4]

        print (dbSatisfaction, dbTimeEntered, dbComment)
    except:
        print ("Error unable to fetch data")





def correctData(satisfaction, timeEntered, comment):

    if dbSatisfaction is satisfaction:
        if dbTimeEntered == timeEntered:
            if dbComment == comment:
                print ("match")
            else:
                print ("no match comment")
        else:
            print ("no match time")
    else:
        print ("no match satisfaction")


#dataFromDB()
#correctData(1, "satisfied", "1995-01-24", "rice")
