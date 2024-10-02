import os

# กำหนด path ของไฟล์
file_path = "app/file.txt"

# หา root directory ของโปรเจกต์
def project_root():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(file_path)))
    print(f"Project root: {project_root}")
    return project_root

project_root()