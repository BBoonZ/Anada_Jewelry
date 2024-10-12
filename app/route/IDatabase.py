import sqlite3

class DatabaseConnection:
    def __init__(self, db_path: str = 'instance/Anada.db'):
        """Initialize the database connection."""
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()
    
    def close(self):
        """Close the database connection."""
        self.conn.close()

# Usage example:
# with DatabaseConnection('instance/Anada.db') as cursor:
#     cursor.execute("SELECT * FROM product")
#     results = cursor.fetchall()
#     print(results)