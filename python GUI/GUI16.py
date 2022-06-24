from tkinter import *
root= Tk()
root.title("weight calculator")
root.geometry('500x400')
root['bg']='grey'
def from_kg():
    gram=float(uservalue.get()) * 1000
    pounds=float(uservalue.get()) *2.20462
    ounce=float(uservalue.get()) *35.274
    t1.delete("1.0",END)
    t1.insert(END,gram)

    t2.delete("1.0",END)
    t2.insert(END,pounds)

    t3.delete("1.0",END)
    t3.insert(END,ounce)

e1=Label(root,text="Enter  the  weight  in  kg  =",font=("comicsansms", 19,"bold"))
uservalue=StringVar()
e2= Entry(root,textvariable=uservalue)
e3=Label(root ,text='Gram',font=("comicsansms", 19,"bold"))
e4=Label(root ,text='Pounds',font=("comicsansms", 19,"bold"))
e5=Label(root ,text='Ounce',font=("comicsansms", 19,"bold"))

t1=Text(root,height=2, width=20)
t2=Text(root,height=2, width=20)
t3=Text(root,height=2, width=20)

b1=Button(root , text="Convert",command=lambda:from_kg
,font=("comicsansms", 19,"bold")).grid(row=2 ,column=4)

e1.grid(row=2  ,column= 1 )
e2.grid(row=2  ,column= 2)
e3.grid(row=5  ,column= 1)
e4.grid(row=5  ,column= 2 )
e5.grid(row=5  ,column= 5)
t1.grid(row=7  ,column= 1)
t2.grid(row=7  ,column= 2)
t3.grid(row=7  ,column= 5)

root.mainloop()
   
    



