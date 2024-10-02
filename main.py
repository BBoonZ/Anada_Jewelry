# main.py
from fastapi import FastAPI
from app.route import RecordSales, test
from fastapi.templating import Jinja2Templates
from fastapi import Request
from starlette.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="website/static"), name="static")   # Locate css file

#app route
app.include_router(test.router)
app.include_router(RecordSales.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


#เวลา run พิมพ์ uvicorn main:app ใน terminal