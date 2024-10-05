from pathlib import Path
from fastapi.templating import Jinja2Templates

# หา root directory ของโปรเจกต์
def project_root():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    return BASE_DIR
print(project_root)