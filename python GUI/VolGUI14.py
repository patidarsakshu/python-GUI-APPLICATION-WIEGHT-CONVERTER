from tkinter import *
import math
root = Tk()
root.title("Volume Of Sphere")
root.geometry("400x550")
root['bg']='cyan'
txta = StringVar()
def adding():
    
    a = float(E1.get())
    x=((4/3)*3.14*a**3)
    txta.set(str(x))
Ac=Label(root,text="GUI Application for calculate Volume Of Sphere")
Ac.grid(row=5,column=15)
L1 = Label(root, text="Enter the value of radius"
         ,font="halvetica,16,bold",borderwidth=5)
L1.grid(row=9, column=10)
LB = Label(root, text="radius = ")
LB.grid(row=10, column=10)
E1 = Entry(root)
E1.grid(row=10, column=12)
LB = Label(root, text="volume = ")
LB.grid(row=12, column=10)
E4 = Entry(root, textvariable=txta)
E4.grid(row=12, column=12)

Button(root, text="Solve", command=lambda: adding()).grid(row=11, column=12)
root.mainloop()