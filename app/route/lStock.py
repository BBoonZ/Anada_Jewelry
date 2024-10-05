import sqlite3

conn = sqlite3.connect("instance/Anada.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM product")

row = cursor.fetchall()

# print(row)

def getAvailable():
    cursor.execute("SELECT * FROM product WHERE stock_quantity > 0")
    info = cursor.fetchall()
    # print(info)
    return info

