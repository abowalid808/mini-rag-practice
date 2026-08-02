from src.helper.config import get_settings, Setting

class BaseController:
    """Base controller class for common functionality."""
    def __init__(self, app_settings: Setting = get_settings()):
        self.app_settings = app_settings