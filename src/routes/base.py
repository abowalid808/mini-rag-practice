from fastapi import FastAPI,APIRouter 
from src.helper.config import get_settings, Setting
import os

app_settings = get_settings()

router2=APIRouter(
    prefix="/system/config", 
)


@router2.get("/app_prob")
def app_prob():
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return{
        "app_name": app_name,
        "app_version": app_version
    }