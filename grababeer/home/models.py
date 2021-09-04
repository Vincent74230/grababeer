from django.db import models


class Beers(models.Model):
    """Favourite beers"""

    barcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    img_url = models.URLField(max_length=200)
    description = models.TextField()
    IBU = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


class Malts(models.Model):
    """Malts"""

    name = models.CharField(max_length=150, primary_key=True)
    malts_in_that_beer = models.ManyToManyField(Beers)


class Hops(models.Model):
    """Hops"""

    name = models.CharField(max_length=150, primary_key=True)
    hops_in_that_beer = models.ManyToManyField(Beers)
