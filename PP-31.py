import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="admin",
password="",
database="StudentMaster"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE StudentMaster")
print("Database created successfully!")
db.close()