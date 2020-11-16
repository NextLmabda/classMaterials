import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

#conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')

table = conn.execute('SELECT * FROM students')

print(table.fetchall())
print ("Table created successfully")
conn.close()