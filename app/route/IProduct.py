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

# สร้าง Product
def CreateProduct(name, type, info, file_pic, stock_quantity):
    # เส้นทางของไฟล์ภาพที่คุณต้องการเพิ่ม
    # Construct the absolute path to the img folder
    img_folder_path = Path(__file__).resolve().parent.parent / 'img'
    image_name = file_pic

    image_path_jpg = img_folder_path / f'{image_name}.jpg'
    image_path_jpeg = img_folder_path / f'{image_name}.jpeg'
    image_path_png = img_folder_path / f'{image_name}.png'

    if image_path_jpg.exists():
        image_path = image_path_jpg
        image_name = f'{image_name}.jpg'
    elif image_path_jpeg.exists():
        image_path = image_path_jpeg
        image_name = f'{image_name}.jpeg'
    elif image_path_png.exists():
        image_path = image_path_png
        image_name = f'{image_name}.png'
    else:
        raise FileNotFoundError("Image not found in .jpg, .jpeg, or .png formats")

    # แปลงภาพเป็นไบนารี
    image_data = image_to_binary(image_path)

    # รันคำสั่ง INSERT เพื่อเพิ่มข้อมูลภาพ
    cursor.execute('INSERT INTO product (name, file_pic, pic, stock_quantity) VALUES (?, ?, ?, ?)', (name, image_name, image_data, stock_quantity))

    # บันทึกการเปลี่ยนแปลง
    conn.commit()

    # แสดงข้อความยืนยัน
    print("Image inserted successfully.")

    # ปิดการเชื่อมต่อ
    conn.close()