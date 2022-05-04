import sqlite3
import os

os.chdir(r'C:\Users\jeffz\Desktop\inventoryapp\SQL')
os.getcwd()
conn = sqlite3.connect('productinventory.db')#make dB connection

cursor = conn.cursor()


#create estimates table
sql_file = open("createestimates.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

#create inventory table
sql_file = open("createinventory.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)

#see the tables in our database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

estimates_file = open("estimates.csv")
rows = csv.reader(estimates_file)
cursor.executemany("INSERT INTO estimates VALUES (?,?,?,?)", rows)

cursor.execute("SELECT * FROM estimates")
print(cursor.fetchall())

# Insert a row of data
cursor.execute("SELECT * FROM estimates")
for row in cursor.execute("SELECT * FROM estimates"):
    print(row)
# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()


conn = get_db_connection()
        cits = conn.execute('SELECT city, province_id, lat, lng FROM canadacities').fetchall()



# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
