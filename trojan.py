import mysql.connector
import tkinter  as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("400x250")
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "testdb"
)
# get cursor object
mycursor= db.cursor()

class viewtable:
    tk.button

mycursor.execute("SELECT * FROM employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#my_w.mainloop()