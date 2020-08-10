import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM employee')
print('Old: ', cursor.fetchall())

# Will bring error if table doesn't exist
# cursor.execute("DROP TABLE employee")

cursor.execute("DROP TABLE IF EXISTS employee")
cursor.execute("SELECT * FROM employee")
print('New: ', cursor.fetchall())

# This time I didn't need the commit
conn.commit()
conn.close()
