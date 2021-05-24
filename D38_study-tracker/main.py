import requests
from datetime import datetime
import os

sheet_endpoint = "https://api.sheety.co/1f0702099249cfeb751c740ec314e040/myStudy/sheet1"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_inputs = {
    "sheet1": {
        "date": today_date,
        "time": now_time,
        "exercise": input("What subject did you study today?"),
        "duration": input("And how long?"),
    }
}

#No Auth
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
print(sheet_response.text)
