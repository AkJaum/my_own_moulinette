from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.unzip import unzip_file
from app.runner import run_all_tests

app = FastAPI()

UPLOAD_DIR = "tmp"

@app.post("/wowlinette")
async def wowlinette(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    zip_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(zip_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    unzip_file(zip_path, UPLOAD_DIR)

    results = run_all_tests(UPLOAD_DIR)

    return results
