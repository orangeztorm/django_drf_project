import requests

# endpoint = "http://httpbin.org/status/418"
# endpoint = "http://httpbin.org/anything"

endpoint = "http://localhost:8000/api/products/"
data = {
    'title': 'New product',
    'price': 19.99,
}

get_response = requests.post(endpoint, json=data) # Application programming interface (API) call

# print(get_response.text) # 418
print(get_response.json()) # 418