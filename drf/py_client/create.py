import requests

endpoint = "http://localhost:8000/api/products/" #http://127.0.0.1:8000/ 

headers = {'Authorization': 'Bearer e6b9471cdfff84b6a4dad4a840146915a0a16375'}
data = {
    "title": "New Field after Auth",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers) # HTTP Request

print(get_response.json())
