import sqlite3

# Connect to database
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Preparing stuff to be inserted into it database
# DON'T DO IT THIS WAY, SQL INJECTION
cursor.execute("""INSERT INTO employee(first_name, last_name, age, sex, income)
               VALUES ('Ramya', 'Rama Priya', 27, 'F', 9000)""")


cursor.execute("""INSERT INTO employee(first_name, last_name, age, sex, income)
               VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)""")


cursor.execute("""INSERT INTO employee(first_name, last_name, age, sex, income)
               VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)""")


cursor.execute("""INSERT INTO employee(first_name, last_name, age, sex, income)
               VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)""")


cursor.execute("""INSERT INTO employee(first_name, last_name, age, sex, income)
               VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)""")  

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
                                                                                           
                                                                                           
                                                                                           
                                                                                           
