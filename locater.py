from tkinter import *
import tkinter as ttk
import os
import subprocess

root = Tk()
root.title("Locater")

mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

tkvar = StringVar(root)

ttk.Label(mainframe, text="Enter Location").grid(row=1)
e1 = ttk.Entry(mainframe)
e1.grid(row = 1, column = 1)

file1 = open("locater.txt","r")
locater = str(file1.read())
boxsize = len(locater)

if(locater == ""):
    print("its empty")
else:
    e1.insert(boxsize,locater)
    print(locater)
file1.close()

ttk.Button(mainframe, text = "Locate").grid(row = 2, column = 0, sticky = ttk.W, pady = 4)
ttk.Button(mainframe, text = "Load").grid(row = 2, column = 1)

root.mainloop()
