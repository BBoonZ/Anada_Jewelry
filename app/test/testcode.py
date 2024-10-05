import sqlite3
from ..route.lStock import DecreaseProduct

# conn = sqlite3.connect("instance/Anada.db")

# cursor = conn.cursor()

# cursor.execute('INSERT INTO product(name) VALUES ("Pig")')
# conn.commit()

DecreaseProduct(6)