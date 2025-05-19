from dataclasses import dataclass
from model.Weather import Weather

@dataclass
class City:
    _name: str
    _population: int
    _country: str
    _weather: Weather

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = value
    
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, value):
        self._country = value

    @property
    def weather(self):
        return self._weather
    
    @weather.setter
    def weather(self, value):
        self._weather = value

