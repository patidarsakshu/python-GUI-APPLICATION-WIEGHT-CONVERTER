from tkinter import *
root= Tk()
root.title("Weight calculator")
root.geometry('500x500')
root['bg']='Teal'
def from_kg():
    gram=float(uvalue.get())* 1000
    pounds=float(uvalue.get())*2.20462
    ounce=float(uvalue.get())*35.274

    t1.delete("1.0",END)
    t1.insert(END,gram)

    t2.delete("1.0",END)
    t2.insert(END,pounds)

    t3.delete("1.0",END)
    t3.insert(END,ounce)
#HEADING
E1=Label(root,text="Enter  the  weight  in  kg  =",bd="5"
         ,font="impack 20 bold",fg="#033E3E")
uvalue=StringVar()
E2=Entry(root,textvariable=uvalue,bd="5",font="impack 10 bold",fg="Teal")
E3=Label(root ,text='Gram',font="impack 20 bold",fg="#033E3E")
E4=Label(root ,text='Pounds',font="impack 20 bold",fg="#033E3E")
E5=Label(root ,text='Ounce',font="impack 20 bold",fg="#033E3E")
#TEXT BOX
t1=Text(root,height=2, width=20,font="bold",fg="#033E3E")
t2=Text(root,height=2, width=20,font="bold",fg="#033E3E")
t3=Text(root,height=2, width=20,font="bold",fg="#033E3E")
#BUTTON
b1=Button(root , text="Convert", bd="5",font=" impack 20 bold"
          ,fg="#033E3E",command=from_kg)

b2=Button(root,text="EXIT",bd="10",fg="#033E3E",font="impack,10,bold"
          ,command=lambda:exit())
#ENTRY
E1.grid(row=8   ,column=4 ,padx=10,pady=10)
E2.grid(row=8   ,column=5 ,padx=11,pady=11)
E3.grid(row=10  ,column=5 ,padx=10,pady=10)
E4.grid(row=11  ,column=5 ,padx=10,pady=10)
E5.grid(row=12  ,column=5 ,padx=10,pady=10)
t1.grid(row=10  ,column=6 ,padx=10,pady=10)
t2.grid(row=11  ,column=6 ,padx=10,pady=10)
t3.grid(row=12  ,column=6 ,padx=10,pady=10)
b1.grid(row=8   ,column=6 ,padx=10,pady=10)
b2.grid(row=13  ,column=5 ,padx=10,pady=10)
root.mainloop()