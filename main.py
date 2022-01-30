import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "yshath1"
Token = "ruifsk59fjfkf"
GRAPH_NAME = "cycling"
account_details = {
    "token": Token,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response=requests.post(url=PIXELA_ENDPOINT,json=account_details)
# print(response.text)
AUTH_TOKEN = {'X-USER-TOKEN': Token}
GRAPH_ID = "shaka2022"
graph_creation = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
# create_graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# response = requests.post(url=create_graph_endpoint,headers=AUTH_TOKEN, json=graph_creation)
# print(response.text)

post_pixel_end = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# today=datetime.now()
today = datetime.now()
post_pixel = {
    "date": today.strftime("%Y%m%d"), "quantity": input("How many run did you do today? ")
}

# response = requests.get(url=post_pixel_end, headers=AUTH_TOKEN, json=post_pixel)
# print(response.text)
change_pixel = {
    "quantity": "8.5"
}
# post_pixel_change = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/2022/01/24"
# response = requests.put(url=post_pixel_change, json=change_pixel,headers=AUTH_TOKEN,)
# print(response.text)

# delete_pixel=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/2022/01/24"
# response = requests.put(url=post_pixel_change, json=change_pixel,headers=AUTH_TOKEN,)
# print(response.text)
