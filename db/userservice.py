from db import get_db
from db.models import User


def register_user_db(surname, name, phone_number, email, password, user_city, user_photo=None):
    with next(get_db()) as db:
        new_user = User(surname=surname, name=name, phone_number=phone_number, email=email,
                        password=password, user_city=user_city, user_photo=user_photo)
        db.add(new_user)
        db.commit()
        return "Успешно зарегистрировались"


def get_users():
    with next(get_db()) as db:
        all_user = db.query(User).all()
        return all_user


def get_exact_user_db(user_id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=user_id).first()
        return exact_user


def delete_user_db(user_id):
    with next(get_db()) as db:
        db.query(User).filter_by(id=user_id).delete()
        db.commit()


def change_user_db(user_id, surname=None, name=None, phone_number=None, email=None, password=None,
                   user_city=None, user_photo=None):
    with next(get_db()) as db:
        user = db.query(User).filter(User.id == user_id).first()
        if surname is not None:
            user.surname = surname
        if name is not None:
            user.name = name
        if phone_number is not None:
            user.phone_number = phone_number
        if email is not None:
            user.email = email
        if password is not None:
            user.password = password
        if user_city is not None:
            user.user_city = user_city
        if user_photo is not None:
            user.user_photo = user_photo
        db.commit()
