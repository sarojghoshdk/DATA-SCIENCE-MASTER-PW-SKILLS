import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists test.test_table(name VARCHAR(50) , roll INT , id VARCHAR(30)) ;")
mydb.close() 