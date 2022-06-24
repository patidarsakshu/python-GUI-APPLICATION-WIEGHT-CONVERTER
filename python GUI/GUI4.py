from cgitb import text
from tkinter import *
root=Tk()
root.title("my first GUI application")
root.geometry('500x400')
root.minsize(200 ,100)
sakshi=Label(text =''' A GUI is a type of computer human interface on a computer.
 It solves the blank screen problem that confronted early computer users [19].
These early users sat down in front of a computer and faced a blank screen, with only a prompt.
The computer gave the user no indication what the user was to do next. 
GUI are an attempt to solve this blank screen problem.''',bg='pink'
,padx=13, pady=99,font=" comicsansms 19 bold",borderwidth=3,relief=GROOVE
 )
sakshi.pack(side=BOTTOM,anchor="sw",fill=X)
root.mainloop()