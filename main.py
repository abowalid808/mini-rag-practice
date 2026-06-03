from fastapi import FastAPI
app = FastAPI()
print("Hello, World! hi")
@app.get("/")
def welcome():
    return{"message": "Hello, World!"}

@app.get("/welcome/{name}")
def welcome_name(name: str):
    return {"message": f"Welcome, {name}!"}
# new comment