class Weather:
    def __init__(self):
        self._weather_status: str
        self._temperature: float
        self._weather_details: str    

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
