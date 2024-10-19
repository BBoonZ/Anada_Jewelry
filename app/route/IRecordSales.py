from abc import ABC, abstractmethod

class IRecordManager(ABC):

    @abstractmethod
    async def save_record(self, id, price, value):
        pass

    @abstractmethod
    async def get_save_record(self):
        pass

    @abstractmethod
    async def add_price(self, id, num):
        pass

    @abstractmethod
    async def set_price(self, id, num=0):
        pass

    @abstractmethod
    async def get_all_price(self):
        pass

    @abstractmethod
    async def delete_record_temp(self, id):
        pass

    @abstractmethod
    async def set_record_temp(self):
        pass

    @abstractmethod
    async def edit_record(self, id, type, value):
        pass