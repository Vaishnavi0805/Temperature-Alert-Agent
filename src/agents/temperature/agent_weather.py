import requests
import uuid
import os
from uagents import Agent
import requests
from messages.agent_weather import TEMPRequest
from messages.general import UAgentResponse, UAgentResponseType
from uagents import Agent, Context, Protocol

from dotenv import load_dotenv
load_dotenv("src\.env")
access_key=os.environ.get("access_key")

agent = Agent(
    name="weather_alert",
    seed="temperature alert"
)
 
weather_protocol = Protocol("weather")


@weather_protocol.on_message(model=TEMPRequest, replies= UAgentResponse)
async def weather(ctx: Context, sender: str, msg: TEMPRequest):
    location=msg.location
    def get_weather(location):
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
    ctx.logger.info(f"Received message from {sender}")
    try:
        temperature = get_weather(msg.location)
        # request_id = str(uuid.uuid4())
        if temperature < msg.min_threshold_temperature:
            result=f'Temperature is below {msg.min_threshold_temperature}°C'
        elif temperature >msg.max_threshold_temperature:
            result=f'Temperature is above {msg.max_threshold_temperature}°C'
        else:
            result=f'Temperature in {location}: {temperature}°C'
        print(result)
       
        await ctx.send(
            sender,
            UAgentResponse(
                options=result,
                type=UAgentResponseType.SELECT_FROM_OPTIONS,
                # request_id=request_id,
            ),
        )
    except Exception as exc:
        ctx.logger.error(exc)
        await ctx.send(
            sender, UAgentResponse(message=str(exc), type=UAgentResponseType.ERROR)
        )

agent.include(weather_protocol)
    
