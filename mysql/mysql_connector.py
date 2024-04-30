import mysql.connector


try:    # ### just like files, connections are prone to errors
        # ### mydb is just a variable 
    mydb = mysql.connector.connect(
        host="localhost",
        user="chen_user",
        password="passwd2024"
    )
    # print(mydb)
    cursor = mydb.cursor()
except Exception as e:
    print(f"An error occured when establishing connection: {e}")
    exit()


if __name__ == "__main__":
    # Conn1= Conn()
    print(f"Print mydb: {mydb}")
    print("Say something")
