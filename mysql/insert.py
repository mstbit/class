from mysql_connector_class import ConnClass

with ConnClass("mydatabase") as db:
# mydb = conn.conn().mydb
# cursor = mydb.cursor()
    # db.execute("USE mydatabase")
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Jake", "123 Main St.")
    db.execute(sql, val)

    db.commit()

    print(db.cursor.rowcount, "record inserted.")


    db.cursor.close()          # ### close recommended
    # db.close()      # ### with should handle this