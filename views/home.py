from fastapi import APIRouter, responses
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from services import report_service

# includes the in-built templating engine for FastApi
templates = Jinja2Templates('templates')
router = APIRouter()


@router.get('/', include_in_schema=False)
async def index(request: Request):
    events = await report_service.get_reports()
    data = {'request': request, 'events': events}
    return templates.TemplateResponse("home/index.html", data)


# explicitly get favicon from static directory because request failed
@router.get('/favicon.ico', include_in_schema=False)
def favicon():
    return responses.RedirectResponse(url='/static/img/favicon.ico')