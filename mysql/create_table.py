# import mysql_connector
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="chen_user",
    password="",
    database="mydatabase"
)
# print(mydb)

mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

##### add id column #####
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")