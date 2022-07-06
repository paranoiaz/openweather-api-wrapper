import requests

from .constants import API, Language, Unit
from .models import Current


class CurrentWeather:

    def __init__(self, key: str) -> None:
        if key is None or key == "":
            raise Exception("No API key provided in options.")

        self.api_key = key

    def get_weather_coords(self, latitude: float, longitude: float, unit: Unit=None, language: Language=None) -> Current:
        """return the current weather data for a specific location"""
        parameters = {
            "lat": latitude,
            "lon": longitude,
            "appid": self.api_key,
            "units": unit,
            "lang": language
        }
        response = requests.get(url=API.ENDPOINT, params=parameters).json()

        if response["cod"] != 200:
            raise Exception(response["message"])

        return Current(response)

    def get_weather_city_name(self, city_name: str, state: str=None, country: str=None, unit: Unit=None, language: Language=None) -> Current:
        """return the current weather data for a specific city"""
        query = ",".join(filter(None, (city_name, state, country)))
        parameters = {
            "q": query,
            "appid": self.api_key,
            "units": unit,
            "lang": language
        }
        response = requests.get(url=API.ENDPOINT, params=parameters).json()

        if response["cod"] != 200:
            raise Exception(response["message"])

        return Current(response)

    def get_weather_city_id(self, city_id: str, unit: Unit=None, language: Language=None) -> Current:
        """return the current weather data for a specific id"""
        parameters = {
            "id": city_id,
            "appid": self.api_key,
            "units": unit,
            "lang": language
        }
        response = requests.get(url=API.ENDPOINT, params=parameters).json()

        if response["cod"] != 200:
            raise Exception(response["message"])

        return Current(response)

    def get_weather_zip_code(self, zip_code: str, unit: Unit=None, language: Language=None) -> Current:
        """return the current weather data for a specific zip"""
        parameters = {
            "zip": zip_code,
            "appid": self.api_key,
            "units": unit,
            "lang": language
        }
        response = requests.get(url=API.ENDPOINT, params=parameters).json()

        if response["cod"] != 200:
            raise Exception(response["message"])

        return Current(response)