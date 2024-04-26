# import mysql_connector
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="chen_user",
  password="redcar2024"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

