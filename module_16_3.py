# Основы Fast Api и маршрутизация \ CRUD Запросы: Get, Post, Put Delete.
# uvicorn module_16_2:app --reload

from fastapi import FastAPI

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/user")
async def get_user() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int) -> str:
    user_id = str(int(max(users, key=str))+1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_user(user_id: int, username: str, age: int) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    removed_user = users.pop(str(user_id), None)  # Удалить без ошибки, если ключ отсутствует
    if removed_user is None:
        return f"User {user_id} does not exist"
    return f"The user {user_id} is deleted"

