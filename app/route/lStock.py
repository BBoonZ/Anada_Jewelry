import sqlite3

conn = sqlite3.connect("Anada.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM product")

row = cursor.fetchall()

for i in row:
    print(i[0])