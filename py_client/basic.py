import requests

# endpoint = "http://httpbin.org/status/418"
# endpoint = "http://httpbin.org/anything"

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={'abc': 1234}, json={"query": "Hello world"}) # Application programming interface (API) call

# print(get_response.text) # 418
print(get_response.json()) # 418