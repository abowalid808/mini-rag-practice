from src.helper.config import get_settings, Setting
import os

class BaseController:
    """Base controller class for common functionality."""
    def __init__(self, app_settings: Setting = get_settings()):
        self.app_settings = app_settings
        # return the path of the src folder
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        # return the path of the assets folder
        self.files_path = os.path.join(self.base_path, "assets/files")