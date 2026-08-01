from fastapi import FastAPI,APIRouter 
import os

router1=APIRouter(
    prefix="/courses/NLP", # This prefix will be added to all routes in this router
    tags=["NLP"]
)
router2=APIRouter()


@router1.get("/")
def welcome_1():
    return{"message": "Welcome to the NLP course"}
@router1.get("/C1")
def welcome_c1():
    return{"message": "Welcome to the NLP course 1"}

@router1.get("/C2")
def welcome_c2():
    return{"message": "Welcome to the NLP course 2"}

@router1.get("/C3")
def welcome_c3():
    return{"message": "Welcome to the NLP course 3"}

@router2.get("/app_prob")
def app_prob():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "app_name": app_name,
        "app_version": app_version
    }