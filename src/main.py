from agents.temperature.agent_weather import agent as weather_alert
from messages.agent_weather import TEMPRequest
from messages.general import UAgentResponse
from uagents import Bureau,Agent, Context

temp_request = TEMPRequest(location="mumbai",min_threshold_temperature= 35 ,max_threshold_temperature = 38)
@weather_alert.on_interval(period=3600)
async def send_message(ctx: Context):
    await ctx.send("agent1qvjflcz3t00rym9qkpdvsd9fq6qnxvvxhdx87dhqwvp3vnk4wela2y907ft", temp_request)

@weather_alert.on_message(model=UAgentResponse)
async def message_handler(ctx: Context, _: str, msg: UAgentResponse):
    ctx.logger.info(f"{msg.options}")

if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    print(f"Adding weather alert agent to Bureau: {weather_alert.address}")
    bureau.add(weather_alert)
    bureau.run()