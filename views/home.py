from fastapi import APIRouter, responses
from starlette.requests import Request
from starlette.templating import Jinja2Templates

# includes the in-built templating engine for FastApi
templates = Jinja2Templates('templates')
router = APIRouter()


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse("home/index.html", {'request': request})


# explicitly get favicon from static directory because request failed
@router.get('/favicon.ico')
def favicon():
    return responses.RedirectResponse(url='/static/img/favicon.ico')