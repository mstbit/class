import mysql_connector as conn

mydb = conn.mydb
cursor = mydb.cursor()

cursor.execute(
    "USE mydatabase")

# cursor.execute("DESCRIBE customers")

sql = "SELECT * FROM customers LIMIT 10"
cursor.execute(sql)

result = cursor.fetchall()      # ### fetch all rows
for x in result:
    print(x)

# mydb.commit           # ### not changing the DB






cursor.close()          # ### close recommended
mydb.close()            # ### close recommended