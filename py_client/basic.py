import requests

# endpoint = "http://httpbin.org/status/418"
endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint) # Application programming interface (API) call

print(get_response.text) # 418