from django.db import models

# Create your models here.





class Owner(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	trading_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=50)
	email = models.EmailField()
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
	garage = models.BooleanField(default=True)
	parking = models.BooleanField(default=True)
	sqft = models.IntegerField()
	address = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='photos/%Y/%m/%d')


	def __str__(self):
		return self.name


