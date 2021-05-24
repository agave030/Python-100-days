import smtplib
import datetime as dt
import random

MY_EMAIL = "testing@gmail.com"
MY_PASSWORD = "testing123()"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="recepient@gmail.com",
            msg=f"Subject:Motivation\n\n{quote}"
        )









