# Основы Fast Api и маршрутизация \ CRUD Запросы: Get, Post, Put Delete. \ Модели данных Pydantic
# uvicorn module_16_4:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


users = {}
users_id = 0
# default_user = User(id=1, username="Example", age=18)
# users[str(default_user.id)] = default_user


@app.get("/users")
async def get_user() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int) -> str:
    global users_id
    users_id += 1
    user = User(id=users_id, username=username, age=age)
    users[users_id] = user
    return f"User {users_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: str, age: int) -> str:
    try:
        if user_id in users.keys():
            user = users[user_id]
            user.username = username
            user.age = age
            return f"The user {user_id} is updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id)
        return f"User {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

