# Основы Fast Api и маршрутизация \ CRUD Запросы: Get, Post, Put Delete. \ Модели данных Pydantic
# uvicorn module_16_4:app --reload

from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field, ValidationError
from typing import Annotated

app = FastAPI()


class User(BaseModel):
    id: int
    username: str = Field(min_length=3, max_length=30)
    age: int = Field(ge=0, le=150)


users = {}
users_id = 0


@app.get("/users", response_model=dict[int, User])
async def get_users() -> dict[int, User]:
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                                   description="Enter username", example="UrbanUser")],
                     age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> User:
    try:
        global users_id
        users_id += 1
        user = User(id=users_id, username=username, age=age)
        users[users_id] = user
        return f"User {users_id} is registered"
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())



@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def put_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=10)],
                   username: Annotated[str, Path(min_length=5, max_length=20,
                                                 description="Enter username", example="UrbanUser")],
                   age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]):
    try:
        if user_id in users.keys():
            user = users[user_id]
            user.username = username
            user.age = age
            return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=10)]):
    try:
        users.pop(user_id)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

