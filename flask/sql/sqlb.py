import sqlite3

conn = sqlite3.connect('cars')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE inventory
    (make TEXT, model TEXT, quantity INT)''')