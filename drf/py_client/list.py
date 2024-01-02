import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/" #http://127.0.0.1:8000/ 
username = input("Username: ")
password = getpass()
auth_response = requests.post(auth_endpoint, json={"username": "Godwin", "password": password}) # HTTP Request

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/api/products/" #http://127.0.0.1:8000/ 
    headers = {
        "Authorization":f"Bearer {token}"
    } 
    get_response = requests.get(endpoint, headers=headers) # HTTP Request

    print(get_response.json())

# endpoint = "http://localhost:8000/api/products/" #http://127.0.0.1:8000/ 

# get_response = requests.get(endpoint) # HTTP Request

# print(get_response.json())
