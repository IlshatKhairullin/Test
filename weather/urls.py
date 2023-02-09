from django.urls import path

from weather.views import main_page, weather_now, weather_forecast

urlpatterns = [
    path("", main_page, name="main_page"),
    path("now/", weather_now, name="weather_now"),
    path("forecast/", weather_forecast, name="weather_forecast"),
]
