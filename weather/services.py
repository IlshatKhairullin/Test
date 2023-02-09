import requests
import os
from dataclasses import asdict

from weather.enums import Weather
from weather.dataclasses import WeatherNow, WeatherForecast


def process_weather_now(location: str) -> dict:
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


def fetch_weather_data(
    request: requests.models.Response, weather_choice: Weather
) -> dict:
    context = {}
    location = request.GET.get("search")

    if weather_choice == Weather.Now:
        data = process_weather_now(location=location)
        weather_now_dataclass = WeatherNow(
            country=data.get("country"),
            city=data.get("location"),
            local_time=data.get("local_time"),
            current_temp_c=data.get("temp_c"),
            feels_like_temp_c=data.get("feels_like_c"),
            humidity=data.get("humidity"),
            wind_kph=data.get("wind_kph"),
            wind_direction=data.get("wind_direction"),
            icon_url=data.get("icon_url"),
        )
        context.update(asdict(weather_now_dataclass))

    elif weather_choice == Weather.Forecast:
        data = process_weather_forecast(location=location)
        weather_forecast_dataclass = WeatherForecast(
            country=data.get("country"),
            city=data.get("location"),
            forecast=data.get("forecast"),
        )
        context.update(asdict(weather_forecast_dataclass))
    return context
