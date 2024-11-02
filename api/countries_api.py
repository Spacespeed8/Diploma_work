from db.countries_service import (get_country_id,add_country,
                                  checker_country_info,delete_exact_country)
from fastapi import APIRouter


country_router=APIRouter(prefix="/country", tags=["/Страны"])


@country_router.post("/Добавить карту")
async def add_country(countries_with_bonus,
                      which_country,
                      country_id):
    return add_country(countries_with_bonus,
                       which_country,
                       country_id)


@country_router.delete("/Удалить карту")
async def delete_exact_country(country_id,which_country):
    return delete_exact_country(country_id,
                                    which_country)


@country_router.get("/Получть")
async def get_country_id(country_id):
    return  get_country_id(country_id)

@country_router.put("/Проверить")
async def  checker_country_info(country_id,
                                which_country,
                                countries_with_bonus):
    return  checker_country_info(country_id,
                                 which_country,
                                 countries_with_bonus)


