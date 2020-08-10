import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM employee")
print('Old:', cursor.fetchall())

sql = "UPDATE employee SET age=age+1 WHERE sex='M'"
cursor.execute(sql)

cursor.execute("SELECT * FROM employee")
print('New:', cursor.fetchall())

# This is actually necessary, everything will work but the DB update will not be permanent
conn.commit()
conn.close()
