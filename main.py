# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.db import models
from app.db.database import SessionLocal, engine
from app.route.RecordSalesRoute import SalesRouter
from app.route.StockRoute import StockRouter

app = FastAPI()

app.mount("/static", StaticFiles(directory="website/static"), name="static")   # Locate css file
app.mount("/img", StaticFiles(directory="app/img"), name="img")                    # Locate img Product file


#app route
# app.include_router(test.router)
# app.include_router(RecordSales.router)
sales_router = SalesRouter()
stock_router = StockRouter()

app.include_router(sales_router.router)
app.include_router(stock_router.router)

# Create the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


#เวลา run พิมพ์ uvicorn main:app ใน terminal
#python -m uvicorn main:app ใช้คำสั่งนี้รันได้ by คิว
#route /recordsales แสดง html