from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from pathlib import Path
from .lStock import getAvailable

router = APIRouter()


BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Navigate up three levels to the project root
templates = Jinja2Templates(directory=str(BASE_DIR / "website" / "templates"))

@router.get("/recordsales", response_class=HTMLResponse)
async def recordsales(request: Request):
    info = getAvailable()
    return templates.TemplateResponse("sale_record.html", {"request": request, "Avaliable": info})

@router.get("/recordsales/<product>", response_class=HTMLResponse)
async def ProductEdit(request: Request):
    return templates.TemplateResponse("pop_sale_record_1.html")






