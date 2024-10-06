from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    Actor = Column(Integer, index=True)  # 0 คือ employees, 1 คือ Owners
    user = Column(String, index=True)
    password = Column(String, index=True)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    information = Column(String, index=True)
    file_pic = Column(String(100), index=True)
    pic = Column(LargeBinary, index=True)
    stock_quantity = Column(Integer, index=True)
    type = Column(String, index=True)
    price = Column(String, index=True)
