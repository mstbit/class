import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="chen_user",
    password="passwd2024",
    database="mydatabase"
)
# print(mydb)

cursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)

mydb.commit()

print(cursor.rowcount, "record inserted.")


cursor.close()          # ### close recommended
mydb.close()            # ### close recommended
