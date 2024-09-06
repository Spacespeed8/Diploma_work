from fastapi import APIRouter
from db.cardservice import (add_card_db, delete_exact_card_db,
                            get_exact_card_db, get_user_card_db, checker_card_info_db)
from pydantic import BaseModel

card_router = APIRouter(prefix="/card", tags=["Cards"])


class NewCard(BaseModel):
    user_id: int
    card_number: int
    cvv: int
    exp_date: int
    card_name: str
    balance: float


@card_router.post("/add_card")
async def add_card_api(card_model: NewCard):
    card_data = dict(card_model)
    new_card = add_card_db(**card_data)
    if new_card:
        return {'status': 1,
                'message': 'Успешно добавлено'}
    return False


@card_router.delete("/delete_card")
async def delete_card_api(card_number: int):
    delete_card = delete_exact_card_db(card_number)
    if delete_card:
        return {"status": 1,
                "message": "Успешно удалено"}
    return False


@card_router.get("/get_exact_card")
async def get_exact_card_api(card_number: int):
    exact_card = get_exact_card_db(card_number)
    if exact_card:
        return {"status": 1,
                "message": exact_card}
    return False


@card_router.get("/get_user_cards")
async def get_user_cards_api(user_id: int):
    exact_user_cards = get_user_card_db(user_id)
    if exact_user_cards:
        return {"status": 1,
                "message": exact_user_cards}
    return False


@card_router.get("/check_card")
async def check_card_api(card_number: int,
                         card_name: str):
    check_card = checker_card_info_db(card_number, card_name)
    if check_card:
        return {"status": 1,
                "message": check_card}
    return False



