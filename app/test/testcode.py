from pathlib import Path
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Navigate up three levels to the project root
templates = Jinja2Templates(directory=str(BASE_DIR / "website" / "templates"))

print(BASE_DIR)
print(templates)