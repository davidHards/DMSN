import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="David",
    passwd='Sword',
    database="DMSN"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE actors (id INT PRIMARY KEY, actor VARCHAR(2000))")
