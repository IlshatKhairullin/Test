from dataclasses import dataclass, field


@dataclass
class WeatherNow:
    """Датакласс для хранения информации о погоде на данный момент"""

    country: str = field(init=False)
    city: str = field(init=False)
    local_time: str = field(init=False)
    current_temp_c: int = field(init=False)
    feels_like_temp_c: int = field(init=False)
    humidity: int = field(init=False)
    wind_kph: float = field(init=False)
    wind_direction: str = field(init=False)
    icon_url: str = field(init=False)

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


@dataclass
class WeatherForecast:
    """Датакласс для хранения информации о прогнозе погоды на 10 дней"""

    country: str = field(init=False)
    city: str = field(init=False)
    forecast: list = field(init=False)

    def fill_data(self, data: dict) -> None:
        self.country = data.get("country")
        self.city = data.get("location")
        self.forecast = data.get("forecast")
