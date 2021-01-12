from tkinter import *
from tkinter import messagebox

root=Tk()

import mysql.connector 
from dbconnectprgm.dbconnect import get_connection
def db_connect(uername,password):
     db=get_connection()
     cursor=db.cursor()
     cursor.execute(("select * from users where username=%s AND password=%s "),(uername,password))
     user=cursor.fetchone()
     print(user)
     return user

def authenticate_user():
     uname=uentry.get()
     pwd=pentry.get()
     user=db_connect(uname,pwd)
     if(user==None):
        messagebox.showerror("invalid user","error")

     else:
        messagebox.showinfo("loggesd in","user successfully logged")


ulabel=Label(root,text="username")
plabel=Label(root,text="password")
uentry=Entry(root)
pentry=Entry(root)

btn=Button(root,text="login",command=authenticate_user)

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)

btn.grid(row=2,column=1)

root.mainloop()