from db.models import Transaction, Card
from db import get_db


# Создадим перевод
def create_transaction_db(card_from, card_to, amount):
    with next(get_db()) as db:
        card_from = db.query(Card).filter_by(card_number=card_from)
        card_to = db.query(Card).filter_by(card_number=card_to)
        if card_from and card_to:
            if card_from.card_balance >= amount:
                transfer = Transaction(card_from=card_from,
                                       amount=amount,
                                       card_to=card_to)
                card_from.card_balance -= amount
                card_to.card_balance += amount
                db.add(transfer)
                db.commit()
                return True
            return "Недостаточно средств"
        return False


# Получить все переводы по карте
def get_card_transfer_db(card_number):
    with next(get_db()) as db:
        card_transfer = db.query(Transaction).filter_by(card_from=card_number).all()
        return card_transfer


# Отменить перевод
def cancel_transfer_db(transfer_id):
    with next(get_db()) as db:
        exact_transfer = db.query(Transaction).filter_by(id=transfer_id).first()
        if exact_transfer:
            db.delete(exact_transfer)
            db.commit()
            return True
        return False



