import requests

API_KEY = 'c30bda76c0157443467d6476d3bba3f1'
BASE_URL = 'https://api.openweathermap.org/data/2.5/'
city = input('Enter a city name: ')
report_type = input('Enter weather(w) or 5 day forecast(5): ')


def weather():
    weather_request_url = f'{BASE_URL}weather?&q={city}&appid={API_KEY}'
    response = requests.get(weather_request_url)

    if response.status_code == 200:
        data = response.json()
        weatherdata = (data['weather'][0]['description'])
        weathers = str.capitalize(weatherdata)
        temp = data['main']['temp']
        fahrenheit = int((temp - 273) * 1.8 + 32)
        wind = int(data['wind']['speed'])
        print(f'Weather: {weathers}')
        print(f'Temp: {fahrenheit}F')
        print(f'Wind: {wind}mph')
    else:
        print('An error occurred.')


def forecast():
    forecast_request_url = f'{BASE_URL}forecast?&q={city}&appid={API_KEY}'
    response = requests.get(forecast_request_url)

    if response.status_code == 200:
        data = dict(response.json())
        cut = range(6, 40, 8)
        for c in cut:
            c = int(c)
            day = data['list'][c]['dt_txt']
            temp = data['list'][c]['main']['temp']
            fahrenheit = int((temp - 273) * 1.8 + 32)
            weatherdata = (data['list'][c]['weather'][0]['description'])
            weathers = str.capitalize(weatherdata)
            print(f'{day} Temp: {fahrenheit} \nWeather: {weathers}')

    else:
        print('An error occurred.')


if report_type == 'w':
    weather()
elif report_type == '5':
    forecast()
else:
    print('Invalid selection.')
