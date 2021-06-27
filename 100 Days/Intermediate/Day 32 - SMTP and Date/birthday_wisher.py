##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas as pd
import smtplib
import json
import os

# -- Sender data -- #
my_email = "alex_ru2002@list.ru"
with open("../../../../../Документы/password_manager_log.json", "r") as file:
    data = json.load(file)
mailru_password = data["www.list.ru"]["password"]

# -- Message choice --#
path = "letter_templates"
file = random.choice(os.listdir(path))
with open(f"{path}/{file}", "r") as data:
    message = data.read()

# -- Date checker -- #
today = dt.datetime.today()
df = pd.read_csv('dates.csv')
birthday_list = []
for index, row in df.iterrows():
    bd = dt.datetime(year=row["year"], month=row["month"], day=row["day"])
    if bd.month == today.month and bd.month == today.month:
        name = row["name"]
        message = message.replace("[NAME]", name)
        subject_list = ["Happy birthday!!!", "Finally this day!", f"To my dear {name}"]
        subject = random.choice(subject_list)

        with smtplib.SMTP("smtp.mail.ru") as connection:
            connection.starttls()  # used to secure connection...
            connection.login(user=my_email, password=mailru_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="a.n.chasovskoy@gmail.com",
                                msg=f"Subject:{subject}\n\n"
                                    f"{message}"
                                )
    else:
        print("No birthdays today ☺")


