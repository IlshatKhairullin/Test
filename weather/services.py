import requests
import os
from dataclasses import asdict
from django.http import HttpRequest

from weather.enums import Weather
from weather.dataclasses import WeatherNow, WeatherForecast


def process_weather_now(location: str) -> dict:
    """Возвращает данные о погоде на данный момент"""
    try:
        r = requests.get(
            f'{os.environ.get("OPEN_WEATHER_API_NOW")}',
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {os.environ.get("OPEN_WEATHER_TOKEN")}',
            },
            params={"location": location},
        )
    except Exception as ex:
        print(f"Ошибка при запросе на api {ex}")

    return r.json()


def process_weather_forecast(location: str) -> dict:
    """Возвращает прогноз погоды на 10 дней вперед"""
    try:
        r = requests.get(
            f'{os.environ.get("OPEN_WEATHER_API_FORECAST")}',
            headers={
                "Content-Type": "application/json",
                "Authorization": f'Bearer {os.environ.get("OPEN_WEATHER_TOKEN")}',
            },
            params={"location": location, "days": 10},
        )
    except Exception as ex:
        print(f"Ошибка при запросе на api {ex}")

    return r.json()


def fetch_weather_data(request: HttpRequest, weather_choice: Weather) -> dict:
    """В зависимости от ручки парсит данные из словаря, заполняет датакласс и возвращает контекст"""
    context = {}
    location = request.GET.get("search")

    if weather_choice == Weather.Now:
        data: dict = process_weather_now(location=location)
        weather_now_dataclass = WeatherNow()
        weather_now_dataclass.fill_data(data=data)
        context.update(asdict(weather_now_dataclass))

    elif weather_choice == Weather.Forecast:
        data: dict = process_weather_forecast(location=location)
        weather_forecast_dataclass = WeatherForecast()
        weather_forecast_dataclass.fill_data(data=data)
        context.update(asdict(weather_forecast_dataclass))
    return context
