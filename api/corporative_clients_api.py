from fastapi import APIRouter
from db.corporative_clients_service import (add_corporative_client, checker_corporative_client,
                                            get_exact_corporative_client)

corporative_clients_router = APIRouter(prefix="/corporative_client", tags=["corporative_clients "
                                                                           "exept Russian Federation "
                                                                           "and Kazakhstan"])


@corporative_clients_router.post("/add")
async def add_corporative_client(type_of_bussiness, id, company):
    return add_corporative_client(type_of_bussiness, id, company)


@corporative_clients_router.get("/post")
async def checker_corporative_client(id, company):
    return checker_corporative_client(id, company)


@corporative_clients_router.get("/get")
async def get_exact_corporative_client(id):
    return get_exact_corporative_client(id)
