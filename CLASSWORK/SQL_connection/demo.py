import mysql.connector as sql


con = sql.connect(
    host="localhost",
    port=3306,
    user="root"
)

# print("connected")

cursor.execute("create database 19_feb")