import json
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from pathlib import Path
from api import weather_api
from services import openweather_service
from views import home

# docs_url=None if docs not needed
app = FastAPI()


def configure():
    configure_routing()
    configure_apikeys()


def configure_apikeys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
        raise Exception("settings.json file not found, you cannot continue, please see settings_template.json")

    with open('settings.json') as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')


def configure_routing():
    # mount static files e.g css, images e.t.c
    app.mount('/static', StaticFiles(directory='static'), name='static')

    # includes modular routes
    app.include_router(weather_api.router)
    app.include_router(home.router)


configure()
