from requests import get

weather_api = f'https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=0fbf3c3afac48c7bf1d1491776e2cf32'
res = get(weather_api).json()
print(res['main']['temp'])