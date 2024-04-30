import mysql_connector

##### connection
conn = mysql.connector.connect(
  host="localhost",
  user="chen_user",
  password="passwd2024",
  database="employees"
)

if conn is not None:
    cursor = conn.cursor()
else:
    print("connection failed")
    exit()


sql = "SELECT \
  D.dept_no, \
  D.dept_name, \
  E.emp_no, E.first_name, E.last_name \
  FROM employees AS E \
  INNER JOIN dept_manager AS DM ON E.emp_no = DM.emp_no \
      INNER JOIN departments AS D ON DM.dept_no = D.dept_no \
          WHERE DM.to_date = '9999-01-01'"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
  print(x)
  
cursor.close()
conn.close()