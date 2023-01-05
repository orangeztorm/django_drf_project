import requests

# endpoint = "http://httpbin.org/status/418"
# endpoint = "http://httpbin.org/anything"

product_id = input("Enter product ID: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print('product id is not valid')

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.get(endpoint, params={'abc': 1234}, json={"content": "Hello world"}) # Application programming interface (API) call

    # print(get_response.text) # 418
    print(get_response.json()) # 418
    