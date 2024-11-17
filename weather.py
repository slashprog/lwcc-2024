
GEOCODER_URL = "http://api.openweathermap.org/geo/1.0/direct"

WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"


import httpx

class Weather:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__city = None
        self.__temperature = None
        self.__humidity = None
        self.__lat = self.__lon = None

    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, location):
        self.__city = location
        location_params = {
            "q": location,
            "limit": 1,
            "appid": self.__api_key 
        }

        response = httpx.get(GEOCODER_URL, params=location_params)
        rec = response.json()[0]
        self.__lat, self.__lon = rec["lat"], rec["lon"]

    def get_weather(self):
        weather_params = {
            "lat": self.__lat,
            "lon": self.__lon,
            "units": "metric",
            "appid": self.__api_key
        }
        response = httpx.get(WEATHER_URL, params=weather_params)
        rec = response.json()
        self.__temperature = rec["main"]["temp"]
        self.__humidity = rec["main"]["humidity"]
        return self.__temperature, self.__humidity
    
    @property
    def temperature(self):
        self.get_weather()
        return self.__temperature
    
    @property
    def humidity(self):
        self.get_weather()
        return self.__humidity

  