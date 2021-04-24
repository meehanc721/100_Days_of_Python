import requests
from twilio.rest import Client


MY_LAT = 31.578461
MY_LONG = -84.155884

api_key = "insert_key_here"
api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
tw_account_sid = "AC0cfc4da53b41e7a8564ac48010b7ef67"
tw_auth_token = "insert_token_here"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_codes = []
for i in range(0, 12):
    weather_codes.append(weather_data["hourly"][i]["weather"][0]["id"])

will_rain = any(x < 700 for x in weather_codes)
if will_rain:
    client = Client(tw_account_sid, tw_auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_='+116193822382',
        to='+17029349088'
    )
    print(message.status)



