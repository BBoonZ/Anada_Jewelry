from fastapi import APIRouter, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .RecordSalesProxy import RecordManagerProxy
from .RecordSales  import RecordManager
from .Stock import ProductManager
from .CreateProduct import ICreateProduct
from .IDeleteProduct import DeleteProduct
from .UploadFile import UploadRoute

class StockRouter:
    def __init__(self):
        self.router = APIRouter()
        self.IRecord = RecordManagerProxy(RecordManager())
        self.IStock = ProductManager()
        self.ICreate = ICreateProduct()
        self.IDelete = DeleteProduct()
        self.Upload = UploadRoute()
        BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Navigate up three levels to the project root
        self.templates = Jinja2Templates(directory=str(BASE_DIR / "website" / "templates"))

        # Define routes
        self.router.add_api_route("/", self.home, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/stock/type-{type}", self.stock_home, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/stock/edit/{product_id}", self.stock_popup_edit, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/stock/create/", self.create_product, methods=["GET"], response_class=HTMLResponse)
        self.router.add_api_route("/stock/create/submit", self.summit_create_product, methods=["POST"])
        self.router.add_api_route("/stock/delete/{product_id}", self.delete_product, methods=["POST"])
        self.router.add_api_route("/stock/edit/{product_id}", self.summit_popup_edit, methods=["POST"])
    
    async def home(self, request: Request):
        return self.templates.TemplateResponse("home.html", {"request": request})

    async def stock_home(self, request: Request, type):
        info = self.IStock.get_all()
        if type != "none":
            info = self.IStock.get_type_product(type)
        return self.templates.TemplateResponse("stock.html", {"request": request, "All": info})

    async def stock_popup_edit(self, request: Request, product_id : int):
        info = self.IStock.get_product(product_id)
        option = info[6]
        option_dic = {
            "none" : "option0",
            "ring" : "option1",
            "earring" : "option2",
            "bracelets" : "option3",
            "bangles" : "option4",
            "necklaces" : "option5",
            "pendants" : "option6"
            }
        option = option_dic.get(option)
        return self.templates.TemplateResponse("popup_edit.html", {"request" : request, "product": info, "option": option})

    async def summit_popup_edit(self, id: str = Form(), name: str = Form(),file: UploadFile = File(), info: str = Form(), type: str = Form(), price: str = Form(), value: str = Form()):
        print(id, name, info, type, price, value)
        print(file.filename)
        # return RedirectResponse(url="/stock", status_code=303)
        # await self.Upload.upload_file(file)
        await self.IStock.setProduct(id, name, type, info, price, value, file)
        return None

    async def create_product(self, request: Request):
        return self.templates.TemplateResponse("popup_create.html", {"request": request})

    async def summit_create_product(self, name = Form(), info = Form(), product_type = Form(), file: UploadFile = File(), price = Form(), value = Form()):
        # print(file)
        if (file.filename == ""):
            print("wat")
            await self.ICreate.create_product(name, info, "main.png", value, product_type, price,)
            return None

        await self.Upload.upload_file(file)
        # # print(name, info, file.filename, value, product_type, price)
        await self.ICreate.create_product(name, info, file.filename, value, product_type, price,)
        return None

    async def delete_product(self, product_id):
        self.IDelete.DeleteProduct(product_id)
        return None

# To use the SalesRouter class, you would initialize it and include its router in your FastAPI app
# Example:
# app = FastAPI()
# sales_router = SalesRouter()
# app.include_router(sales_router.router)