import tkinter as tk
from tkinter import *
from tkinter import messagebox


val = ""
A = 0
opertor = ""

def b1_button():
    global val
    val = val + "1"
    data.set(val)

def b2_button():   
    global val
    val = val + "2"
    data.set(val)

def b3_button():
    global val
    val = val + "3"
    data.set(val)

def b4_button():
    global val
    val = val + "4"
    data.set(val)

def b5_button():
    global val
    val = val + "5"
    data.set(val)

def b6_button():
    global val
    val = val + "6"
    data.set(val)

def b7_button():
    global val
    val = val + "7"
    data.set(val)

def b8_button():
    global val
    val = val + "8"
    data.set(val)

def b9_button():
    global val
    val = val + "9"
    data.set(val)

def b0_button():
    global val
    val = val + "0"
    data.set(val)

def add_button():
    global A
    global opertor 
    global val
    A = int(val)
    opertor = "+"
    val = val + "+"
    data.set(val)

def sub_button():
    global A
    global opertor 
    global val
    A = int(val)
    opertor = "-"
    val = val + "-"
    data.set(val)

def div_button():
    global A
    global opertor 
    global val
    A = int(val)
    opertor = "/"
    val = val + "/"
    data.set(val)

def multi_button():
    global A
    global opertor 
    global val
    A = int(val)
    opertor = "*" 
    val = val + "*"
    data.set(val)

def clear_button():
     global A
     global opertor
     global val
     val = ""
     A = 0 
     opertor = ""
     data.set(val)

def calculation():       
    global A
    global opertor
    global val
    val2 = val
    if opertor == "+":
        x= int(val2.split("+")[1])
        c = A+x
        data.set(c)
        val = str(c)

    elif opertor == "-":
        x= int(val2.split("-")[1])
        c = A-x
        data.set(c)
        val = str(c)

    elif opertor == "*":
        x= int(val2.split("*")[1])
        c = A*x
        data.set(c)
        val = str(c)

    elif opertor == "/":
        x = int(val2.split("/")[1])
        if x==0 :
          messagebox.show("gg","")
          A = ""
          val =""
          data.set(val)
        else:
          c=int(A/X)
          data.set(c)
          val =str(c)

root = tk.Tk()
root.geometry("250x400")
root.title("Yashwant Calculator")
#label
data =StringVar()
lbl = Label(root, textvariable=data,anchor=SE,bg="white",fg="black",font=("Verdana",20))
lbl.pack(expand=True, fill="both")

#frame
frame1= Frame(root,bg="#000000")
frame1.pack(expand=True, fill="both")

frame2= Frame(root,bg="#000000")
frame2.pack(expand=True, fill="both")

frame3= Frame(root,bg="#000000")
frame3.pack(expand=True, fill="both")

frame4= Frame(root,bg="#000000")
frame4.pack(expand=True, fill="both")

#frame 1 buttons
b1= Button(frame1,text="1",border=0,bg="black",fg="white",command=b1_button)
b1.pack(side=LEFT,expand=True, fill="both")

b2= Button(frame1,text="2",border=0,bg="black",fg="white",command=b2_button)
b2.pack(side=LEFT,expand=True, fill="both")

b3= Button(frame1,text="3",border=0,bg="black",fg="white",command=b3_button)
b3.pack(side=LEFT,expand=True, fill="both")

b_add = Button(frame1,text="+",border=0,bg="black",fg="white",command=add_button)
b_add.pack(side=LEFT,expand=True, fill="both")

#frame 2
b4= Button(frame2,text="4",border=0,bg="black",fg="white",command=b4_button)
b4.pack(side=LEFT,expand=True, fill="both")

b5= Button(frame2,text="5",border=0,bg="black",fg="white",command=b5_button)
b5.pack(side=LEFT,expand=True, fill="both")

b6= Button(frame2,text="6",border=0,bg="black",fg="white",command=b6_button)
b6.pack(side=LEFT,expand=True, fill="both")

b_sub = Button(frame2,text="-",border=0,bg="black",fg="white",command=sub_button)
b_sub.pack(side=LEFT,expand=True, fill="both")

#frame 3
b7= Button(frame3,text="7",border=0,bg="black",fg="white",command=b7_button)
b7.pack(side=LEFT,expand=True, fill="both")

b8= Button(frame3,text="8",border=0,bg="black",fg="white",command=b8_button)
b8.pack(side=LEFT,expand=True, fill="both")

b9= Button(frame3,text="9",border=0,bg="black",fg="white",command=b9_button)
b9.pack(side=LEFT,expand=True, fill="both")

b_multi = Button(frame3,text="x",border=0,bg="black",fg="white",command=multi_button)
b_multi.pack(side=LEFT,expand=True, fill="both")

#frame 4
b_clear =Button(frame4, text="C", border=0,bg="black", fg="white",command=clear_button)
b_clear.pack(side=LEFT,expand=True,fill="both")

b0 =Button(frame4, text="0", border=0, bg="black",fg="white",command=b0_button)
b0.pack(side=LEFT,expand=True,fill="both")

b_div =Button(frame4, text="/", border=0,bg="black", fg="white",command=div_button)
b_div.pack(side=LEFT,expand=True,fill="both")

b_eqaul= Button(frame4, text="=", border=0,bg="#006994", fg="white",command=calculation)
b_eqaul.pack(side=LEFT,expand=True,fill="both")
 
mainloop()