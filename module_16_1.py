# Основы Fast Api и маршрутизация
# uvicorn module_16_1:app --reload

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user_id(user_id: int = 123) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
async def user_stats(username: str, age: int) -> dict:
    return {"massage": f"Информация о пользователе.", "Имя": {username}, "Возраст": {age}}

