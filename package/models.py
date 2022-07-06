from datetime import datetime

from .constants import Filter


class Current:

    def __init__(self, data: dict) -> None:
        # the api only returns computed data, some data may not be available
        self.coordinates = Coordinates(data["coord"] if "coord" in data else {})
        filtered_data = { _key: _value for _key, _value in data.items() if _key in Filter.WEATHER }
        self.weather = Weather(filtered_data if filtered_data else {})
        self.general = General(data if data else {})
    
    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.coordinates}, {self.weather})"


class Coordinates:

    def __init__(self, data: dict) -> None:
        self.latitude = data["lat"] if "lat" in data else None
        self.longitude = data["lon"] if "lon" in data else None

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.latitude}, {self.longitude})"


class Temperature:

    def __init__(self, data: dict) -> None:
        self.degree = data["temp"] if "temp" in data else None
        self.degree_feeling = data["feels_like"] if "feels_like" in data else None
        self.degree_min = data["temp_min"] if "temp_min" in data else None
        self.degree_max = data["temp_max"] if "temp_max" in data else None
        self.humidity = data["humidity"] if "humidity" in data else None
    
    def convert_to_celsius(self) -> float:
        """convert kelvin to celsius"""
        return round(self.degree - 273.15, 2)
    
    def convert_to_fahrenheit(self) -> float:
        """convert kelvin to fahrenheit"""
        return round(9 / 5 * (self.degree - 273.15) + 32, 2)
    
    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.degree}, {self.degree_feeling}, {self.degree_min}, {self.degree_max}, {self.humidity})"


class Pressure:

    def __init__(self, data: dict) -> None:
        self.pressure_main = data["pressure"] if "pressure" in data else None
        self.pressure_sea_level = data["sea_level"] if "sea_level" in data else None
        self.pressure_ground_level = data["grnd_level"] if "grnd_level" in data else None
    
    def convert_to_bar(self) -> float:
        """convert hectopascal to bar"""
        return self.pressure_main / 1000

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.pressure_main}, {self.pressure_sea_level}, {self.pressure_ground_level})"


class Wind:

    def __init__(self, data: dict) -> None:
        self.speed = data["speed"] if "speed" in data else None
        self.degree = data["deg"] if "deg" in data else None
        self.gust = data["gust"] if "gust" in data else None
    
    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.speed}, {self.degree}, {self.gust})"


class Clouds:

    def __init__(self, data: dict) -> None:
        self.percentage = data["all"] if "all" in data else None

    def has_clouds(self) -> bool:
        """check if cloud percentage above 0"""
        if self.percentage is None:
            return False

        return self.percentage > 0

    def is_cloudy(self) -> bool:
        """check if cloud percentage above 50"""
        if self.percentage is None:
            return False

        # a cloud percentage above 50 is considered cloudy
        return self.percentage > 50

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.percentage})"


class Rain:

    def __init__(self, data: dict) -> None:
        self.volume_one_hour = data["1h"] if "1h" in data else None
        self.volume_three_hours = data["3h"] if "3h" in data else None

    def is_raining(self) -> bool:
        """check if rain volume above 0"""
        if self.volume_one_hour is None and self.volume_three_hours is None:
            return False

        return self.volume_one_hour > 0 or self.volume_three_hours > 0

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.volume_one_hour}, {self.volume_three_hours})"


class Snow:

    def __init__(self, data: dict) -> None:
        self.volume_one_hour = data["1h"] if "1h" in data else None
        self.volume_three_hours = data["3h"] if "3h" in data else None
    
    def is_snowing(self) -> bool:
        """check if snow volume above 0"""
        if self.volume_one_hour is None and self.volume_three_hours is None:
            return False

        return self.volume_one_hour > 0 or self.volume_three_hours > 0

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.volume_one_hour}, {self.volume_three_hours})"


class Weather:

    def __init__(self, data: dict) -> None:
        if "weather" not in data:
            data["weather"] = [{}]

        self.id = data["weather"][0]["id"] if "id" in data["weather"][0] else None
        self.group = data["weather"][0]["main"] if "main" in data["weather"][0] else None
        self.description = data["weather"][0]["description"] if "description" in data["weather"][0] else None
        self.visibility = data["visibility"] if "visibility" in data else None

        self.temperature = Temperature(data["main"] if "main" in data else {})
        self.pressure = Pressure(data["main"] if "main" in data else {})
        self.wind = Wind(data["wind"] if "wind" in data else {})
        self.clouds = Clouds(data["clouds"] if "clouds" in data else {})
        self.rain = Rain(data["rain"] if "rain" in data else {})
        self.snow = Snow(data["snow"] if "snow" in data else {})
    
    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.id}, {self.group}, {self.description}, {self.visibility}, {self.temperature}, {self.pressure}, {self.wind}, {self.clouds}, {self.rain}, {self.snow})"


class City:
    
    def __init__(self, data: dict) -> None:
        self.id = data["id"] if "id" in data else None
        self.name = data["name"] if "name" in data else None
        self.country = data["sys"]["country"] if "country" in data["sys"] else None
    
    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.id}, {self.name}, {self.country})"


class General:

    def __init__(self, data: dict) -> None:
        self.base = data["base"] if "base" in data else None
        # unix utc timestamp, use timezone shift to offset to local time 
        self.timestamp = data["dt"] if "dt" in data else None
        self.timezone_shift = data["timezone"] if "timezone" in data else None
        self.sunrise = data["sys"]["sunrise"] if "sunrise" in data["sys"] else None
        self.sunset = data["sys"]["sunset"] if "sunset" in data["sys"] else None
        self.city = City(data if data else None)
    
    def convert_timestamp(self) -> datetime:
        """return converted unix timestamp"""
        return datetime.utcfromtimestamp(self.timestamp)

    def __repr__(self) -> str:
        return f"{self.__class__.__module__}.{self.__class__.__qualname__}({self.base}, {self.timestamp}, {self.timezone_shift}, {self.sunrise}, {self.sunset}, {self.city})"