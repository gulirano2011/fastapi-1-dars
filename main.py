from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="My application",
    description="Bu Hello world web appi",
    version="1.0.0"
)

class User(BaseModel):
    name:str
    age:int

@app.get("/")
def home():
    """BU asosiy sahifa funksiyasi"""
    return {"message":"Hello world!"}

@app.get('/users/{name}')
async def get_user(name: str):
    return {"message": f"{name}"}

@app.post("/users")
async def create_user(user:User):
    """Bu funksiya userlarni yaratadi"""
    return {
        "message":"User yaratildi!",
        "data":user
    }

