# from fastapi import FastAPI
# from api.card_api import card_router
# from api.client_orders_api import corporative_clients_router
# from api.countries_api import country_router
# from api.transfer_api import transfer_router
# from api.user_api import user_router
# from db import Base, engine
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
#
# app = FastAPI()
#
# app.mount("/static", StaticFiles(directory="static"), name="static")
# Base.metadata.create_all(engine)
#
#
# app.include_router(card_router)
# app.include_router(transfer_router)
# app.include_router(user_router)
# app.include_router(corporative_clients_router)
# app.include_router(country_router)
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from api.card_api import card_router  # импортируй свои API маршруты
# Подключи остальные API маршруты аналогично

app = FastAPI()

# Настройка статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Настройка шаблонов
templates = Jinja2Templates(directory="static")

# Маршрут для index.html
@app.get("/", response_class=HTMLResponse)
async def read_index():
    return templates.TemplateResponse("index.html", {"request": {}})

# Подключение API маршрутов
app.include_router(card_router)
# Подключи остальные API маршруты тут

# Запуск приложения
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)