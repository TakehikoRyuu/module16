# Основы Fast Api и маршрутизация \ CRUD Запросы: Get, Post, Put Delete. \ Модели данных Pydantic
# uvicorn module_16_5:app --reload

from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = {}
users_id = 0


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    user_list = list(users.values())
    return templates.TemplateResponse("users.html", {"request": request, "users": user_list})


@app.get("/users/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})


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

