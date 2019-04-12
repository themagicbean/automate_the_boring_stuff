'''
Created on Mar 27, 2019

@author: darrenbean
'''

import tkinter
from tkinter import * 
from doctest import master

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Case No.").grid(row=2)
Label(master, text="Date").grid(row=3)
Label(master, text="Time").grid(row=4)
Label(master, text="Dept.").grid(row=5)

DFIRST = Entry(master)
DFIRST.grid(row=0, column=1)
DLAST = Entry(master)
DLAST.grid(row=1, column=1)
CASENO = Entry(master)
CASENO.grid(row=2, column=1)
HRGDATE = Entry(master)
HRGDATE.grid(row=3, column=1)
HRGTIME = Entry(master)
HRGTIME.grid(row=4, column=1)
HRGDEPT = Entry(master)
HRGDEPT.grid(row=5, column=1)

def printtext():
    global DFIRST, DLAST, CASENO, HRGDATE, HRGTIME, HRGDEPT

    FIRSTNAME = DFIRST.get()
    LASTNAME = DLAST.get()
    CASENUMBER = CASENO.get()
    HEARINGDATE = HRGDATE.get()
    HEARINGTIME = HRGTIME.get()
    HEARINGDEPT = HRGDEPT.get()
    
    print(FIRSTNAME + LASTNAME + CASENUMBER + HEARINGDATE + HEARINGTIME + HEARINGDEPT)

def getvariables():
    global DFIRST, DLAST, CASENO, HRGDATE, HRGTIME, HRGDEPT

    FIRSTNAME = DFIRST.get()
    LASTNAME = DLAST.get()
    CASENUMBER = CASENO.get()
    HEARINGDATE = HRGDATE.get()
    HEARINGTIME = HRGTIME.get()
    HEARINGDEPT = HRGDEPT.get()
    
    
    
    
b1 = Button(master, relief="raised", text="Make Fee Waiver", command=printtext)
b1.grid(row=7)
b2 = Button(master, relief="raised", text="Cancel and Quit", command=master.quit)
b2.grid(row=8)


mainloop()

"""
def callback():
    print("click!")
    
b = Button(master, text="ok", command=callback)
b.pack()
"""

"""
def printtext():
    global E
    string = E.get()
    print(string)

E = Entry(master)
E.pack()
E.focus_set()

b = Button(master, text="ok", command=printtext)
b.pack(side="bottom")
"""