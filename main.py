from tkinter import *
import tkinter as tk
import os
import mysql.connector
htmlstring = "start about.html"
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="NOah2003",
    database="cp363_a3"
)
cursor=db.cursor() #db cursor







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
r5 = Radiobutton(win, text="About", variable=radio, value=5)
r5.pack(anchor=N)
exit_button = Button(win, text="Done", height=5,width=30, command=win.destroy)
exit_button.pack(pady=20)
win.mainloop()
if(radio.get()==1): #checks which radiobutton was selected
    win=Tk()
    win.geometry("400x400")
    win.title("Create tables")
    e=Entry(win)
    e.pack()
    def query(): #e.get() gets the input into entrybox e, gets query from user input (string)
        cursor.execute(e.get()) #executes query
        label=Label(win,text="Query '"+e.get()+"' passed succesfully.")  #adds label that executed properly
        label.pack()
    submit=Button(win,text="Submit query",command=query)
    submit.pack()
    win.mainloop()
elif(radio.get()==2):
    win=Tk()
    win.geometry("400x400")
    win.title("Drop tables")
    e=Entry(win)
    e.pack()
    def query(): #e.get() gets the input into entrybox e, gets query from user input (string)
        cursor.execute(e.get()) #executes query
        label=Label(win,text="Query '"+e.get()+"' passed succesfully.")  #adds label that executed properly
        label.pack()
    submit=Button(win,text="Submit query",command=query)
    submit.pack()
    win.mainloop()
elif(radio.get()==3):
    win=Tk()
    win.geometry("400x400")
    win.title("Populate tables")
    e=Entry(win)
    e.pack()
    def query(): #e.get() gets the input into entrybox e, gets query from user input (string)
        cursor.execute(e.get()) #executes query
        label=Label(win,text="Query '"+e.get()+"' passed succesfully.")  #adds label that executed properly
        label.pack()
    submit=Button(win,text="Submit query",command=query)
    submit.pack()
    win.mainloop()
elif(radio.get()==4):
    query1="SELECT * FROM vehicle WHERE EXISTS (SELECT * FROM employee WHERE employee.BranchID = vehicle.BranchID);"
    query2="SELECT CardHolderName, COUNT(CardType) FROM paymentTransaction GROUP BY CardHolderName;"
    query3= "SELECT Name FROM customer UNION SELECT Name FROM employee ORDER BY Name;"
    query4= "SELECT customer.Age FROM customer LEFT JOIN employee ON customer.Age= employee.Age WHERE customer.Age > 1;"
    query5= "SELECT COUNT(ID), Gender FROM customer GROUP BY Gender HAVING COUNT(ID) > 1000;"
    query6= "SELECT year, AVG(price) FROM vehicle GROUP BY year HAVING AVG(price)< (SELECT AVG(price) FROM vehicle);"
    query7= "SELECT ContractID FROM vehicle v LEFT JOIN contract c ON c.LicensePlate = v.LicensePlate;"
    win=Tk()
    win.geometry("400x400")
    win.title("Query tables")
    def query(): 
        match ladio.get():
            case 1:
                cursor.execute(query1)
                result=cursor.fetchall()
                for r in result:
                    print(r)
                win.destroy()
            case 2:
                cursor.execute(query2)
                result=cursor.fetchall()
                for r in result: 
                    print(r)
                win.destroy()
            case 3:
                cursor.execute(query3)
                result=cursor.fetchall()
                for r in result:
                    print(r)
                win.destroy()
            case 4:
                cursor.execute(query4)
                result=cursor.fetchall()
                for r in result:
                    print(r)
                win.destroy()
            case 5:
                cursor.execute(query5)
                result=cursor.fetchall()
                for r in result:
                    print(r)
                win.destroy()
            case 6:
                cursor.execute(query6)
                result=cursor.fetchall()
                for r in result:
                    print(r)
                win.destroy()
            case 7:
                cursor.execute(query7)
                result=cursor.fetchall()
                for r in result:
                    print(r)
                win.destroy()
            case _:
                print("No query selected")
                win.destroy()
    ladio=IntVar()
    l1 = Radiobutton(win, text="Query 1", variable=ladio, value=1)
    l1.pack(anchor=N)
    l2 = Radiobutton(win, text="Query 2", variable=ladio, value=2)
    l2.pack(anchor=N)
    l3 = Radiobutton(win, text="Query 3", variable=ladio, value=3)
    l3.pack(anchor=N)
    l4 = Radiobutton(win, text="Query 4", variable=ladio, value=4)
    l4.pack(anchor=N)
    l5 = Radiobutton(win, text="Query 5", variable=ladio, value=5)
    l5.pack(anchor=N)
    l6 = Radiobutton(win, text="Query 6", variable=ladio, value=6)
    l6.pack(anchor=N)
    l7 = Radiobutton(win, text="Query 7", variable=ladio, value=7)
    l7.pack(anchor=N)
    submit=Button(win,text="Submit query",command=query)
    submit.pack()
    win.mainloop()
elif(radio.get()==5):
    os.system(htmlstring)