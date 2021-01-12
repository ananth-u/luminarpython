from tkinter import *

root= Tk() #root reference for the obj
root.title("main window")

label1=Label(root,text="username")
label2=Label(root,text="emailaddress")
label3=Label(root,text="password")
entry1=Entry(root)
label1.pack()
entry1.pack()

root.mainloop() #exsist till we click the close button