import requests
from .models import Beers, Malts, Hops


def beers(page):
    """Gets a page of 25 beers"""
    page = int(page)
    response = requests.get(
        "https://api.punkapi.com/v2/beers?page={}&per_page=25".format(page)
    )
    response = response.json()
    return response


def save_my_beer(beer_id):
    """registers a single beer in DB, adds malts and hops and links it to related beer"""
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
        beer_query = Beers.objects.get(barcode=beer_id)
        hops_query.hops_in_that_beer.add(beer_query)


    malts = response[0]['ingredients']['malt']
    for element in malts:
        #Saving malts conatained in that beer
        malts_query = Malts(name=element['name'])
        malts_query.save()
        #Linking malts to that beer
        beer_query = Beers.objects.get(barcode=beer_id)
        malts_query.malts_in_that_beer.add(beer_query)

def single_beer(beer_id):
    response = requests.get(
        "https://api.punkapi.com/v2/beers/{}".format(beer_id)
    )
    response = response.json()
    return response
