import sqlite3

# Connecting to database
conn = sqlite3.connect('example.db')

# Cursor object
cursor = conn.cursor()

# Retrieving specific records using the where clause
cursor.execute("SELECT * FROM employee ORDER BY age")

print(cursor.fetchall())

# Not nessecary
conn.commit()

# Closing
conn.close()
