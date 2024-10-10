from .IDatabase import DatabaseConnection

class RecordManager:
    def __init__(self):
        """Initialize the RecordManager with the database cursor and default values."""
        self.cursor = DatabaseConnection().cursor
        self.Record_temp = []
        self.product_id2 = 1
        self.all = 0

    async def save_record_temp(self, id, price, value):
        """Save a temporary record with product info, price, and value."""
        # Fetch product details based on the product ID
        self.cursor.execute("SELECT id, name, information, file_pic, type FROM product WHERE id = ?", (id,))
        info = self.cursor.fetchall()[0]

        # Format the price and update the total price
        price = int(price)
        await self.set_price(price)
        formatted_price = format(price, ",")

        # Add the new record to the temporary records list
        temp = info + (formatted_price, value, str(self.product_id2))
        self.Record_temp.append(temp)

        # Increment the product ID counter
        self.product_id2 += 1

    async def get_record_temp(self):
        """Return the list of temporary records."""
        return self.Record_temp

    async def set_price(self, num):
        """Update the total price by adding the given value."""
        self.all += num

    async def get_all_price(self):
        """Return the formatted total price."""
        return format(self.all, ",")

    async def delete_record_temp(self, id):
        """Delete a temporary record based on the product ID."""
        for record in self.Record_temp:
            if record[6] == id:
                # Update the total price and remove the record
                self.all -= int(record[5].replace(",", ""))
                self.Record_temp.remove(record)
                break





