from .IDatabase import DatabaseConnection

class DeleteProduct:
    def __init__(self):
        self.conn = DatabaseConnection()
        self.cursor = self.conn.cursor
    
    def DeleteProduct(self, product_id: str):
        self.cursor.execute("DELETE FROM product WHERE id = ?", (product_id))
        self.conn.commit()