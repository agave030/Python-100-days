import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEYS = "7RSIV2W1P6JPR5JE"
NEWS_API_KEYS = "81a67d28c73d4ab9844bcab73b1d315d"
ACCOUNT_SID = "AC5dd1c53bd74c379a63060b7c92d197fa"
AUTH_TOKEN = "#"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEYS,
}

news_params = {
    "apiKey": NEWS_API_KEYS,
    "qInTitle": COMPANY_NAME,
    "sortBy": "relevancy",
}

yesterday = (dt.datetime.now() - dt.timedelta(1)).strftime('%Y-%m-%d')
day_before_yesterday = (dt.datetime.now() - dt.timedelta(2)).strftime('%Y-%m-%d')

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
yesterday_price = stock_data["Time Series (Daily)"][yesterday]["4. close"]
day_before_yesterday_price = stock_data["Time Series (Daily)"][day_before_yesterday]["4. close"]

positive_difference = abs(round(float(yesterday_price) - float(day_before_yesterday_price),  2))
percentage = round(positive_difference / float(yesterday_price), 2)
if percentage >= 0.05:

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_data = news_response.json()['articles'][:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
                    .create(
                         body=f"title: {news_data[0]['title']}\ndescription: {news_data[0]['description']}"
                              f"title: {news_data[1]['title']}\ndescription: {news_data[1]['description']}"
                              f"title: {news_data[2]['title']}\ndescription: {news_data[2]['description']}",
                         from_='+17089428697',
                         to='#'
                     )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

