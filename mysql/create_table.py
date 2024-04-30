import mysql_connector as conn

mydb = conn.mydb

mycursor = mydb.cursor()
mycursor.execute(
    "USE mydatabase")
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

##### add id column #####
# mycursor.execute(
#     "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
