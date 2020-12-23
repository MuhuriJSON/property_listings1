from django.db import models
from datetime import datetime
from realtors.models import Realtor


# Create your models here.

class Listing(models.Model):

    user_id = models.IntegerField()
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    town = models.CharField(max_length=30, blank=True)
    rent_or_sale = models.CharField(max_length=4, blank=True, default='Rent')
    price = models.IntegerField(blank=True)
    address = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    garage = models.BooleanField(default=True)
    sqft = models.IntegerField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    listing_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
