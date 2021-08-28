from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from api import weather_api
from views import home

app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    # mount static files e.g css, images e.t.c
    app.mount('/static', StaticFiles(directory='static'), name='static')

    # includes modular routes
    app.include_router(weather_api.router)
    app.include_router(home.router)


configure()