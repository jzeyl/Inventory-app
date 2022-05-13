import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

import sqlite3
import os
import csv
import pandas as pd

#connect to database
conn = sqlite3.connect('productinventory.db')#make dB connection
cursor = conn.cursor()

os.chdir(r'C:\Users\jeffz\Desktop\inventoryapp\SQL')
os.getcwd()


#get date and time for stamp on each record
dt = datetime.now()
date = dt.strftime("%d/%m/%Y")
time = dt.strftime("%H:%M:%S")


#function to print values
def show_entry_fields():
    global record
    record = (a1.get(), b1.get(), c1.get(),date,time)
    print("Estimate number: %s\n Product number: %s\n Quantity: %s\n Date: %s\n Time: %s" % 
    (a1.get(), b1.get(), c1.get(),date,time))

#add estimate to database
def addtodatabase():
    global record
    record = (a1.get(), b1.get(), c1.get(),date,time)
    # Insert a row of data
    cursor.execute("INSERT INTO Estimates VALUES (?, ?, ?, ?,?)", (record))
    # Save (commit) the changes
    conn.commit()
    print(type(record))
    messagebox.showinfo('information', Record has been added to the database.')

#create gui
window = tk.Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x200')
window.configure(background = "grey");

#labels
a = tk.Label(window ,text = "Estimate number").grid(row = 0,column = 0)
b = tk.Label(window ,text = "Product number").grid(row = 1,column = 0)
c = tk.Label(window ,text = "Quantity").grid(row = 2,column = 0)

#entries
a1 = tk.Entry(window)
a1.grid(row = 0,column = 1)
b1 = tk.Entry(window)
b1.grid(row = 1,column = 1)
c1 = tk.Entry(window)
c1.grid(row = 2,column = 1)

btn = ttk.Button(window ,text="Show record", command = show_entry_fields).grid(row=6,column=0)
btn = ttk.Button(window ,text="Add entry to database", command = addtodatabase).grid(row=6,column=1)
btn = ttk.Button(window ,text="Plot current inventory", command = show_entry_fields).grid(row=6,column=2)
btn = ttk.Button(window ,text="View estimates table", command = addtodatabase).grid(row=7,column=1)
window.mainloop()
