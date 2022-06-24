from tkinter import *
root =Tk()
root.geometry("655x333")

def A():
    print("5")

def B():
    print("5")

def C():
    print("2")

def sum():
    sum=5+5+2
    print(sum)

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text=" The value of A", command=A)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text=" The value of B", command=B)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text=" The value of C",command=C)
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="THE SUM is", command=sum)
b4.pack(side=LEFT, padx=23)
root.mainloop()