
from django import forms


class CreateRealtorForm(forms.Form):
	name = forms.CharField(label='Realtor name', max_length=100)
	photo = forms.ImageField()
	phone = forms.IntegerField()
	email = forms.EmailField()
