from fastapi import APIRouter, FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import os
import shutil
from typing import List


class UploadRoute:
    def __init__(self):
        self.router = APIRouter()
        self.upload_dir = "app/img/"

        # Define routes
        self.router.add_api_route("/uploadfile", self.upload_file, methods=["POST"])

    async def upload_file(self, file: UploadFile = File()):
        # Check if the uploaded file is a valid PNG or JPG
        if file.content_type not in ["image/png", "image/jpeg"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Only PNG or JPG files are allowed.")

        # Ensure the upload directory exists
        if not os.path.exists(self.upload_dir):
            os.makedirs(self.upload_dir)

        # Define the file path to save the uploaded file
        file_path = os.path.join(self.upload_dir, file.filename)

        # Save the file to the upload directory
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"filename": file.filename, "file_path": file_path}