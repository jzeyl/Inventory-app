import sqlite3
import os
import csv
import pandas as pd

os.chdir(r'C:\Users\jeffz\Desktop\inventoryapp\SQL')
os.getcwd()
conn = sqlite3.connect('productinventory.db')#make dB connection

cursor = conn.cursor()

#create estimates table
sql_file = open("createestimates_.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

#create inventory table
sql_file = open("createinventory.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

#see the tables in our database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

estd = conn.execute('select * from estimatesp')
estd.description

#see the tables in our database
cursor.execute("SELECT * FROM estimates;")
print(cursor.fetchall())

# This is the qmark style:
cur.execute("insert into lang values (?, ?)", ("C", 1972))
#insert many added as tuples


estimates_file = open("estimates.csv")
#rows = csv.reader(estimates_file)
rows = pd.read_csv("estimates.csv")
rows = rows.to_numpy()# conver to array
rowstuple = [tuple(x) for x in rows]
cursor.executemany("INSERT INTO estimates VALUES (?,?,?,?)", ((rowstuple,)))

cursor.execute("SELECT * FROM estimates")
print(cursor.fetchall())

# Insert a row of data
cursor.execute("INSERT INTO estimates ('ok','ok','1','ok')")

cursor.execute("SELECT * FROM estimates")
for row in cursor.execute("SELECT * FROM estimates"):
    print(row)
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


conn = get_db_connection()
        cits = conn.execute('SELECT city, province_id, lat, lng FROM canadacities').fetchall()



# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
