import psycopg2

connection = psycopg2.connect(
    dbname="mycrm",
    host="localhost",
    user="postgres",
    
    port="5432"
)

connection.autocommit = True

cursor = connection.cursor()

#cursor.execute("CREATE DATABASE mycrm")

cursor.close()
connection.close()
