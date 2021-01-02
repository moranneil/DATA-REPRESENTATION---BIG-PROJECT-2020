import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    auth_plugin="mysql_native_password",
    database="garage"
)

print("Connected Ok")

cursor = db.cursor()

sql="update vehicle set price=%s, colour=%s where reg=%s"
values = ("2899.00","Black","2003-LM-201")

cursor.execute(sql,values)

db.commit()
print("Updated successfully")
