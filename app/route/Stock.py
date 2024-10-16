from .IDatabase import DatabaseConnection
from .ICreateProduct import ICreateProduct
from .UploadFile import UploadRoute

class ProductManager:
    def __init__(self):
        """Initialize the ProductManager with the database cursor and connection."""
        self.conn = DatabaseConnection()
        self.cursor = self.conn.cursor
        self.ICreate = ICreateProduct()
        self.IUpload = UploadRoute()

    def get_all(self):
        """Retrieve all products with stock quantities greater than 0."""
        self.cursor.execute("SELECT * FROM product")
        products = self.cursor.fetchall()
        return products

    def get_available(self):
        """Retrieve all products with stock quantities greater than 0."""
        self.cursor.execute("SELECT * FROM product WHERE stock_quantity > 0")
        products = self.cursor.fetchall()
        return products

    def get_product(self, product_id):
        """Retrieve a specific product by its ID."""
        self.cursor.execute("SELECT * FROM product WHERE id = ?", (product_id,))
        product = self.cursor.fetchall()[0]
        return product

    def get_type_product(self, product_type):
        """Retrieve all products of a specific type."""
        self.cursor.execute("SELECT * FROM product WHERE type = ?", (product_type,))
        products = self.cursor.fetchall()
        return products

    def decrease_product(self, product_ids, num=1):
        """Decrease the stock quantity of the given product(s)."""
        # Fetch current stock quantity
        self.cursor.execute("SELECT stock_quantity FROM product WHERE id = ?", (product_ids,))
        current_quantity = self.cursor.fetchall()[0][0]

        # Update stock quantity
        new_quantity = int(current_quantity) - int(num)
        self.cursor.execute("UPDATE product SET stock_quantity = ? WHERE id = ?", (new_quantity, product_ids))
        self.conn.commit()
        print("DecreaseSuccess")

    def increase_product(self, product_id, num=1):
        """Increase the stock quantity of a specific product."""
        self.cursor.execute("SELECT stock_quantity FROM product WHERE id = ?", (product_id,))
        current_quantity = self.cursor.fetchall()[0][0]

        # Update stock quantity
        new_quantity = int(current_quantity) + (num)
        self.cursor.execute("UPDATE product SET stock_quantity = ? WHERE id = ?", (new_quantity, product_id))
        self.conn.commit()
        print("IncreaseSuccess")

    async def setProduct(self, id, name, type, detail, price, stock, pic):
        type = self.ICreate.convert_type(type)
        #Delete Pic
        self.cursor.execute("SELECT file_pic FROM product WHERE id = ? AND file_pic != 'main.png'", (id,))
        file = self.cursor.fetchall()[0][0]
        if (file):
            await self.IUpload.delete_file(file)
            await self.IUpload.upload_file(pic)

        self.cursor.execute("UPDATE product SET name = ?, information = ?, stock_quantity = ?, type = ?, price = ? , file_pic = ? WHERE id = ?", (name, detail, stock, type, price, pic.filename, id))
        self.conn.commit()

# DecreaseProduct([6])
# IncreaseProduct("6")
# getProduct("7")