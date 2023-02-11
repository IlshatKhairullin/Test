import requests
import os
from dataclasses import asdict
from django.http import HttpRequest
from datetime import datetime

from weather.enums import Weather
from weather.dataclasses import WeatherNow, WeatherForecast


def send_request_weather_api(location: str, forecast: bool = False) -> dict:
    """Посылает запрос на апи, и возвращает прогноз или погоду на данных момент в зависимости от forecast=True/False"""
    response = requests.get(
        f"{os.environ.get('OPEN_WEATHER_API_FORECAST') if forecast else os.environ.get('OPEN_WEATHER_API_NOW')}",
        headers={
            "Content-Type": "application/json",
            "Authorization": f'Bearer {os.environ.get("OPEN_WEATHER_TOKEN")}',
        },
        params={"location": location, "days": {10 if forecast else 1}},
    )
    if not response.ok:
        print(f"Date - {datetime.now()}", f'Response - {response.json()}', sep='\n')
        print()
    return response.json()


def fetch_weather_data(request: HttpRequest, weather_choice: Weather) -> dict:
    """В зависимости от ручки парсит данные из словаря, заполняет датакласс и возвращает контекст"""
    context = {}
    location = request.GET.get("search")

    if weather_choice == Weather.Now:
        data: dict = send_request_weather_api(location=location, forecast=False)
        weather_now_dataclass = WeatherNow()
        weather_now_dataclass.fill_data(data=data)
        context.update(asdict(weather_now_dataclass))

    elif weather_choice == Weather.Forecast:
        data: dict = send_request_weather_api(location=location, forecast=True)
        weather_forecast_dataclass = WeatherForecast()
        weather_forecast_dataclass.fill_data(data=data)
        context.update(asdict(weather_forecast_dataclass))
    return context
