#Python
from datetime import date, datetime
from typing import Optional,List
from uuid import UUID

#Pydantic
from pydantic import BaseModel, EmailStr, Field
#Fastapi 
from fastapi import FastAPI,status


app=FastAPI()

#Models
class Userbase(BaseModel):
    user_id:UUID = Field(...) 
    email:EmailStr = Field(...)
    
    
class UserLogin(Userbase):
    password:str=Field(
            ...,
            min_lenght=8,
            max_lenght=64

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
    tweet_id: UUID = Field(...)
    content:str= Field(
        ...,
        min_length=1,
        max_length=256)
    created_at:datetime= Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field (...)


# Path Operations

@app.get(path="/")
def home():
    return {"Twitter API ":"Working"}


## Users
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signUp():
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show al Users",
    tags=["Users"]
)
def show_all_users():
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Register a User",
    tags=["Users"]
)
def show_a_user():
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user():
    pass



## Tweets