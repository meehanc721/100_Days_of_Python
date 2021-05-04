import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/57bd2355354ccf51dd6624d8bd381b5b/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # 1. Use the Sheety API to GET all the data in that sheet
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # 6. PUT request and use the row id, ('id'), from sheet_data to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        # Gets the IATA code for each city
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )