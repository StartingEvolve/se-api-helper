from fastapi import FastAPI
from helpers import FirebaseHasher
from pydantic import BaseModel

class HashPassword(BaseModel):
    password: str
    salt: str


app = FastAPI()


@app.post("/hash-password")
async def hash_password(hash: HashPassword):
    return {"password_hash": str(FirebaseHasher.hash_password(hash.password,hash.salt)) }