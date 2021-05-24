import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 24.9342
MY_LONG = 121.36888
api_key = os.environ.get("API_KEY")
account_sid = "AC5dd1c53bd74c379a63060b7c92d197fa"
auth_token = os.environ.get("AUTH_TOKEN")

weather_param = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(ENDPOINT, params=weather_param)
response.raise_for_status()
weather_data = response.json()

weather_id_list = []
will_rain = False

for i in range(0, 12):
    weather_id_list.append(weather_data["hourly"][i]["weather"][0]["id"])
if min(weather_id_list) < 700:
    will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token,  http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+17089428697',
        to=os.environ.get("PHONE_NUMBER")
    )
    print(message.status)


# weather_slice = weather_data["hourly"][:12]

