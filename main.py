# main.py
from fastapi import FastAPI
from app.route import test
from fastapi.templating import Jinja2Templates
from fastapi import Request
from starlette.responses import HTMLResponse

app = FastAPI()

app.include_router(test.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


#เวลา run พิมพ์ uvicorn main:app ใน terminal