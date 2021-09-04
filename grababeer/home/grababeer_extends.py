import requests
from .models import Beers, Malts, Hops


def beers(page):
    page = int(page)
    response = requests.get(
        "https://api.punkapi.com/v2/beers?page={}&per_page=25".format(page)
    )
    response = response.json()
    return response


def single_beer(beer_id):
    response = requests.get("https://api.punkapi.com/v2/beers/{}".format(beer_id))
    response = response.json()
    favourite_beer = Beers(
        barcode=response[0]["id"],
        name=response[0]["name"],
        img_url=response[0]["image_url"],
        IBU=response[0]["ibu"],
        description=response[0]["description"],
    )
    favourite_beer.save()

    hops = response[0]['ingredients']['hops']
    for element in hops:
        #Saving hops contained in this beer
        hops_query = Hops(name=element['name'])
        hops_query.save()
        #Linking hops to that beer
        beer_query = Beers(barcode=beer_id)
        print(beer_query)



    malts = response[0]['ingredients']['malt']
    for element in malts:
        malts_query = Malts(name=element['name'])
        malts_query.save()
