import sqlite3

con  = sqlite3.connect("data.db")

qry = "create table student(id int, name varchar(20) , email varchar(29))"

qry = "insert into student values(3,'sufiyan','sufiyan@gmail.com')"
con.execute(qry)
con.commit()