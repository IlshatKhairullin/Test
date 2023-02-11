from dataclasses import dataclass, field


@dataclass(init=False)
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

    def fill_data(self, data: dict) -> None:
        self.country = data.get("country")
        self.city = data.get("location")
        self.local_time = data.get("local_time")
        self.current_temp_c = data.get("temp_c")
        self.feels_like_temp_c = data.get("feels_like_c")
        self.humidity = data.get("humidity")
        self.wind_kph = data.get("wind_kph")
        self.wind_direction = data.get("wind_direction")
        self.icon_url = data.get("icon_url")


@dataclass(init=False)
class WeatherForecast:
    """Датакласс для хранения информации о прогнозе погоды на 10 дней"""

    country: str
    city: str
    forecast: list

    def fill_data(self, data: dict) -> None:
        self.country = data.get("country")
        self.city = data.get("location")
        self.forecast = data.get("forecast")
