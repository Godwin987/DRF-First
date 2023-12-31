import requests

product_id = input("Input Product ID: ")
try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} not a valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/" #http://127.0.0.1:8000/ 

get_response = requests.delete(endpoint) # HTTP Request

# print(get_response.json())
