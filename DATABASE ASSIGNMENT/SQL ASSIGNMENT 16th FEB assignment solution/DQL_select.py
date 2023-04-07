import mysql.connector
mydb = mysql.connector.connect(    # it is creating connection
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor() # upto this it is used for any database creating
mycursor.execute("select * from test.test_table")  
for i in mycursor.fetchall() :
    print(i)
mydb.close()  # to close the connection