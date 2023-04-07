import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("UPDATE test_table SET id = 'EE' WHERE id = 'FF'")
mydb.commit()
mydb.close()