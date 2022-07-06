import os
import unittest

from package.constants import Language, Unit
from package.weather import CurrentWeather


class TestCurrentWeather(unittest.TestCase):

    def setup(self) -> CurrentWeather:
        return CurrentWeather(key=os.environ["API_KEY"])

    def test_get_weather_coords_correct(self) -> None:
        current = self.setup()
        latitude = 90
        longitude = 180

        result = current.get_weather_coords(latitude=latitude, longitude=longitude, unit=Unit.STANDARD, language=Language.ENGLISH)
        
        self.assertEqual(latitude, result.coordinates.latitude)
        self.assertEqual(longitude, result.coordinates.longitude)
    
    def test_get_weather_coords_wrong(self) -> None:
        current = self.setup()
        latitude = 1000
        longitude = 1000

        self.assertRaises(Exception, current.get_weather_coords, latitude, longitude)
    
    def test_get_weather_city_name_correct(self) -> None:
        current = self.setup()
        city_name = "London"
        country = "GB"

        result = current.get_weather_city_name(city_name=city_name, country=country, unit=Unit.STANDARD, language=Language.ENGLISH)
        
        self.assertEqual(country, result.general.city.country)
    
    def test_get_weather_city_name_wrong(self) -> None:
        current = self.setup()
        city_name = "Abc"
        country = "123"

        self.assertRaises(Exception, current.get_weather_city_name, city_name, country)
    
    def test_get_weather_city_id_correct(self) -> None:
        current = self.setup()
        city_id = "2643743"
        city_name = "London"

        result = current.get_weather_city_id(city_id=city_id, unit=Unit.STANDARD, language=Language.ENGLISH)
        
        self.assertEqual(city_name, result.general.city.name)
    
    def test_get_weather_city_id_wrong(self) -> None:
        current = self.setup()
        city_id = "-1000"

        self.assertRaises(Exception, current.get_weather_city_id, city_id)
    
    def test_get_weather_zip_code_correct(self) -> None:
        current = self.setup()
        zip_code = "10001"
        city_name = "New York"

        result = current.get_weather_zip_code(zip_code=zip_code, unit=Unit.STANDARD, language=Language.ENGLISH)
        
        self.assertEqual(city_name, result.general.city.name)
    
    def test_get_weather_zip_code_wrong(self) -> None:
        current = self.setup()
        zip_code = "Abc"

        self.assertRaises(Exception, current.get_weather_zip_code, zip_code)