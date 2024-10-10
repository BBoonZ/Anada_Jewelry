from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .IRecordSales import RecordManager
from .Stock import ProductManager

class StockRouter:
    def __init__(self):
        self.router = APIRouter()
        self.IRecord = RecordManager()
        self.IStock = ProductManager()
        BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Navigate up three levels to the project root
        self.templates = Jinja2Templates(directory=str(BASE_DIR / "website" / "templates"))

        # Define routes
        self.router.add_api_route("/stock/", self.stock_home, methods=["GET"], response_class=HTMLResponse)

    async def stock_home(self, request: Request):
        info = self.IStock.get_all()
        return self.templates.TemplateResponse("stock.html", {"request": request, "All": info})

# To use the SalesRouter class, you would initialize it and include its router in your FastAPI app
# Example:
# app = FastAPI()
# sales_router = SalesRouter()
# app.include_router(sales_router.router)