from tkinter import *
from tkinter import messagebox
root=Tk()
def msg():
    messagebox.askyesno('Cancel Registration',"Registration in progress,Are you sure about cancel?")
Label(root,text="Please fill up").grid(row=0,column=0)
Label(root,text="Registration Form ").grid(row=0,column=1)
labl1 = Label(root,text="User Name :")
labl2 = Label(root,text="Email Id :")
labl3 = Label(root,text="Mobile :")
labl4 = Label(root,text="Age :")
labl5 = Label(root,text="Password :")
labl6 = Label(root,text="Confirm Password:")
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)
labl1.grid(row=1,column=0)
entry1.grid(row=1,column=1)
labl2.grid(row=2,column=0)
entry2.grid(row=2,column=1)
labl3.grid(row=3,column=0)
entry3.grid(row=3,column=1)
labl4.grid(row=4,column=0)
entry4.grid(row=4,column=1)
labl5.grid(row=5,column=0)
entry5.grid(row=5,column=1)
labl6.grid(row=6,column=0)
entry6.grid(row=6,column=1)
btn1 = Button(root,text="Login",fg="white",bg="black")
btn2 = Button(root,text="Cancel",command= msg,fg="white",bg="black")
btn1.grid(row=7,column=0)
btn2.grid(row=7,column=1)
root.mainloop()