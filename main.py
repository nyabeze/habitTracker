import requests
import datetime

USERNAME = "ryanny"
TOKEN = "p@55w0rd"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {'token': TOKEN,
               'username': USERNAME,
               'agreeTermsOfService': "yes",
               'notMinor': "yes"}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"
graph_config = {"id": GRAPH_ID,
                "name": "Coding-Graph",
                "unit": "km",
                "type": "float",
                "color": "shibafu"}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today = datetime.date(2024, 7, 18)
if today.month < 10:
    month = f"0{today.month}"
else:
    month = today.month
if today.day < 10:
    day = f"0{today.day}"
else:
    day = today.day

date = f"{today.year}{month}{day}"
print(date)
add_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

values_to_be_added = {"date": date,
                      "quantity": "12"}


# response = requests.post(url=add_value_endpoint, json=values_to_be_added, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

update_values = {
    "date": date,
    "quantity": "10.7"
}

# response = requests.put(url=update_pixel_endpoint, json=update_values, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
delete_values = {"date": date}


response = requests.delete(url=delete_endpoint, json=delete_values, headers=headers)
print(response.text)
