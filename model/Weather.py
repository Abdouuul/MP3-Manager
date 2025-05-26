from __future__ import annotations
from Model.City import City
from Config.app_config import API_URL, API_KEY

class Weather:
    _weather_status: str
    _temperature: float
    _weather_details: str    
    _city : City
    def __init__(self):
        self._api_url = API_URL + self._city.name + "&appid=" + API_KEY
    

    @property
    def weather_status(self):
        return self._weather_status
    
    @weather_status.setter
    def weather_status(self, current_status):
        self._weather_status = current_status
    
    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, current_temp):
        self._temperature = current_temp
    
    @property
    def weather_details(self):
        return self._weather_details
    
    @weather_details.setter
    def weather_details(self, details):
        self._weather_details = details

    @property
    def api(self):
        return self._api_url
    
    @api.setter
    def api(self, api):
        self._api_url = api
    

