# Python program to create a close button 
# using destroy Class method 
from tkinter import *  
# Class for tkinter window 
class Window(): 
    def _init_(self): 
        # Creating the tkinter Window 

        self.root = Tk() 

        self.root.geometry("200x100") 
        # Button for closing 

        exit_button = Button(self.root, text="Exit", command=self.Close) 

        exit_button.pack(pady=20) 
        self.root.mainloop() 

    # Function for closing window 
    def Close(self): 
        self.root.destroy() 
# Running test window 
test = Window()