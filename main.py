#Python
from datetime import date
from typing import Optional
from uuid import UUID

#Pydantic
from pydantic import BaseModel, EmailStr, Field
#Fastapi 
from fastapi import FastAPI


app=FastAPI()

#Models
class Userbase(BaseModel):
    user_id:UUID = Field(...) 
    email:EmailStr = Field(...)
    
    
class UserLogin(Userbase):
    password:str=Field(
            ...,
            min_lenght=8
        )
class User(Userbase):
    first_name: str=Field(
        ...,
        min_lenght=1,
        max_length=50,
        example="Ian")
    last_name: str=Field(
        ...,
        min_lenght=1,
        max_lenght=50,
        example="Vaz"
    )
    birth_date:Optional[date] =Field(default=None)
    
    
class Tweet(BaseModel):
    pass

@app.get(path="/")
def home():
    return {"Twitter API ":"Working"}