import requests
import os
from django.shortcuts import render, redirect
from django.contrib import messages
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
open_weather_token = os.environ.get('OPEN_WEATHER_TOKEN', '')


def main_page(request):
    return render(request, 'weather/main_page.html', {})


def get_weather(request):
    data = None
    location: str = request.GET.get('search')

    if 'weather_now' in request.GET:
        try:
            r = requests.get(f'https://api.m3o.com/v1/weather/Now',
                             headers={'Content-Type': 'application/json',
                                      'Authorization': f'Bearer {open_weather_token}'},
                             params={'location': location
                                     })
            data = r.json()
            return render(request, 'weather/weather_now.html', {'country': data['country'],
                                                                'city': data['location'],
                                                                'local_time': data['local_time'],
                                                                'current_temp_c': data['temp_c'],
                                                                'feels_like_temp_c': data['feels_like_c'],
                                                                'humidity': data['humidity'],
                                                                'wind_kph': data['wind_kph'],
                                                                'wind_direction': data['wind_direction'],
                                                                'icon_url': data['icon_url'],
                                                                })

        except Exception as ex:
            print(f'Ошибка при обработки запроса {ex}')
        messages.error(request, 'Данного города не существует или вы ввели что то неправильно')
        return redirect('main_page')

    elif 'weather_forecast' in request.GET:
        params = ('date', 'avg_temp_c', 'chance_of_rain', 'max_wind_kph', 'sunrise', 'sunset', 'icon_url')
        context = {}
        list_of_forecast = []

        try:
            r = requests.get(f'https://api.m3o.com/v1/weather/Forecast',
                             headers={'Content-Type': 'application/json',
                                      'Authorization': f'Bearer {open_weather_token}'},
                             params={'location': location,
                                     'days': 10
                                     })
            data = r.json()
            context.update({'country': data['country'], 'city': data['location']})

            for daily_data in data['forecast']:
                params_dict = {}
                for param in params:
                    params_dict[param] = daily_data[param]
                list_of_forecast.append(params_dict)
            context['forecast'] = list_of_forecast

            return render(request, 'weather/weather_forecast.html', context)

        except Exception as ex:
            print(f'Ошибка при обработки запроса {ex}')
        messages.error(request, 'Данного города не существует или вы ввели что то неправильно')
        return redirect('main_page')
