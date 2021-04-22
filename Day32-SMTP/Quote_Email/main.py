
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
today = now.weekday()
if today == 6:
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)

    my_email = "codechad721@gmail.com"
    password = "suckalemon"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="codechad721@yahoo.com",
            msg=f"Subject:Monday Inspiration\n\n{quote}"
        )
