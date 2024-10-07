import sqlite3

conn = sqlite3.connect("instance/Anada.db")
cursor = conn.cursor()

Record_temp = []
product_id2 = 0
all = 0

async def saveRecordtemp(id, price, value):
    global product_id2

    cursor.execute("SELECT id, name, information, file_pic, type FROM product WHERE id = ?", (id))
    info = cursor.fetchall()[0]
    # print(info)
    price = int(price)
    await setPrice(price)
    price = format(price, ",")
    temp = info + (price, value) + tuple(str(product_id2))
    Record_temp.append(temp)
    # print(Record_temp)

    product_id2 += 1
    return None

async def getRecordtemp():
    # print(Record_temp)
    return Record_temp

async def setPrice(num):
    global all
    all += num
    # print(price)
    return None

async def getAllPrice():
    value = format(all, ",")
    return value

async def DeleteRecordTemp(id):
    global Record_temp
    global all

    for i in Record_temp:
        if i[6] == id:
            all -= int(i[5].replace(",", ""))
            Record_temp.remove(i)
            break
    return None




