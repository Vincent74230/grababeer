from django.test import TestCase
from .models import Beers, Malts, Hops

class DisplayPages(TestCase):
    """Tests home and favourites page response"""
    def test_display_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_display_favourites(self):
        response = self.client.get('/my_favourites')
        self.assertEqual(response.status_code, 200)


class RegisterFavourites(TestCase):
    """Tests save_my_beer view"""
    def test_saving_favourite(self):
        response = self.client.get("/save_my_beer", {"favourite_beer":1,},)
        self.assertEqual(response.status_code, 302)

        #See if beer is 'Beers' table in DB
        saved_beer = Beers.objects.all()
        self.assertEqual(len(saved_beer), 1)
        self.assertEqual(saved_beer[0].barcode, 1)
        self.assertEqual(saved_beer[0].name, 'Buzz')

        #See if hops and malts are in DB
        malts = Malts.objects.all()
        self.assertEqual(len(malts), 3)
        hops = Hops.objects.all()
        self.assertEqual(len(malts), 3)

        #Checking many-to-many relationships
        beer_that_contains_Fuggles_hop = Beers.objects.filter(hops='Fuggles')
        self.assertEqual(beer_that_contains_Fuggles_hop[0].name, 'Buzz')
        beer_that_contains_Munich_malt = Beers.objects.filter(malts='Munich')
        self.assertEqual(beer_that_contains_Munich_malt[0].name, 'Buzz')
