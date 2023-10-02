import os
import uuid

import requests
from uagents import Agent, Context, Protocol
from messages import TEMPRequest, KeyValue, UAgentResponse, UAgentResponseType

access_key = 'd2fc04587fe1111cdebb51da78f8d699'
location = 'New York'

TEMP_SEED = os.getenv("TEMP_SEED", "secret phrase")

agent = Agent(
    name="temp_agent",
    seed=TEMP_SEED,
)

def current(location):
    url_current = url_current = f'http://api.weatherstack.com/current?access_key={access_key}&query={location}'
    response = requests.get(url_current)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['current']['temperature']
        # print(f'Temperature in {location}: {temperature}°C')
        return temperature
    else:
        print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")
        return None

# Setting Thresholds
min_temp_threshold = 19
max_temp_threshold = 20

def threshold():
    temperature = current(location)
    if temperature < min_temp_threshold:
        print(f'Temperature is below {min_temp_threshold}°C')
    elif temperature > max_temp_threshold:
        print(f'Temperature is above {max_temp_threshold}°C')
    else:
        print(f'Temperature in {location}: {temperature}°C')


threshold()