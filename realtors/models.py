from django.db import models
from datetime import datetime

# Create your models here.


class Realtor(models.Model):

	user_id = models.IntegerField()
	name = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
	description = models.TextField(blank=True)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	is_mvr = models.BooleanField(default=False, blank=True)
	hire_date = models.DateTimeField(default=datetime.now, blank=True)


	def __str__(self):
		return self.name
