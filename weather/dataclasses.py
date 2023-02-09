from dataclasses import dataclass


@dataclass
class WeatherNow:
    """Датакласс для хранения информации о погоде на данный момент"""

    country: str
    city: str
    local_time: str
    current_temp_c: int
    feels_like_temp_c: int
    humidity: int
    wind_kph: float
    wind_direction: str
    icon_url: str


@dataclass
class WeatherForecast:
    """Датакласс для хранения информации о прогнозе погоды на 10 дней"""

    country: str
    city: str
    forecast: list
