from tkinter import *
import mysql.connector as sql

con = sql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "",
    database = "19febpython"

)
cursor = con.cursor()
root = Tk()
root.geometry("500x500")
root.title("registration form")

def create():
    name = t1.get()
    email = t2.get()
    phone = t3.get()

    qry = "insert into students"
