from dataclasses import dataclass


# датакласс для хранения информации о погоде на данный момент
@dataclass
class WeatherNow:
    country: str
    city: str
    local_time: str
    current_temp_c: int
    feels_like_temp_c: int
    humidity: int
    wind_kph: float
    wind_direction: str
    icon_url: str


# датакласс для хранения информации о прогнозе погоды на 10 дней
@dataclass
class WeatherForecast:
    country: str
    city: str
    forecast: list
