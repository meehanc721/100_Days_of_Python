import requests
from twilio.rest import Client


STOCK_NAME = "GME"
COMPANY_NAME = "GameStop"

STOCK_API_KEY = "UNLI5AYGGJV6LYB7"
STOCK_ENDPOINT = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GME&apikey={STOCK_API_KEY}"

NEWS_API_KEY = "f2c23a0b6c484b349e3ee09d64ffcb86"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

tw_account_sid = "AC0cfc4da53b41e7a8564ac48010b7ef67"
tw_auth_token = "f5de37bd41808797ee07fa581c81495d"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "GME",
    "apikey": STOCK_API_KEY,
}

# Get our stock API data
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()


# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday = list(stock_data["Time Series (Daily)"].keys())[0]
yesterday_close = float(stock_data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
print(yesterday_close)
# Get the day before yesterday's closing stock price
day_before_yesterday = list(stock_data["Time Series (Daily)"].keys())[1]
day_before_yesterday_close = float(stock_data["Time Series (Daily)"][f"{day_before_yesterday}"]["4. close"])
print(day_before_yesterday_close)
# Find the positive difference between days
difference = float(yesterday_close - day_before_yesterday_close)
print(difference)
up_down = None
if difference > 0:
    up_down = "▲"
else:
    up_down = "▼"


# Work out the percentage difference in price between closing price
diff_percent = round((difference / float(yesterday_close)) * 100)
print(diff_percent)

if abs(diff_percent) > 10:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles_list = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nSummary: {article['description']}" for article in three_articles]

    for i in range(0, 3):
        client = Client(tw_account_sid, tw_auth_token)
        message = client.messages \
            .create(
            body=formatted_articles_list[i],
            from_='+116193822382',
            to='+17029349088'
        )
        print(message.status)




#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

