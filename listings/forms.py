from django.forms import ModelForm
from . models import Listing


class ListingCreationForm(ModelForm):

	class Meta:
		model  = Listing
		fields = ['title','rent_or_sale','price', 'bathrooms', 'bedrooms','sqft', 'address', 'description',  'photo_main']