
from sqlalchemy import Boolean, Column, Engine, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI, Request, Depends, HTTPException
from typing import Union, List
from pydantic import BaseModel
from sqlalchemy.orm import relationship, Session

#from .database import sessionmaker ,declarative_base ,create_engine, Base, get_db
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()

#class Item(BaseModel):
    #name: str
    #price: float
#ORM class
# สร้างตารางในฐานข้อมูล
Base.metadata.create_all(bind=engine)

# ตรวจสอบการสร้างตารางใหม่
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)
    #owner_id = Column(Integer, ForeignKey("users.id"))

    #owner = relationship("User", back_populates="items")

    #สร้างฐานข้อมูล
    engine = create_engine("sqlite:///./test.db")
    Base.metadata.create_all(bind=engine)

#pydantic
class ItemBase(BaseModel):
    title: str
    description: str
    price : float

class ItemCreated(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    class Config:
        from_attribute = True


@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreated, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/item/{item_id}", response_model=ItemResponse)
def read_item(item_id: int,db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items", response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    db_item = db.query(Item).all()
    return db_item

# @app.put

# @app.delete

