from pathlib import Path
from .IDatabase import DatabaseConnection

class ICreateProduct:
    def __init__(self):
        self.conn = DatabaseConnection()
        self.cursor = self.conn.cursor()

    def image_to_binary(self, image_path):
        """Convert the image to binary data."""
        with open(image_path, 'rb') as file:
            return file.read()

    def create_product(self, name, info, file_pic, stock_quantity, product_type, price):
        """Insert a new product with an image into the database."""
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

        # Convert the image to binary
        image_data = self.image_to_binary(image_path)

        # Insert the product into the database
        self.cursor.execute(
            'INSERT INTO product(name, information, file_pic, pic, stock_quantity, type, price) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (name, info, image_name, image_data, stock_quantity, product_type, price)
        )

        # Commit the transaction
        self.conn.commit()

        print("Product with image inserted successfully.")

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()

# Usage Example:
# product_manager =ICreateProduct('instance/Anada.db')
# product_manager.create_product('Product Name', 'Product Info', 'image_filename', 10, 'Product Type', 29.99)
# product_manager.close_connection()
