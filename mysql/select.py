import mysql_connector as conn

mydb = conn.mydb
cursor = mydb.cursor()

cursor.execute(
    "USE mydatabase")

sql = "SELECT * FROM customers"
cursor.execute(sql)

mydb.commit






cursor.close()          # ### close recommended
mydb.close()            # ### close recommended