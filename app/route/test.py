from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@router.post("/items/")
async def create_item(item: dict):
    return {"item": item}

@router.get("/html", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>FastAPI HTML Response</title>
        </head>
        <body>
            <h1>Hello, FastAPI!</h1>
            <p>This is an example of returning HTML.</p>
        </body>
    </html>
    """