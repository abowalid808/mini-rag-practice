from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")
from src.routes import base
from src.routes import data


app = FastAPI() 
app.include_router(base.router2)
app.include_router(data.data_router)
