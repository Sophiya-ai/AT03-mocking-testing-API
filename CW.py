import requests


def get_weather(api_key, town):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={town}&limit=5&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None