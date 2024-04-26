import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="chen_user",
  password=""
)

if __name__ == "__main__":
    print(mydb)