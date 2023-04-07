import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
)
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM test.test_table WHERE id = 'DD'")
mydb.commit()
mydb.close()