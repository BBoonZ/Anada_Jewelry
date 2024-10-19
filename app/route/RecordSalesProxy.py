from .IDatabase import DatabaseConnection
from .IRecordSales import IRecordManager

class RecordManagerProxy(IRecordManager):
    def __init__(self, real_record_manager: IRecordManager):
        """Initialize the proxy with an instance of the real RecordManager."""
        self.real_record_manager = real_record_manager

    async def save_record(self, id, price, value):
        print(f"Proxy: Saving record with id {id}")
        # Additional checks or logging can be added here
        return await self.real_record_manager.save_record(id, price, value)

    async def get_save_record(self):
        print("Proxy: Fetching saved records")
        return await self.real_record_manager.get_save_record()

    async def add_price(self, id, num):
        print(f"Proxy: Adding price for record id {id}")
        return await self.real_record_manager.add_price(id, num)

    async def set_price(self, id, num=0):
        print(f"Proxy: Setting price for record id {id}")
        return await self.real_record_manager.set_price(id, num)

    async def get_all_price(self):
        print("Proxy: Fetching total price")
        return await self.real_record_manager.get_all_price()

    async def delete_record_temp(self, id):
        print(f"Proxy: Deleting temporary record with id {id}")
        return await self.real_record_manager.delete_record_temp(id)

    async def set_record_temp(self):
        print("Proxy: Setting temporary records")
        return await self.real_record_manager.set_record_temp()

    async def edit_record(self, id, type, value):
        print(f"Proxy: Editing record with id {id}")
        return await self.real_record_manager.edit_record(id, type, value)







