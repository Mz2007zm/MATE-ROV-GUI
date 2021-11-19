#!/usr/bin/python
import tkinter as tk
import time
import sys
import os
from tkinter import messagebox, RIGHT, LEFT, StringVar
########################
root = tk.Tk()
root.geometry('400x300')
root.resizable(0,0)
root.config(bg ='gray')
root.title("Countdown Timer Verision 0.0.1")

# #  # #

minute=StringVar()
second=StringVar()
hours=StringVar()

sec = StringVar()
mins= StringVar()
hrs= StringVar()

# #  # #

tk.Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=200, y=155) # Seconds
tk.Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=175, y=155) # Mins
tk.Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=150, y=155) # Hours

# #  # #

minute.set('00')
second.set('00')
hours.set('00')

sec.set('00')
mins.set('00')
hrs.set('00')
# #  # #

def countdown():
    print("hello") #testing, working but code not working
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)

        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)
        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1

tk.Button(root, text='START', bd ='5', command = countdown, bg = 'white', font = 'arial 10 bold').place(x=150, y=210)
# #  # #

def stop():
    minute.set('00')
    second.set('00')
    hours.set('00')
    sec.set('00')
    mins.set('00')
    hrs.set('00')
    root.destroy()
    python = sys.executable
    os.execl(python, python, * sys.argv)



tk.Button(root, text='STOP', bd ='5', command = stop, bg = 'white', font = 'arial 10 bold').place(x=150, y=250)
##############################################################
top = tk.Tk()
top.geometry("1920x1080")

def button1():
   tk.messagebox.showinfo( "Hello Python", "Hello World")

B = tk.Button(top, text ="Hello", command = button1)

B.pack(side=RIGHT, padx=25, pady=25)

# # # # # # # # # # # # # # # # # # # # #

def button2():
   tk.messagebox.showinfo( "Hello Python2", "Hello World2")

Bu = tk.Button(top, text ="Hello2", command = button2)

Bu.pack(side=RIGHT, padx=15, pady=20)
##############
top.mainloop()
##############
