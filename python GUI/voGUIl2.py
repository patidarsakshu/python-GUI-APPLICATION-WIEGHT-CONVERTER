#from telnetlib import XASCII
from tkinter import *
#import math
root = Tk()
root.title("")
root.geometry("700x750")
root['bg']='skyblue'
txtac = StringVar()
txtas = StringVar()
txtav= StringVar()
#z = 0
def adding():
    pie=3.14285714286
    r = float(ER.get())
    h = float(EH.get())
    xc=(2*pie*(r*h))
    xs=(2*pie*r*(r+h))
    xv=(pie*r**2*h)
    txtac.set(str(xc))
    txtas.set(str(xs))
    txtav.set(str(xv))
    #l4=Label(root,text="gui")

L1=Label(root, text="yha heading kya du"
         ,bg="cyan",padx=5,pady=5,font="Courier,40,bold",borderwidth=5)
L1.pack(side=TOP)
L1.grid(row=8, column=8, columnspan=1)
LR = Label(root, text="radius of cylinder = ")
LR.grid(row=10, column=7,padx=10,pady=10)
ER = Entry(root)
ER.grid(row=10, column=8,padx=10,pady=10)


LH = Label(root, text="height of cylinder = ",bg='red')
LH.grid(row=11, column=7,padx=10,pady=10)
EH = Entry(root)
EH.grid(row=11, column=8,padx=10,pady=10)

L4 = Label(root, text="Curved Surface Area = ")
L4.grid(row=14, column=7,padx=10,pady=10)
E4 = Entry(root, textvariable=txtac)
E4.grid(row=14, column=8,padx=10,pady=10)

L5 = Label(root, text="Toatal Surface Area= ")
L5.grid(row=15, column=7,padx=10,pady=10)
E5 = Entry(root, textvariable=txtas)
E5.grid(row=15, column=8,padx=10,pady=10)

L6 = Label(root, text="Volume = ")
L6.grid(row=16, column=7,padx=10,pady=10)
E6 = Entry(root, textvariable=txtav)
E6.grid(row=16, column=8,padx=10,pady=10)

Button(root, text="Solve", command= lambda :adding()).grid(row=12, column=8,padx=10,pady=10)
root.mainloop()