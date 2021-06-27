import smtplib
import json

my_email = "alex_ru2002@list.ru"

with open("../../../../../Документы/password_manager_log.json", "r") as file:
    data = json.load(file)

mailru_password = data["www.list.ru"]["password"]

name = "Anna"
message = f"Dear {name},\nit's my pleasure to be your friend and husband so long time. " \
          f"Hope to spend next decades with you.\n\nBest regards,\nAlexander\n\n" \
          f"P.S.: This message was sent by my new Python script."
subject = f"Message for {name}"

with smtplib.SMTP("smtp.mail.ru") as connection:
    connection.starttls()  # used to secure connection...
    connection.login(user=my_email, password=mailru_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="anna-btw@yandex.ru",
                        msg=f"Subject:{subject}\n\n"
                            f"{message}"
                        )
