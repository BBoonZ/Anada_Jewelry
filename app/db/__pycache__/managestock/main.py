
from sqlalchemy import Boolean, Column, Engine, ForeignKey, Integer, String, create_engine, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI, Request, Depends, HTTPException, File, UploadFile, Form
from typing import Union, List, Optional
from pydantic import BaseModel
from sqlalchemy.orm import relationship, Session

from fastapi.responses import StreamingResponse
from io import BytesIO

import os

#from .database import sessionmaker ,declarative_base ,create_engine, Base, get_db
SQLALCHEMY_DATABASE_URL = "sqlite:///./test3.db"
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
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    type = Column(String, index=True)
    cost = Column(Integer, index=True)
    quantity = Column(Integer, index=True)
    price = Column(Integer, index=True)
    image_path = Column(LargeBinary, nullable=True)
    image_mime_type = Column(String, nullable=True)  # เก็บ MIME type ของไฟล์

    #owner_id = Column(Integer, ForeignKey("users.id"))

    #owner = relationship("User", back_populates="items")

    #สร้างฐานข้อมูล
    engine = create_engine("sqlite:///./manage2.db")
    Base.metadata.create_all(bind=engine)

#pydantic
class ItemBase(BaseModel):
    name: str  # เพิ่ม name
    description: str
    type: str  # เพิ่ม type
    cost: int  # เพิ่ม cost
    quantity: int  # เพิ่ม quantity
    price: float
    image_path: Optional[str] = None

class ItemCreated(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    class Config:
        from_attribute = True

os.makedirs("uploads", exist_ok=True)
# @app.post("/items", response_model=ItemResponse)
# def create_item(item: ItemCreated, image_path: Optional[UploadFile] = File(None), db: Session = Depends(get_db)):
#     # if image_path:
#     #     file_path = f"images/{image_path.filename}"  # เส้นทางที่จัดเก็บไฟล์
#     #     with open(file_path, "wb") as buffer:
#     #         buffer.write(image_path.file.read())  # เขียนไฟล์ลงไดเรกทอรี
#     # else:
#     #     file_path = None

#     db_item = Item(**item.model_dump())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

@app.post("/items")
def create_item(
    name: str = Form(...),
    description: str = Form(...),
    type: str = Form(...),
    cost: int = Form(...),
    quantity: int = Form(...),
    price: int = Form(...),
    image_file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
 # จัดการการอัปโหลดไฟล์ภาพเป็น BLOB
    image_blob = None
    image_mime_type = None
    if image_file:
        image_blob = image_file.file.read()  # อ่านไฟล์เป็นไบต์ (binary data)
        image_mime_type = image_file.content_type  # เก็บ MIME type ของไฟล์

        # ตรวจสอบประเภทไฟล์ที่รองรับ (JPEG, PNG)
        if image_mime_type not in ["image/jpeg", "image/png", "image/gif", "image/jpg"]:
            raise HTTPException(status_code=400, detail="Unsupported file type")


    # เพิ่มข้อมูลสินค้าใหม่ในฐานข้อมูล
    
    db_item = Item(
        name=name,
        description=description,
        type=type,
        cost=cost,
        quantity=quantity,
        price=price,
        image_path=image_blob,
        image_mime_type=image_mime_type  # เก็บประเภทไฟล์
    )
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

@app.get("/item/{item_id}/image")
def get_item_image(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None or db_item.image_path is None:
        raise HTTPException(status_code=404, detail="Image not found")
    
    # แปลง BLOB เป็นไบต์เพื่อส่งคืน
    image_data = BytesIO(db_item.image_path)
    return StreamingResponse(image_data, media_type=db_item.image_mime_type)

@app.get("/items", response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    db_item = db.query(Item).all()
    return db_item

@app.put("/item/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreated, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    item_data = item.model_dump()
    for key, value in item_data.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/item/{item_id}")
async def delete_item(item_id: int,db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}

