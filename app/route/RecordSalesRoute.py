from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .RecordSalesProxy import RecordManagerProxy
from .RecordSales import RecordManager
from .Stock import ProductManager

class SalesRouter:
    def __init__(self):
        self.router = APIRouter()
        self.IRecord = RecordManagerProxy(RecordManager())
        self.IStock = ProductManager()
        BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Navigate up three levels to the project root
        self.templates = Jinja2Templates(directory=str(BASE_DIR / "website" / "templates"))

        # Define routes
        self.router.add_api_route("/recordsales/{type}", self.record_sales_home, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/recordsales/product/{product_id}", self.product_edit, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/saveRecord/", self.save_record, methods=["POST"])
        self.router.add_api_route("/cart", self.cart_show, methods=["GET"])
        self.router.add_api_route("/cart/delete/{product_id}", self.cart_delete, methods=["GET"])
        self.router.add_api_route("/cart/edit/{product_id}/{type}/{value}", self.card_edit, methods=["POST"])
        self.router.add_api_route("/cart", self.summit_record, methods=["POST"])

    async def record_sales_home(self, request: Request, type: str):
        info = self.IStock.get_available()
        if type != "none":
            info = self.IStock.get_type_product(type)
        return self.templates.TemplateResponse("sale_record.html", {"request": request, "Available": info})

    async def product_edit(self, request: Request, product_id: str):
        product = self.IStock.get_product(product_id)
        return self.templates.TemplateResponse("popup_sale_record_1.html", {"request": request, "Product": product})

    async def save_record(self, id: str = Form(), price: str = Form(), value: str = Form()):
        await self.IRecord.save_record(id, int(price)*int(value), value)
        return None

    async def cart_show(self, request: Request):
        info = await self.IRecord.get_save_record()
        all_price = await self.IRecord.get_all_price()
        return self.templates.TemplateResponse("popup_sale_record_2.html", {"request": request, "Product": info, "All_price": all_price})

    async def cart_delete(self, request: Request, product_id: str):
        await self.IRecord.delete_record_temp(product_id)
        return RedirectResponse(url="/cart", status_code=303)

    async def card_edit(self, product_id: str, type, value):
        # print(product_id, type, value)
        await self.IRecord.edit_record(product_id, type, value)
        return RedirectResponse(url="/cart", status_code=303)

    async def summit_record(self):
        info = await self.IRecord.get_save_record()
        for i in info:
            # print(i[5], i[6], type(i[5]))
            self.IStock.decrease_product(i[0], i[6])
        await self.IRecord.set_record_temp()
        self.IRecord.all = []
        # You can handle the deletion logic here as needed
        return None

# To use the SalesRouter class, you would initialize it and include its router in your FastAPI app
# Example:
# app = FastAPI()
# sales_router = SalesRouter()
# app.include_router(sales_router.router)