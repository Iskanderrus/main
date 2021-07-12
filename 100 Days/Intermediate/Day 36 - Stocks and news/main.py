import requests
from datetime import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = "9V4NM6P0KYIBQU6Q"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key,
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
tesla_data = response.json()
tesla_dates = tesla_data["Time Series (Daily)"]

tesla_close = []

for date in tesla_dates.items():
    tesla_close.append((date[0], date[1]['4. close']))

for i in range(len(tesla_close)):
    try:
        delta = abs(round(((float(tesla_close[i][1]) / float(tesla_close[i + 1][1]) - 1) * 100), 2))
    except IndexError:
        print("Reached last day.")
    finally:
        if delta >= 5:
            print(f"Get news on {tesla_close[i + 1][0]}")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# # STEP 1: Use https://newsapi.org/docs/endpoints/everything When STOCK price increase/decreases by 5% between
# yesterday and the day before yesterday then print("Get News"). HINT 1: Get the closing price for yesterday and the
# day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive
# difference is 20. HINT 2: Work out the value of 5% of yerstday's closing stock price.


# # STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


# # STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash. """
