import requests

def beers(page):
    page = int(page)
    response = requests.get('https://api.punkapi.com/v2/beers?page={}&per_page=25'.format(page))
    response = response.json()
    return (response)
