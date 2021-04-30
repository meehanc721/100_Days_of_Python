import requests
from datetime import datetime

USERNAME = "codechad721"
TOKEN = "suckalemon"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Nail Biting Graph",
    "unit": "Times",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2021, month=4, day=27)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210428"


update_pixel_config = {
    "quantity": "15"
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
print(response.text)
