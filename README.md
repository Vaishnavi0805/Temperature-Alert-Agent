
# ❄️ Temperature Alert Agent 🌡️

This repository contains the temperature alert agent using a single agent: `weather_alert`

1. `weather_alert`: This agent takes location as input and returns real-time current temperature at that location. It utilizes the [WeatherStack](https://weatherstack.com/) API to retrieve the desired results. Further, the agent also requires two additional parameter 'min_threshold_temperature' and 'max_threshold_temperature' which will define the minimum and the maximum temperature threshold value for which the notification will be received.

## Getting Started 🚀

To use the agents, follow the steps below:

### Step 1: Obtain API Key 🔑

Before running the agent, you need to obtain the required API keys:

#### WEATHERSTACK_API_KEY 🔌

1. Visit the Weatherstack API website: https://weatherstack.com/.
2. If you don't have an account, create one by signing up for free.
3. Once you are logged in, click on the Dashboard  at the top right corner.
4. Then on the Dashboard, you will see 'Your API Access Key'. 
5. Copy that API Key.

### Step 2: Set Environment Variables 🌐

Create a `.env` file in the `Temperature-Alert-Agent
` directory and export the obtained API keys as environment variables:

```bash
export access_key="{GET THE API KEY}"
```

### Step 3: Install Dependencies ⚙️

To use the environment variables from the `.env` file and install the project dependencies:

```bash
source .env
pip install uagents
```
### Step 4: Set Parameters🔧

To set the parameters of the agent, head towards the main.py in 'src' folder, and add the desired parameters you want :

```bash
main.py:

<line 6> temp_request =  TEMPRequest(location="{YOUR LOCATION}",min_threshold_temperature= {MINIMUM THRESHOLD} ,max_threshold_temperature = {MAXIMUM THRESHOLD}) </line 6>
```

### Step 4: Run the Project 🏃

To run the project and its agents:

```bash
python main.py
```

Now we have the temperature alert agent running, we will get the notifications in a timely duration. 🎉

### Submission for HackAI:  
Team: Vaishnavi Sarmalkar, Prerna Chheda, Manish Patil, Rohit Wahwal
