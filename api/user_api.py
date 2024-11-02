from fastapi import APIRouter
from db.userservice import register_user_db, change_user_db, get_users, delete_user_db, get_exact_user_db
from pydantic import BaseModel

user_router = APIRouter(prefix="/user", tags=["Пользователи"])


@user_router.post("/Регистрация")
async def register_user(surname, name, phone_number,
                        email, password, user_city, user_photo=None):
    return register_user_db(surname, name, phone_number,
                            email, password, user_city, user_photo)


@user_router.put("/Поменять пользователя")
async def change_user(user_id, surname=None, name=None, phone_number=None, email=None, password=None,
                      user_city=None, user_photo=None):
    return change_user_db(user_id, surname, name, phone_number, email, password,
                          user_city, user_photo)


@user_router.get("/Получить пользователя")
async def get_user(user_id: int):
    result = get_exact_user_db(user_id)

    return {'message': result}


@user_router.delete("Удалить пользователя")
async def delete_user(user_id):
    delete_user_db(user_id)
    return {'message': "Пользователь удален"}
