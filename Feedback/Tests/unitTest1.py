import psycopg2

def connectTest(conn_string):
    error = ""

    try:
        conn = psycopg2.connect(conn_string)
    except psycopg2.Error as error:
        pass

    if (error == ""):
        print("passed")
    else:
        print("Failed /n" + error)
