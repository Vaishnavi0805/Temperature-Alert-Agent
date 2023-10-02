from agents.temperature.weather1 import agent as weather_alert
from uagents import Bureau

if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    print(f"Adding weather alert agent to Bureau: {weather_alert.address}")
    bureau.add(weather_alert)
    bureau.run()