from django.urls import path

from weather.views import main_page, get_weather

urlpatterns = [
    path("", main_page, name='main_page'),
    path("check/", get_weather, name='get_weather'),
]
