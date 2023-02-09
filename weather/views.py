from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages

from weather.enums import Weather
from weather.services import fetch_weather_data


# основная страница с поиском
def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, "weather/main_page.html", {})


# возвращает страницу с погодой на данный момент, если город введен неправильно, то вернет ошибку об этом
def weather_now(request: HttpRequest) -> HttpResponse:
    context = fetch_weather_data(request, Weather.Now)

    if not all(context.values()):
        messages.error(
            request, "Данного города не существует или вы ввели что то неправильно"
        )
        return redirect("main_page")
    return render(request, "weather/weather_now.html", context)


# возвращает страницу с прогнозом погоды на 10 дней, если город введен неправильно, то вернет ошибку об этом
def weather_forecast(request: HttpRequest) -> HttpResponse:
    context = fetch_weather_data(request, Weather.Forecast)

    if not all(context.values()):
        messages.error(
            request, "Данного города не существует или вы ввели что то неправильно"
        )
        return redirect("main_page")
    return render(request, "weather/weather_forecast.html", context)
