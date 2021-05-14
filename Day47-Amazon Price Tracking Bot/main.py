from bs4 import BeautifulSoup
import requests
from pprint import pprint
import lxml
import smtplib

# Had to use Walmart because Amazon was being mean to my scraper
url = "https://www.walmart.com/ip/Instant-Pot-Ultra-6-Qt-10-in-1-Multi-Use-Programmable-Pressure-Cooker-Slow-Rice-Yogurt-Maker-Cake-Egg-Saut-Steamer-Warmer-Sterilizer/515428065"

# Get the HTML of the Instant Pot product page
response = requests.get(url,
                        headers={
                            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                            "Accept-Language": "en-US,en;q=0.9",
                            "Accept-Encoding": "gzip, deflate",
                            "Cookie":"PHPSESSID=rmg2423p015s9fch6vl6evsdb6; _ga=GA1.2.1069491515.1621024371; _gid=GA1.2.691592355.1621024371",
                            "X-Http-Proto": "HTTP/1.1",
                            "X-Real-Ip": "67.243.223.127"
                        }
                    )
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "lxml")
price = soup.find(name="span", class_="price-characteristic").getText()
price_float = float(price)
print(price_float)

title = soup.find(name="h1", class_="prod-ProductTitle prod-productTitle-buyBox font-bold").getText()

if price_float > 100:
    my_email = "############"
    password = "###########"

    message = f"Subject: Price Drop\n\n{title} is now {price_float}.\n\nBuy here: {url}"
    message = message.encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="meehanc721@gmail.com",
            msg=message
        )
