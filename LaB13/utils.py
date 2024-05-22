import requests
from classes.weather_response import WeatherResponse

# инфо с weather api
weather_base = "http://api.weatherapi.com/v1/current.json"
my_key = "e1cab89d77bb4456925150243241905"
air_quality = "no"
language = "ru"

def get_weather(city: str):
    payload = {
            "key": my_key,
            "aiq": air_quality,
            "q": city or "Saint Petersburg",
            "lang": language,
            }

    r = requests.get(weather_base, params=payload, timeout=10)
    r.encoding = "utf-8"
    response_json = WeatherResponse(**r.json())
    location = response_json.location
    current = response_json.current
    return (location, current) # эти показатели прога берет с сайта из раздела response body
