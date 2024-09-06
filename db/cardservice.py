from db.models import Card
from db import get_db


# Добавление карты в бд
def add_card_db(user_id, card_number, cvv,
                exp_date, card_name, balance):
    with next(get_db()) as db:
        new_card = Card(user_id=user_id, card_number=card_number,
                        cvv=cvv, card_balance=balance, exp_date=exp_date,
                        card_name=card_name)
        db.add(new_card)
        db.commit()
        return True


# Удаление карты
def delete_exact_card_db(card_number):
    with next(get_db()) as db:
        delete_card = db.query(Card).filter_by(card_number=card_number).first()
        if delete_card:
            db.delete(delete_card)
            db.commit()
            return True
        return False


# Получение карты пользователя
def get_user_card_db(user_id):
    with next(get_db()) as db:
        user_card = db.query(Card).filter_by(user_id=user_id).first()
        if user_card:
            return user_card
        return False


# Получение определенной карты
def get_exact_card_db(card_number):
    with next(get_db()) as db:
        exact_card = db.query(Card).filter_by(card_number=card_number).first()
        if exact_card:
            return exact_card
        return False


# Проверка карты
def checker_card_info_db(card_number, card_name):
    with next(get_db()) as db:
        checker = db.query(Card).filter_by(card_number=card_number, card_name=card_name).first()
        if checker:
            return True
        return False

