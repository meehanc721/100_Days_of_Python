import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 40.712776
MY_LONG = -74.005974

MY_EMAIL = "codechad721@gmail.com"
PASSWORD = ",.Cm1993"

def near_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) #10
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) #23

    time_now = datetime.now().hour

    if  time_now >= sunset or time_now <= sunrise:
        return True

while True:
    if near_iss() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="codechad721@yahoo.com",
                msg=f"Subject:Look up for the ISS\n\nISS above you!"
            )

