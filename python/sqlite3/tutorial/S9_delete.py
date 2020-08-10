import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM employee")
print("Old: ", cursor.fetchall())

cursor.execute("DELETE FROM EMPLOYEE WHERE age<22")
cursor.execute("SELECT * FROM employee")
print("New: ", cursor.fetchall())

# Run the bottom code if you want to commit it to the original database
# conn.commit() 
conn.close()
