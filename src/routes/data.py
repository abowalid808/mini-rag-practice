from fastapi import FastAPI,APIRouter,UploadFile,File 
from src.helper.config import get_settings, Setting
from DataController import DataController

data_router=APIRouter(
    prefix="/data",
)

@data_router.post("/upload/{file_id}")
async def upload_file(file_id: str, file: UploadFile = File(...), app_settings: Setting = get_settings()):

    # validate the file extension and size
    is_valid, message = DataController().validate_file(file)

    return {
        "file_id": file_id,
        "message": message
    }