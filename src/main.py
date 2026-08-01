from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")
from src.routes import base

app = FastAPI() 
app.include_router(base.router1)
app.include_router(base.router2)

print("Server is running...")
print("API documentation available at http://localhost:8000/docs")
