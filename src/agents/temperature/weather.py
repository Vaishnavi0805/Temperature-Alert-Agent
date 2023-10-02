import requests

access_key = 'd2fc04587fe1111cdebb51da78f8d699'
location = 'New York'

units = 'm'  # 'm' for metric units (Celsius), 'f' for imperial units (Fahrenheit)
language = 'en'  


def current(url_current):
    response = requests.get(url_current)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['current']['temperature']
        print(f'Temperature in {location}: {temperature}°C')
    else:
        print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")


def forecast(url_forecast):
    response = requests.get(url_forecast)
    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
        # temperature = weather_data['current']['temperature']
        # print(f'Temperature in {location}: {temperature}°C')
    else:
        print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")


url_current = f'http://api.weatherstack.com/current?access_key={access_key}&query={location}'
url_forecast = f'http://api.weatherstack.com/foecast?access_key={access_key}&query={location}'


current(url_current)
#forecast(url_forecast)