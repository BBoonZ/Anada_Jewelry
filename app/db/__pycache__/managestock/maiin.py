
from sqlalchemy import Boolean, Column, Engine, ForeignKey, Integer, String, create_engine


from fastapi import FastAPI, Request, Depends
from typing import Union, List
from pydantic import BaseModel
from sqlalchemy.orm import relationship, Session

from .database import sessionmaker ,declarative_base ,create_engine, Base, get_db
 
app = FastAPI()

#class Item(BaseModel):
    #name: str
    #price: float
#ORM class
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
class Item(BaseModel):
    title: str
    description: str
    price : float

class ItemCreated(Item):
    pass

class ItemResponse(Item):
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
    return db_item

@app.get("/items", response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    db_item = db.query(Item).all()
    return db_item

# @app.put

# @app.delete

