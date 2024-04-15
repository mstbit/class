import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="chen_user",
  password="redcar2024"
)

print(mydb)