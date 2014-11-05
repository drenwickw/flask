# Create a SQLIte3 database table

# import the library

import sqlite3

# create a new database if not already extant
conn = sqlite3.connect('my.db')

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute('''CREATE TABLE population
    (city TEXT, state TEXT, population INT)''')

#close the database connection
conn.close()