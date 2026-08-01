from fastapi import FastAPI,APIRouter 
import os

router2=APIRouter()

@router2.get("app_prob")
def app_prob():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "app_name": app_name,
        "app_version": app_version
    }