import requests
import os
from dotenv import load_dotenv, find_dotenv
from weather.enums import Weather

load_dotenv(find_dotenv())


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
        context.update(
            {
                "country": data.get("country"),
                "city": data.get("location"),
                "local_time": data.get("local_time"),
                "current_temp_c": data.get("temp_c"),
                "feels_like_temp_c": data.get("feels_like_c"),
                "humidity": data.get("humidity"),
                "wind_kph": data.get("wind_kph"),
                "wind_direction": data.get("wind_direction"),
                "icon_url": data.get("icon_url"),
            }
        )

    elif weather_choice == Weather.Forecast:
        data = process_weather_forecast(location=location)
        context.update({"country": data.get("country"), "city": data.get("location")})
        context["forecast"] = data.get("forecast")
    return context
