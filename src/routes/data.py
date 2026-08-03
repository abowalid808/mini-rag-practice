from fastapi import FastAPI,APIRouter,UploadFile,File 
from src.helper.config import get_settings, Setting
from src.controllers import DataController
from src.models import ResponceSignal
from src.controllers import ProjectController
import aiofiles
import logging

logger = logging.getLogger('uvicorn.error')
data_router=APIRouter(
    prefix="/data",
)

@data_router.post("/upload/{file_id}")
async def upload_file(file_id: str, file: UploadFile = File(...), app_settings: Setting = get_settings()):

    # validate the file extension and size
    is_valid, message = DataController().validate_file(file)

    # if is_valid:
    #     return {
    #         "file_id": file_id,
    #         "message": ResponceSignal.file_uploaded_sucsses.value,
    #     }
    # else:
    #     return {
    #         "file_id": file_id,
    #         "message": ResponceSignal.file_upload_failed.value,
    #     }

    # take the path to keep file in the assets folder
    project_path = ProjectController().get_project_path(file_id)

    try:
        async with aiofiles.open(project_path, 'wb') as f:
            while chunk := await file.read(app_settings.file_chunk_size):  # Read the file in chunks
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")

        return {
            "file_id": file_id,
            "message": ResponceSignal.file_upload_failed.value,
        }
    
    return {
        "file_id": file_id,
        "message": ResponceSignal.file_upload_failed.value,
    }