import mysql.connector as sql

con = sql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
)

print("connected")

cursor = con.cursor()
cursor.execute("create database 19febpython")
cursor.execute("create table student (id int primary key,name varchar(20),email varchar(50))")