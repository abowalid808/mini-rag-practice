from .BaseController import BaseController
from fastapi import UploadFile,File 


class DataController(BaseController):

    def __init__(self):
        super().__init__()

    def validate_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.file_allowed_extensions:
            return False, ValueError(f"File type {file.content_type} is not allowed.")

        if file.size > self.app_settings.file_allowed_size:
            return False, ValueError(f"File size exceeds the allowed limit of {self.app_settings.file_allowed_size} bytes.")

        return True, "file Uploaded successfully."
    