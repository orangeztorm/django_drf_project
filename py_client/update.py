import requests

# endpoint = "http://httpbin.org/status/418"
# endpoint = "http://httpbin.org/anything"

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title': 'Hello world from another time',
    'price': 19999.99,
}

get_response = requests.put(endpoint, json=data) # Application programming interface (API) call

# print(get_response.text) # 418
print(get_response.json()) # 418