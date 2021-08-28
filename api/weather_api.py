from fastapi import APIRouter, Depends, Response
from typing import Optional, List

from models.location import Location
from models.reports import Report, ReportSubmittal
from models.validation_error import ValidationError
from services import openweather_service, report_service

router = APIRouter()


# /api/weather/portland?state=OR&country=US&units=imperial
@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        print(f"Server crashed while processing request: {x}")
        return Response(content="Error processing your request.", status_code=500)


# name controls what shows up in swagger(openapi)
@router.get('/api/reports', name='all_reports', response_model=List[Report])
async def reports_get() -> List[Report]:
    return await report_service.get_reports()


@router.post('/api/reports', name='add_reports', status_code=201, response_model=Report)
async def reports_get(report: ReportSubmittal) -> Report:
    return await report_service.add_report(report.description, report.location)
