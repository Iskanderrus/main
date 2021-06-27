import smtplib
import json
import datetime as dt
import random

# --- Sender data ---#
my_email = "alex_ru2002@list.ru"
with open("../../../../../Документы/password_manager_log.json", "r") as file:
    data = json.load(file)
mailru_password = data["www.list.ru"]["password"]

# --- Message data --- #
with open("quotes.txt", "r") as data:
    quotes_list = data.readlines()

message = random.choice(quotes_list)
subject = "Your personal quote of the day"

# --- Weekday checker ---#quotes_list = []
now = dt.datetime.now()
if now.weekday() == 0 and now.hour == 10:
    with smtplib.SMTP("smtp.mail.ru") as connection:
        connection.starttls()  # used to secure connection...
        connection.login(user=my_email, password=mailru_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="a.n.chasovskoy@gmail.com",
                            msg=f"Subject:{subject}\n\n"
                                f"{message}"
                            )
else:
    print("It's not right time to practice your wisdom now...")
