import requests

def get_cat_image():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data[0]['url']
    else:
        return None