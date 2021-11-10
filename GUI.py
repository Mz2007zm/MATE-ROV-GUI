#!/usr/bin/python
import tkinter as tk
from tkinter import messagebox
top = tk.Tk()
top.geometry("500x500")
# Code to add widgets will go here...

def helloCallBack():
   tk.messagebox.showinfo( "Hello Python", "Hello World")

B = tk.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

#helloCallBack()
