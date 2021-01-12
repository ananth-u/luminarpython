from tkinter import *

root=Tk()

tFrame=Frame(root)
bFrame=Frame(root)


tFrame.pack()
bFrame.pack(side=BOTTOM)

btn1=Button(tFrame,text="firstbutton",fg="green")
btn2=Button(tFrame,text="secondbutton",fg="yellow")
btn3=Button(tFrame,text="3rdbutton",fg="blue")
btn4=Button(bFrame,text="4thbutton",fg="cyan")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack()


root.mainloop()