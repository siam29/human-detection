from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import os
from model import detect_humans

app = FastAPI()

os.makedirs("uploaded_images", exist_ok=True)

@app.post("/detect/")
async def detect_human(file: UploadFile = File(...)):
    file_location = f"uploaded_images/{file.filename}"
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    output_image, _ = detect_humans(file_location)
    return FileResponse(output_image)
