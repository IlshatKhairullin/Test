import requests
import os
from django.shortcuts import render
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
open_weather_token = os.environ.get('OPEN_WEATHER_TOKEN', '')


def main_page(request):
    return render(request, 'weather/main_page.html', {})


def weather_now(request):
    pass


def weather_forecast(request):
    pass
