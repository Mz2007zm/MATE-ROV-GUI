#!/usr/bin/python
import tkinter as tk
from tkinter import messagebox, RIGHT
top = tk.Tk()
top.geometry("1920x1080")
# Code to add widgets will go here...

def button1():
   tk.messagebox.showinfo( "Hello Python", "Hello World")

B = tk.Button(top, text ="Hello", command = button1)

B.pack(side=RIGHT, padx=25, pady=25)

# # # # #

def button2():
   tk.messagebox.showinfo( "Hello Python2", "Hello World2")

Bu = tk.Button(top, text ="Hello2", command = button2)

Bu.pack(side=RIGHT, padx=15, pady=20)
top.mainloop()
