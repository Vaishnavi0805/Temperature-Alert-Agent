import requests
from uagents import Agent

access_key = 'd2fc04587fe1111cdebb51da78f8d699'
location = 'New York'

units = 'm'  # 'm' for metric units (Celsius), 'f' for imperial units (Fahrenheit)
language = 'en'  


def current(url_current):
    response = requests.get(url_current)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['current']['temperature']
        # print(f'Temperature in {location}: {temperature}°C')
        return temperature
    else:
        print(f"Error: Unable to retrieve weather data. Status code: {response.status_code}")
        return None


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


# current(url_current)
#forecast(url_forecast)

# # Setting Thresholds
# min_temp_threshold = 19
# max_temp_threshold = 20

# def threshold():
#     temperature = current(url_current)
#     # print(temperature)
#     if temperature < min_temp_threshold:
#         print(f'Temperature is below {min_temp_threshold}°C')
#     elif temperature > max_temp_threshold:
#         print(f'Temperature is above {max_temp_threshold}°C')
#     else:
#         print(f'Temperature in {location}: {temperature}°C')


# threshold()

#############################
# Import necessary libraries
from uAgent import Agent
import requests
import time

# Initialize the Agent
agent = Agent()

# Function to set temperature alerts
def set_temperature_alert(location, min_temp, max_temp):
    # First generate a secure seed phrase (e.g. https://pypi.org/project/mnemonic/)
    SEED_PHRASE = "notifier"
    
    # Copy the address shown below
    print(f"Your agent's address is: {Agent(seed=SEED_PHRASE).address}")
    
    # Then sign up at https://agentverse.ai to get an API key and register your agent
    API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYXBpLWtleSIsIm5vbmNlIjoiMTlhNDY4OGYtMjAxYS00ZjEyLWE0OGMtOTM5ZWUwM2E5MTZiIiwic3ViIjoiNWU2MmY3YTVjYWI5MzM4OGE5NmNiMDg1NjE4NzM5ODYyY2I1NDVhNDIwNDQyZDQwIiwiZXhwIjoxNzA0MDA0NjE2fQ.e8-ssommtVS4-6oHzpgVaKGNG_KHNaWUQtcMLT2TBMA"
    while True:
        current_temp = current(location)
        if current_temp is not None:
            if current_temp < min_temp:
                agent = Agent(
                name="alice",
                seed=SEED_PHRASE,
                mailbox=f"{API_KEY}@wss://agentverse.ai",
                
            )
                agent.send_notification(f"Temperature Alert: It's too cold in {location}! Current temperature: {current_temp}°C")
            elif current_temp > max_temp:
                agent.send_notification(f"Temperature Alert: It's too hot in {location}! Current temperature: {current_temp}°C")
        time.sleep(3600)  # Check temperature every hour

# Function to manually check and report the current temperature
def check_temperature(location):
    current_temp = current(location)
    if current_temp is not None:
        agent.send_notification(f"Current temperature in {location}: {current_temp}°C")

# Set your temperature range
min_temperature = 20  # Set your minimum temperature threshold (in Celsius)
max_temperature = 30  # Set your maximum temperature threshold (in Celsius)

# Start the temperature alert agent
set_temperature_alert(location, min_temperature, max_temperature)

# Example: Manually check the temperature
# Uncomment the next line to check the temperature manually
# check_temperature(preferred_location)

def send_notification():
    