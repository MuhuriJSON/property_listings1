from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Owner(models.Model):
	user_id = models.IntegerField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	trading_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	address = models.CharField(max_length=200)

	def __str__(self):
		return self.trading_name


class Property(models.Model):
	
	STYLE_CHOICES = [('Apart','Apartment'),
					 	('Bung','Bungalow'),
					 	('Mans','Mansionnete'),
					 	('Comm','Commercial'),
					]
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	style = models.CharField(max_length=100, choices=STYLE_CHOICES)
	bedrooms = models.IntegerField()
	bathrooms = models.IntegerField()
	parking = models.BooleanField(default=True)
	sqft = models.IntegerField()
	address = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)


	def __str__(self):
		return self.name

		

class PropertyUnit(models.Model):
	unit_code = models.CharField(max_length=6, unique=True)
	property_name = models.CharField(max_length=250)
	rental_rate = models.IntegerField()
	recurrent_charges = models.IntegerField()
	lease_status = models.BooleanField(default=False)
	description = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return self.unit_code



class Tenant(models.Model):

	user_id = models.IntegerField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=50)
	email = models.EmailField(unique=True)

	def __str__(self):
		return str(self.first_name + ' ' + self.last_name)



class Lease(models.Model):
	unit_code = models.CharField(max_length=6)
	tenant_names = models.CharField(max_length=50)
	lease_term = models.IntegerField()
	lease_start = models.DateTimeField()
	lease_end = models.DateTimeField()


	def __str(self):
		return str(self.unit_code + ' ' + self.tenant_names)
