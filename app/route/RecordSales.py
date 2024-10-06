from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from pathlib import Path
from .lStock import getAvailable, getProduct, getTypeProduct

router = APIRouter()


BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Navigate up three levels to the project root
templates = Jinja2Templates(directory=str(BASE_DIR / "website" / "templates"))

@router.get("/recordsales/{type}", response_class=HTMLResponse)
async def recordsales(request: Request, type):
    info = getAvailable()
    if type != "none":
        info = getTypeProduct(type)
    return templates.TemplateResponse("sale_record.html", {"request": request, "Available": info})

@router.get("/recordsales/product/{product_id}", response_class=HTMLResponse)
async def ProductEdit(request: Request, product_id):
    product = getProduct(product_id)
    return templates.TemplateResponse("popup_sale_record_1.html", {"request": request, "Product" : product})

# @router.get("")






