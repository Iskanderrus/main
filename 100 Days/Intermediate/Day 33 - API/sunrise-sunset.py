import requests
from datetime import datetime

MY_LAT = 55.836410
MY_LNG = 37.657400


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise_hour_msk = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 3
sunset_hour_msk = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 3

sunrise_min = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
sunset_min = int(data["results"]["sunset"].split("T")[1].split(":")[1])

print(f"{sunrise_hour_msk}:{sunrise_min}")
print(f"{sunset_hour_msk}:{sunset_min}")



time_now = datetime.now()
print(time_now.hour)
