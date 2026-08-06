import os
from src.controllers import ProcessController
from fastapi import FastAPI,APIRouter,UploadFile,File 
from src.helper.config import get_settings, Setting
from src.controllers import DataController
from src.models import ResponceSignal
from src.controllers import ProjectController
import aiofiles
import logging

from src.routes.schemes import ProcessRequest

logger = logging.getLogger('uvicorn.error')
data_router=APIRouter(
    prefix="/data",
)

@data_router.post("/upload/{file_id}")
async def upload_file(file_id: str, file: UploadFile = File(...), app_settings: Setting = get_settings()):
    data_controller = DataController()

    # validate the file extension and size
    is_valid, message = data_controller.validate_file(file)
    if not is_valid:
        return {
            "file_id": file_id,
            "message": ResponceSignal.file_upload_failed.value,
        }

    file_path, saved_file_name = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=file_id,
    )

    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.file_chunk_size):  # Read the file in chunks
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file: {e}")

        return {
            "file_id": file_id,
            "message": ResponceSignal.file_upload_failed.value,
        }
    
    return {
        "file_id": saved_file_name,
        "message": ResponceSignal.file_uploaded_sucsses.value,
    }
@data_router.post("/process/{project_id}")
async def process_file(project_id: str, process_request: ProcessRequest, app_settings: Setting = get_settings()):
    file_id = process_request.file_id

    process_controller = ProcessController(project_id=project_id)
    file_content = process_controller.get_file_content(file_name=file_id)
    chunks = process_controller.split_content_into_chunks(content=file_content)

    return chunks