from fastapi import FastAPI
from api.card_api import card_router
from api.corporative_clients_api import corporative_clients_router
from api.countries_api import country_router
from api.transfer_api import transfer_router
from api.user_api import user_router
from db import Base, engine


app = FastAPI(docs_url="/")
Base.metadata.create_all(engine)

app.include_router(card_router)
app.include_router(transfer_router)
app.include_router(user_router)
app.include_router(corporative_clients_router)
app.include_router(country_router)
