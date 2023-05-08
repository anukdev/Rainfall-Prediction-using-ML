#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5a7bd2ff8b52b98fc8337150314e69c6"
account_sid = "AC484debae23259bb25d70dca78fadecb5"
auth_token = "317c47143b9390b85a29b7539b111a31"

weather_params = {
  "lat": 8.346230,
  "lon": 77.076271,
  "appid": api_key,
  "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
# print(response.json())
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
  condition_code = hour_data["weather"][0]["id"]
  if int(condition_code) < 700:
    will_rain = True

if will_rain:
  proxy_client = TwilioHttpClient()
  # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

  client = Client(account_sid, auth_token, http_client=proxy_client)
  message = client.messages \
      .create(
      body="It's going to rain today. Remember to bring an ☔️",
      from_="+12174039287",
      to="+917560910094"
  )
  print(message)

# API Key a9c3728770628e8181a5ad71547a26d0
# SID AC484debae23259bb25d70dca78fadecb5
# AUTH TOKEN 317c47143b9390b85a29b7539b111a31