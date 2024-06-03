import parser
from tkinter import *
root = Tk() #root defined

root.title("Calculator") #title of the window
display = Entry(root) #entry box for input and output display
display.grid(row=1,columnspan=6,ipady=10,sticky=W+E) #alignment of entry box
#get user input and place in text field
i=0
def get_num(num):
    global i
    entre_strng = display.get()
    if (entre_strng == "Error"):
        all_clear()
        display.insert(i,num)
        i+=1
    else:
        display.insert(i, num)
        i += 1
#clear function
def all_clear():
    display.delete(0,END)
#Delete a number
def del_num():
    entre_strng = display.get()
    if (entre_strng == "Error"):
        all_clear()
    elif len(entre_strng):
        temp_strng= entre_strng[:-1]
        all_clear()
        display.insert(0,temp_strng)
    else :
        all_clear()
        display.insert(0,"Error")
#get operator
def get_opr(opr):
    global i
    entre_strng = display.get()
    if (entre_strng == "Error"):
        all_clear()
        length = len(opr)
        display.insert(i,opr)
        i+=length
    else:
        length = len(opr)
        display.insert(i, opr)
        i += length
#Calculates on pressing =
def claculate(): #calculate function
    entre_strng = display.get()
    try:
        a=parser.expr(entre_strng).compile()
        result=eval(a)
        all_clear()
        display.insert(0,result)
    except Exception:
        all_clear()
        display.insert(0,"Error")

#adding buttons to calculator
Button(root,text="1",height= 3, width= 5,command = lambda:get_num(1)).grid(row=2,column=0)
Button(root,text="2",height= 3, width= 5,command = lambda:get_num(2)).grid(row=2,column=1)
Button(root,text="3",height= 3, width= 5,command = lambda:get_num(3)).grid(row=2,column=2)
Button(root,text="4",height= 3, width= 5,command = lambda:get_num(4)).grid(row=3,column=0)
Button(root,text="5",height= 3, width= 5,command = lambda:get_num(5)).grid(row=3,column=1)
Button(root,text="6",height= 3, width= 5,command = lambda:get_num(6)).grid(row=3,column=2)
Button(root,text="7",height= 3, width= 5,command = lambda:get_num(7)).grid(row=4,column=0)
Button(root,text="8",height= 3, width= 5,command = lambda:get_num(8)).grid(row=4,column=1)
Button(root,text="9",height= 3, width= 5,command = lambda:get_num(9)).grid(row=4,column=2)
Button(root,text="0",height= 3, width= 5,command = lambda:get_num(0)).grid(row=5,column=1)
Button(root,text="(",height= 3, width= 5,command = lambda : get_opr("(")).grid(row=5,column=0)
Button(root,text=")",height= 3, width= 5,command = lambda : get_opr(")")).grid(row=5,column=2)
Button(root,text=".",height= 3, width= 5,command = lambda : get_opr(".")).grid(row=5,column=3)
Button(root,text="AC",height= 3, width= 5,bg= "red",command = lambda:all_clear()).grid(row=2,column=3)
Button(root,text="DEL",height= 3, width= 5,bg="red",command = lambda:del_num()).grid(row=2,column=4)
Button(root,text="+",height= 3, width= 5,command = lambda : get_opr("+")).grid(row=4,column=3)
Button(root,text="-",height= 3, width= 5,command = lambda : get_opr("-")).grid(row=4,column=4)
Button(root,text="x",height= 3, width= 5,command = lambda : get_opr("*")).grid(row=3,column=3)
Button(root,text="/",height= 3, width= 5,command = lambda : get_opr("/")).grid(row=3,column=4)
Button(root,text="=",height= 3, width= 5,bg="blue",command = lambda : claculate()).grid(row=5,column=4)
root.mainloop()
