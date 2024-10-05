# main.py
from fastapi import FastAPI
from app.route import RecordSales, test
from fastapi.templating import Jinja2Templates
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from app.db import models
from app.db.database import SessionLocal, engine

app = FastAPI()

app.mount("/static", StaticFiles(directory="website/static"), name="static")   # Locate css file
app.mount("/img", StaticFiles(directory="app/img"), name="img")                    # Locate img Product file


#app route
# app.include_router(test.router)
app.include_router(RecordSales.router)


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

#route /test แสดง html