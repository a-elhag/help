import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('example.db')

# Creating a cursor object
cursor = conn.cursor()

# Retrieving Data
cursor.execute("""SELECT * FROM employee""")

# Fetching 1st row from the table
result = cursor.fetchone()
print('1st Row')
print(result)

# Retrieving Data
cursor.execute("""SELECT * FROM employee""")

# Fetching all rows from the table
result = cursor.fetchall()
print('All Rows')
print(result)

# Commit (don't think this is useful for this example)
conn.commit()

# Close
conn.close()
