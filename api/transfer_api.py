from fastapi import APIRouter
from db.transactionservice import (cancel_transfer_db,
                                   create_transaction_db,
                                   get_card_transfer_db)
from pydantic import BaseModel

transfer_router = APIRouter(prefix="/transfer", tags=["Transfer"])


class NewTransfer(BaseModel):
    card_from: int
    card_to: int
    amount: float


@transfer_router.post("/create_transfer")
async def create_transfer_api(transfer_model: NewTransfer):
    transfer_data = dict(transfer_model)
    new_transfer = create_transaction_db(**transfer_data)
    if new_transfer:
        return {"status": 1,
                "message": new_transfer}
    return False


@transfer_router.delete("/cancel_transfer")
async def cancel_transfer_api(transfer_id: int):
    delete_transfer = cancel_transfer_db(transfer_id)
    if delete_transfer:
        return {"status": 1,
                "message": "Перевод отменен"}
    return False


@transfer_router.get("/get_transfer_card")
async def get_transfer_card_api(card_number: int):
    get_transfer_card = get_card_transfer_db(card_number)
    if get_transfer_card:
        return {"status": 1,
                "message": get_transfer_card}
    return False
