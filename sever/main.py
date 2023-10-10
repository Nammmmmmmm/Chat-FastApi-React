from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# pip install "uvicorn[standard]"

from pydantic import BaseModel
from typing import Union

import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_ID = "793b92e1-f319-44ca-a42c-1743c8a78840"
PRIVATE_KEY = "b2d43fb8-7150-4a4e-a61c-091534912a08"

class User(BaseModel):
    username: str
    secret: str
    email: Union[str, None] = None
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None

@app.post('/login/')
async def root(user: User):
    response = requests.get('https://api.chatengine.io/users/me/', 
        headers={ 
            "Project-ID": PROJECT_ID,
            "User-Name": user.username,
            "User-Secret": user.secret
        }
    )
    return response.json()

@app.post('/signup/')
async def root(user: User):
    response = requests.post('https://api.chatengine.io/users/', 
        data={
            "username": user.username,
            "secret": user.secret,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
        headers={ "Private-Key": PRIVATE_KEY }
    )
    return response.json()

# python3 -m venv venv
# source venv/bin/activate
# pip install --upgrade pip
# pip install -r requirements.txt
# uvicorn main:app --reload --port 3001