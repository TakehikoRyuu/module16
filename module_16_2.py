# Основы Fast Api и маршрутизация / Валидация данных
# uvicorn module_16_1:app --reload

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/userid/{user_id}")
async def user_id(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=10)]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user-stats/{username}/{age}")
async def user_stats(username: Annotated[str, Path(min_length=5, max_length=20,
                                                   description="Enter username", example="UrbanUser")],
                     age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]) -> dict:
    return {"massage": f"Информация о пользователе.", "Имя": {username}, "Возраст": {age}}

