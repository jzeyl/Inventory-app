import sqlite3
import os
import csv
import pandas as pd

os.chdir(r'C:\Users\jeffz\Desktop\inventoryapp\SQL')
os.getcwd()
conn = sqlite3.connect('productinventory.db')#make dB connection
cursor = conn.cursor()

########3Database setup
#create estimates table
sql_file = open("create_estimates.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

#create inventory table
sql_file = open("createinventory.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

#######seed inventory data from csv
df = pd.read_csv('inventory.csv')
df.to_sql('Inventory', conn, if_exists='append', index=False)
cursor.execute("SELECT * FROM Inventory")
print(cursor.fetchall())

#see the tables in our database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

#see column names of the
estd = conn.execute('select * from estimates')
estd.description

#see column names of the
estd = conn.execute('select * from inventory')
estd.description

#see the data in a table
cursor.execute("SELECT * FROM Inventory;")
print(cursor.fetchall())
conn.close()

