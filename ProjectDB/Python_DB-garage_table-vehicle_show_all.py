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

sql="select * from vehicle"
values = (1,)

cursor.execute(sql)
result = cursor.fetchall()
#print("result Ok",result)
for x in result:
    print("IN LOOP")
    print(x)

print("FINISHED")
