# OpenWeather API Wrapper
An easy to use wrapper written in Python.

**Dependencies**
```
Requests
```

**Notes**

It will look for an environment variable named `API_KEY` before running the tests. Make sure this variable is set or supply the OpenWeather API key in a different way.

**Usage**

Create a **CurrentWeather** instance using an API key.
```python
current_weather = CurrentWeather(key="YOUR API KEY")
```

Retrieve weather data by coordinates.
```python
current_weather.get_weather_coords(latitude=90, longitude=180)
```

Retrieve weather data by city name.
```python
current_weather.get_weather_city_name(city_name="London", country="GB")
```

Retrieve weather data by city id.
```python
# city codes can be found on the openweather docs
current_weather.get_weather_city_id(city_id="2643743")
```

Retrieve weather data by zip code.
```python
current_weather.get_weather_zip_code(zip_code="10001")
```

Further more you can specify optional arguments like unit and language.
```python
# all supported units and languages can be found in the corresponding classes
current_weather.get_weather_coords(latitude=90, longitude=180, unit=Unit.STANDARD, language=Language.ENGLISH)
```

All methods in **CurrentWeather** return a **Current** instance.
```python
current = current_weather.get_weather_coords(latitude=45, longitude=90)

# check if it is raining currently
current.weather.rain.is_raining()

# check if there are any clouds currently
current.weather.clouds.has_clouds()

# get the current temperature
current.weather.temperature.degree

# convert kelvin to celsius
current.weather.temperature.convert_to_celsius()
```
