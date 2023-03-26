from tkinter import *
import tkinter as tk

import mysql.connector

db=mysql.connector.connect()

win = Tk()
win.title("Bob's Car Rental")
win.geometry("400x400")
radio = IntVar()
r1 = Radiobutton(win, text="Create tables", variable=radio, value=1)
r1.pack(anchor=N)
r2 = Radiobutton(win, text="Drop tables", variable=radio, value=2)
r2.pack(anchor=N)
r3 = Radiobutton(win, text="Populate tables", variable=radio, value=3)
r3.pack(anchor=N)
r4 = Radiobutton(win, text="Query tables", variable=radio, value=4)
r4.pack(anchor=N)
exit_button = Button(win, text="Done", height=5,width=30, command=win.destroy)
exit_button.pack(pady=20)
win.mainloop()
if(radio.get()==1):
    win=Tk()
    win.geometry("400x400")
    win.title("Create tables")
    e=Entry(win)
    e.pack()
    def query():
        label=Label(win,text="Query '"+e.get()+"' passed succesfully.") 
        label.pack()
    submit=Button(win,text="Submit query",command=query)
    submit.pack()
    win.mainloop()