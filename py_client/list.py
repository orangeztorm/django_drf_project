import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"

username = input('Username: ')
password = getpass('Password:')

auth_response = requests.post(auth_endpoint, json={
    'username': username,
    'password': password,  
})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    print(token)


# endpoint = "http://httpbin.org/status/418"
# endpoint = "http://httpbin.org/anything"

    endpoint = "http://localhost:8000/api/products/"


    get_response = requests.get(endpoint, headers=headers) # Application programming interface (API) call

# print(get_response.text) # 418
    print(get_response.json()) # 418
    
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print(results) 
    # if next_url is not None:
    #     next_response = requests.get(next_url, headers=headers)
    #     print(next_response.json())