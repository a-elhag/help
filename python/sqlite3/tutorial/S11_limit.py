import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM employee")
print("All: ", cursor.fetchall())

print("\nLimit 3")
cursor.execute("SELECT * FROM employee LIMIT 3")
print("No offset: ", cursor.fetchall())

cursor.execute("SELECT * FROM employee LIMIT 3 OFFSET 2")
print("Offset: ", cursor.fetchall())

conn.commit()
