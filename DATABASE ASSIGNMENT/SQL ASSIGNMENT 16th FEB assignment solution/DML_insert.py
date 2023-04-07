import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("insert into test.test_table values('saroj' , 020 , 'AA')")
mycursor.execute("insert into test.test_table values('ram' , 021 , 'DD')")
mycursor.execute("insert into test.test_table values('nilu' , 021 , 'AA')")
mycursor.execute("insert into test.test_table values('manoj' , 022 , 'CC')")
mycursor.execute("insert into test.test_table values('sam' , 023 , 'FF')")
mycursor.execute("insert into test.test_table values('rissi' , 024 , 'AA')")
mycursor.execute("insert into test.test_table values('kasto' , 025 , 'AA')")

mydb.commit()
mydb.close()