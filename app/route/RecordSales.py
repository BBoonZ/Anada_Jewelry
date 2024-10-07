from fastapi import APIRouter, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request
from pathlib import Path
from .lStock import getAvailable, getProduct, getTypeProduct
from .IRecordSales import saveRecordtemp, getRecordtemp, getAllPrice, DeleteRecordTemp

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

@router.post("/saveRecord/")
async def saveRecord(id: str=Form(), price: str=Form(), value: str=Form()):
    await saveRecordtemp(id, price, value)
    # print(id, price, value)
    return None

@router.get("/cart")
async def cart_show(request: Request):
    info = await getRecordtemp()
    allprice = await getAllPrice()
    # print(info)
    return templates.TemplateResponse("popup_sale_record_2.html", {"request": request, "Product" : info, "All_price": allprice})

@router.get("/cart/delete/{product_id}")
async def cart_delete(request: Request, product_id):
    await DeleteRecordTemp(product_id)
    return RedirectResponse(url="/cart", status_code=303)

@router.post("/cart")
async def summitRecord():
    info = await getRecordtemp()
    # for i in info:
    #     DeleteRecordTemp(i[0], i[5])
    return None





