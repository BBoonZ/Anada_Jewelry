from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from pathlib import Path

router = APIRouter()


BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Navigate up three levels to the project root
templates = Jinja2Templates(directory=str(BASE_DIR / "website" / "templates"))

@router.get("/test", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse("sale_record.html", {"request": request, "title": "FastAPI Example"})






