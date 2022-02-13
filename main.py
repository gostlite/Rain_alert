import requests
import os
from token import My_token

Token = My_token
My_lat = 51.507351
My_long = -0.127758

parameter = {"lat": My_lat,
             "lon": My_long,
             "appid": Token,
             "exclude": "current,minutely,daily"}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for weather in weather_slice :
    condition_weather = weather["weather"][0]["id"]
    if int(condition_weather) <= 700:
        will_rain = True



if will_rain:
        print("come with an umbrella")
