import os
import random
import re
import string
from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile, File 


class DataController(BaseController):

    def __init__(self):
        super().__init__()

    def validate_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.file_allowed_extensions:
            return False, ValueError(f"File type {file.content_type} is not allowed.")

        if hasattr(file, "size") and file.size > self.app_settings.file_allowed_size:
            return False, ValueError(f"File size exceeds the allowed limit of {self.app_settings.file_allowed_size} bytes.")

        return True, "file Uploaded successfully."

    def generate_random_string(self, length: int = 8) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def get_clean_file_name(self, orig_file_name: str) -> str:
        clean_name = re.sub(r'[^A-Za-z0-9_.-]', '_', orig_file_name)
        clean_name = re.sub(r'[_\- ]{2,}', '_', clean_name).strip(' _-.')
        return clean_name or 'uploaded_file'

    def generate_unique_filepath(self, orig_file_name: str, project_id: str):
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_file_name = self.get_clean_file_name(orig_file_name=orig_file_name)
        new_file_path = os.path.join(project_path, f"{random_key}_{cleaned_file_name}")

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(project_path, f"{random_key}_{cleaned_file_name}")

        return new_file_path, f"{random_key}_{cleaned_file_name}"
    