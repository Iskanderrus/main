import json
import smtplib
import time
from datetime import datetime
import requests

MY_LAT = 55.836410
MY_LONG = 37.657400


def is_close(d_lat, d_lng):  # Your position is within +5 or -5 degrees of the ISS position.
    if d_lng <= 5 or d_lat <= 5:
        return True


while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    delta_lng = abs(MY_LONG - iss_longitude)
    delta_lat = abs(MY_LAT - iss_latitude)

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 3

    time_now = datetime.now()
    hour_now = time_now.hour

    if sunrise < hour_now > sunset and is_close(delta_lat, delta_lng):
        my_email = "alex_ru2002@list.ru"
        with open("../../../../../Документы/password_manager_log.json", "r") as file:
            data = json.load(file)
        mailru_password = data["www.list.ru"]["password"]
        with smtplib.SMTP("smtp.mail.ru") as connection:
            connection.starttls()  # used to secure connection...
            connection.login(user=my_email, password=mailru_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:ISS is close to you\n\n"
                                    f"Have a look up! There is ISS over your head."
                                )
            print(f"Message sent to {my_email}")
    elif is_close(delta_lat, delta_lng):
        print(f"Current ISS position: {iss_latitude}, {iss_longitude}")
        print("ISS is close but it's not dark enough to see it.")
    else:
        print(f"Hours to sunset: {sunset - hour_now}")
        print(f"Hours to sunrise: {hour_now - sunrise}")
        print(f"Current ISS position: {iss_latitude}, {iss_longitude}")

    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
