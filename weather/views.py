from django.shortcuts import render, redirect
from django.contrib import messages

from weather.enums import Weather
from weather.services import fetch_weather_data


def main_page(request):
    return render(request, "weather/main_page.html", {})


def weather_now(request):
    context = fetch_weather_data(request, Weather.Now)

    if not all(context.values()):
        messages.error(
            request, "Данного города не существует или вы ввели что то неправильно"
        )
        return redirect("main_page")
    return render(request, "weather/weather_now.html", context)


def weather_forecast(request):
    context = fetch_weather_data(request, Weather.Forecast)

    if not all(context.values()):
        messages.error(
            request, "Данного города не существует или вы ввели что то неправильно"
        )
        return redirect("main_page")
    return render(request, "weather/weather_forecast.html", context)
