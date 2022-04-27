#Python
import json
from datetime import date, datetime
from typing import Optional,List
from uuid import UUID

#Pydantic
from pydantic import BaseModel, EmailStr, Field
#Fastapi 
from fastapi import Body, FastAPI,status


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
        
class UserRegister(UserLogin,User):
    pass

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

## Users
###Register User

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signUp(user: UserRegister= Body(...)):
    """Signup
    This Path operation register an user in the app

    Parameters : 
        - Request Body parameter
        - user : UserRegister
    
    returns a json with the basic information
        -user_id : UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date

    """    
    
    with open("users.json","r+",encoding="UTF-8")  as f:
        results=json.loads(f.read())
        user_dict= user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"]=str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


###Login User

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

###Show all Users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show al Users",
    tags=["Users"]
)
def show_all_users():
    """Show all User
        
        This path operation shows all uers in the app
        Parameters:

            -
        returns  a json list with all users in the app with the following Keys
        -user_id : UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date


    """    
    with open("users.json","r",encoding="UTF-8") as f:
        results= json.loads(f.read())
        return results

###Show a single User
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Register a User",
    tags=["Users"]
)
def show_a_user():
    pass
###Delete a User
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user():
    pass
###Update a User
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
###Show all Tweets

@app.get(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweet"]
    )
def home():
    return {"Twitter API ":"Working"}

###Post a Tweet

@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweet"]
)
def post():
        """Signup
    This Path operation register an user in the app

    Parameters : 
        - Request Body parameter
        - user : UserRegister
    
    returns a json with the basic information
        -user_id : UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date

    """    
    with open("users.json","r+",encoding="UTF-8")  as f:
        results=json.loads(f.read())
        user_dict= user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"]=str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user

###Show a Tweet

@app.get(
    path="/tweets/{tweet_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Tweet"]
)
def show_a_tweet():
    pass

###Delete a Tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweet"]
)
def delete_a_tweet():
    pass

###Update a Tweet

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweet"]
)
def update_a_tweet():
    pass

