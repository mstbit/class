import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="chen_user",
  password="",
  database="employees"
)

mycursor = mydb.cursor()

sql = "SELECT \
  D.dept_no, \
  D.dept_name, \
  E.emp_no, E.first_name, E.last_name \
  FROM employees AS E \
  INNER JOIN dept_manager AS DM ON E.emp_no = DM.emp_no \
      INNER JOIN departments AS D ON DM.dept_no = D.dept_no \
          WHERE DM.to_date = '9999-01-01'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)