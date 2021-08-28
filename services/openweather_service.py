from typing import Optional


def get_report(city, state: Optional[str], country: str, units: str) -> dict:
    q = f'{city},{country}'
    key = 123
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&units={units}&appid={key}"

