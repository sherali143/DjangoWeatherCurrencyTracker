from django.conf import settings

import requests

# from .models import ExchangeRate


EXCHANGE_RATE_API_KEY = '5fb7feecc4de8233f8e8692f'
EXCHANGE_RATE_API_URL = f' https://v6.exchangerate-api.com/v6/5fb7feecc4de8233f8e8692f/latest/USD'


WEATHER_API_KEY = ' 238bca69ca9a592e7d2a0c25203176c1 '
WEATHER_API_URL = f' https://api.weatherstack.com/current?access_key=238bca69ca9a592e7d2a0c25203176c1'

def update_exchange_rate():
    response = requests.get(EXCHANGE_RATE_API_URL)
    data = response.json()
    return data 



def fetch_weather_data(city):
    WEATHER_API_KEY = '238bca69ca9a592e7d2a0c25203176c1'
    WEATHER_API_URL = f'https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={city}'
    
    # Make the GET request to the Weatherstack API
    response2 = requests.get(WEATHER_API_URL)
    data2 = response2.json()
    # Return the JSON response data
    return data2
