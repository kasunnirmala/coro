from tkinter import *
import tkinter as ttk

import sys
import glob
import serial
from pynput.keyboard import Key, Controller

from threading import Thread

root = Tk()
root.title("Project KDU")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)

#getting serial ports
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

#running the connection script for remote
def con_serial(comein):
    file1 = open("locater.txt","w")
    locater = file1.read()
    if(locater != ""):
        print(locater)
    print(comein + "  AAAAAAA")
    ser = serial.Serial(comein, 9600)
    
    release = True
    
    while True:
        bytesToRead = ser.inWaiting()
        keyboard = Controller()
        cc=str(ser.readline())
        print(cc)
        ss=(cc[2:3])
     
        while not ser.inWaiting():
            print(ss)

            if ss=='U':
                release =True
                keyboard.press(Key.up)
            elif ss== 'D':
                release =True
                keyboard.press(Key.down)
            elif ss=='L':
                release =True
                keyboard.press(Key.left)
            elif ss=='R':
                release =True
                keyboard.press(Key.right)
            elif ss=='S':
                if release:
                    release=False
                    keyboard.release(Key.down)
                    keyboard.release(Key.left)
                    keyboard.release(Key.up)
                    keyboard.release(Key.right)
                    keyboard = Controller()

                
# Dictionary with options
tempchoi = serial_ports()
choices = { i : 5 for i in tempchoi} #converting list to dictionary
tkvar.set('Select COM') # set the default option

#popup menu for selection/ view of dropdown menu
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a COM Port").grid(row = 3, column = 1)
popupMenu.grid(row = 4, column =1)

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

# on change dropdown value
def change_dropdown(*args):
    try:
        thread=Thread(target=con_serial, args=(tkvar.get(),))
        thread.start()
    except Exception as identifier:
        print(identifier)

    '''ttk.Label(mainframe, text="Enter Location").grid(row=1)
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
    ttk.Button(mainframe, text = "Load").grid(row = 2, column = 1)'''
    print( tkvar.get() )
    

# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
