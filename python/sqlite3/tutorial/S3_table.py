import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('example.db')

# Creating a cursor object (for querying and fetching()
cursor = conn.cursor()

# Dropping employee table if it exists
cursor.execute("DROP TABLE IF EXISTS employee")

# Creating a table
sql = """CREATE TABLE employee(
first_name CHAR(20) NOT NULL,
last_name CHAR(20),
age INT,
sex CHAR(1),
income FLOAT)"""

cursor.execute(sql)

# Commit changes (without this, nothing happens)
conn.commit()

# Good practice to close the connection
conn.close()
