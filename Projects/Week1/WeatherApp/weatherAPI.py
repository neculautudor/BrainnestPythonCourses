''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

import requests
from WeatherApp.confidential.key import KEY


class LocationToCoordConverter:
    # i created this class to get coordinates from city name, because
    # using a city name directly is deprecated
    def __init__(self, max_locations):
        # the api can return multiple locations in case the user inputs a country i think,
        # but i assumed we only use cities and we only need one coordinate
        self.base_url = 'http://api.openweathermap.org/geo/1.0/direct?q='
        self.last_url =  f'&limit={max_locations}' + f'&appid={KEY}'

    def get_coord(self, city):
        if not city:
            return None
        # treating the case where the city is None
        complete_url = self.base_url + city + self.last_url
        # we concatenate the city between the base url and the last url(what we already knew)
        response = requests.get(complete_url) # fetching the actual data
        if not len(response.json()):
            return None
        # in case the api does not find the city, or the input is wrong
        response = response.json()[0] # decoding the data with json and we get the first element because it returns a list
        return response['lat'], response['lon'] # we only need the latitude and longitude


class WeatherGetter:
    def __init__(self):
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.locationConverter = LocationToCoordConverter(max_locations=1)
        # we get the coordinates

    def get_weather(self, city):
        if not self.get_coord(city):
            return 'City not found'
            # in any of the cases written above, we return a string with this message
        lat, lon = self.get_coord(city)
        complete_url = self.base_url + f'lat={lat}' + f'&lon={lon}' + f'&appid={KEY}'
        response = requests.get(complete_url)
        if not response:
            return 'Weather not found(unavailable)'
        return response.json()

    def get_coord(self, city):
        return self.locationConverter.get_coord(city)
    # function for cleaner code
