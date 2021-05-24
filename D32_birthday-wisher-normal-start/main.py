import datetime as dt
import pandas as pd
import smtplib
import random

##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

MY_EMAIL = "testing@gmail.com"
MY_PASSWORD = "testing123()"

today = (dt.datetime.now().month, dt.datetime.now().day)

birthday_data = pd.read_csv("birthdays.csv")

birthday_dict = {(row.month, row.day): row for (index, row) in birthday_data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        letter_contents = letter_file.read()
        letter_contents = letter_contents.replace('[NAME]', birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter_contents}"
        )


