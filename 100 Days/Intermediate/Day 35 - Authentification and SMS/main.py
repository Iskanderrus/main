import requests
import os
from twilio.rest import Client


MY_LAT = 55.836410
MY_LNG = 37.657400
MY_ID = os.environ.get("OWM_API_APPID")


parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": MY_ID,
    "exclude": "current,minutely,daily"
}

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
codes = []
for hour in range(12):
    codes.append(weather_data["hourly"][hour]["weather"][0]["id"])
if min(codes) <= 600:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_=os.environ.get("MY_US_PHONE"),
        to=os.environ.get("MY_PHONE")
    )

    print(message.status)
