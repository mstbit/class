import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="chen_user",
  password="redcar2024"
)

if __name__ == "__main__":
    print(mydb)