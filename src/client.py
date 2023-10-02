# from messages import TopDestinations, UAgentResponse
from messages.weather1 import TEMPRequest
from messages.general import UAgentResponse
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os

# TOP_DESTINATIONS_CLIENT_SEED = os.getenv("TOP_DESTINATIONS_CLIENT_SEED", "top_destinations_client really secret phrase :)")

weather_client = Agent(
    name="weather_alert",
    port=8008,
    seed='temperature alert',
    endpoint=["http://127.0.0.1:8008/submit"],
)
fund_agent_if_low(weather_client.wallet.address())

temp_request = TEMPRequest(location="new york",min_threshold_temperature= 19 ,max_threshold_temperature = 40)

@weather_client.on_interval(period=10.0)
async def send_message(ctx: Context):
    await ctx.send("agent1qvjflcz3t00rym9qkpdvsd9fq6qnxvvxhdx87dhqwvp3vnk4wela2y907ft", temp_request)

@weather_client.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
    ctx.logger.info(f"{msg.options}")

if __name__ == "__main__":
    weather_client.run()