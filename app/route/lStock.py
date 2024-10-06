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

def getProduct(product_id):
    cursor.execute("SELECT * FROM product WHERE id = ?", (product_id))
    info = cursor.fetchall()[0]
    # print(info)
    return info

def getTypeProduct(type: str):
    cursor.execute("SELECT * FROM product WHERE type = ?", (type))
    info = cursor.fetchall()
    return info

def DecreaseProduct(product_id):
    for i in product_id:
        i_str = str(i)
        cursor.execute("SELECT stock_quantity FROM product WHERE id = ?", (i_str))
        values = cursor.fetchall()[0][0]    # เอาแค่ value

        cursor.execute("UPDATE product SET stock_quantity = ? WHERE id = ?", (values-1, i_str))
        conn.commit()
    print("DecreaseSuccess")

def IncreaseProduct(product_id, num=1):
    cursor.execute("SELECT stock_quantity FROM product WHERE id = ?", (product_id))
    values = cursor.fetchall()[0][0]    # เอาแค่ value

    cursor.execute("UPDATE product SET stock_quantity = ? WHERE id = ?", (values+num, product_id))
    conn.commit()

    print("IncreaseSuccess")

# DecreaseProduct([6])
# IncreaseProduct("6")
# getProduct("7")