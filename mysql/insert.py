import mysql_connector as conn

mydb = conn.mydb
mycursor = mydb.cursor()
mycursor.execute(
    "USE mydatabase")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
