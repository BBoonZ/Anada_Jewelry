import sqlite3
import optparse
from PIL import Image
from pathlib import Path

# ฟังก์ชันเพื่อแปลงภาพเป็นไบนารี
def image_to_binary(image_path):
    with open(image_path, 'rb') as file:
        return file.read()

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('instance/Anada.db')
cursor = conn.cursor()

# เส้นทางของไฟล์ภาพที่คุณต้องการเพิ่ม
# Construct the absolute path to the img folder
img_folder_path = Path(__file__).resolve().parent.parent / 'img'
image_path = img_folder_path / 'hippo.jpg'  # แทนที่ด้วยเส้นทางไฟล์ภาพของคุณ

# แปลงภาพเป็นไบนารี
image_data = image_to_binary(image_path)

# รันคำสั่ง INSERT เพื่อเพิ่มข้อมูลภาพ
cursor.execute('INSERT INTO product (name, file_pic, pic, stock_quantity) VALUES ("hippo", ?, ?, 5)', ('hippo.jpg', image_data))

# บันทึกการเปลี่ยนแปลง
conn.commit()

# แสดงข้อความยืนยัน
print("Image inserted successfully.")

# ปิดการเชื่อมต่อ
conn.close()



