from .IDatabase import DatabaseConnection
from .IRecordSales import IRecordManager

class RecordManager(IRecordManager):

    def __init__(self):
        """Initialize the RecordManager with the database cursor and default values."""
        self.cursor = DatabaseConnection().cursor
        self.Record_temp = []
        self.all = []
        self.temp_id = 1

    async def save_record(self, id, price, value):
        """Save a temporary record with product info, price, and value."""
        self.cursor.execute("SELECT id, name, information, file_pic, type FROM product WHERE id = ?", (id,))
        info = self.cursor.fetchall()[0]
        price = int(price)
        await self.add_price(self.temp_id, price)
        formatted_price = format(price, ",")
        temp = info + (formatted_price, value, self.temp_id)
        self.Record_temp.append(temp)
        self.temp_id += 1

    async def get_save_record(self):
        """Return the list of temporary records."""
        return self.Record_temp

    async def add_price(self, id, num):
        """Update the total price by adding the given value."""
        self.all.append([id, num])

    async def set_price(self, id, num=0):
        for i in self.all:
            if i[0] == int(id):
                i[1] = num
                break

    async def get_all_price(self):
        """Return the formatted total price."""
        num = 0
        for i in self.all:
            num += int(i[1])
        return format(num, ",")

    async def delete_record_temp(self, id):
        """Delete a temporary record based on the product ID."""
        for record in self.Record_temp:
            if record[7] == int(id):
                await self.set_price(record[7])
                self.Record_temp.remove(record)
                break

    async def set_record_temp(self):
        self.Record_temp = []
        self.add = []

    async def edit_record(self, id, type, value):
        for i, j in enumerate(self.Record_temp):
            if j[7] == int(id):
                if type == "price":
                    await self.set_price(id, int(value.replace(",", "")))
                    try:
                        value = int(value.replace(",", ""))
                        value = format(value, ",")
                    except:
                        pass
                    index_to_delete = 5
                    j = j[:index_to_delete] + (value,) + j[index_to_delete + 1:]
                    self.Record_temp[i] = j
                else:
                    index_to_delete = 6
                    j = j[:index_to_delete] + (value,) + j[index_to_delete + 1:]
                    self.Record_temp[i] = j
                    print(j[5])
                    await self.edit_record(id, "price", str(int(value)*(int(j[5].replace(",", "")))))
                break
