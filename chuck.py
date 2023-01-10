import requests
import random

API_KEY = 'c30bda76c0157443467d6476d3bba3f1'
BASE_URL = 'https://api.chucknorris.io/jokes/search'

topic = input('Enter a topic for Chuck: ')
request_url = f'{BASE_URL}?query={topic}'
response = requests.get(request_url)


if response.status_code == 200:
    try:
        data = response.json()
        total = data['total']
        so_random = random.randint(0, total)
        value = data['result'][so_random]['value']
        print(value.capitalize())
    except IndexError:
        print('Chuck doesn\'t care about this stupid shit.')
else:
    print('An error occurred.')
