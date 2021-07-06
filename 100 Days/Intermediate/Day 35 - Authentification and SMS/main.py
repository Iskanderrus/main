import requests

MY_LAT = 55.836410
MY_LNG = 37.657400
MY_ID = "10fe3286a023e9351c1b8fb7157cbd48"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": MY_ID,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.json())




