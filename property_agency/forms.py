from django.forms import ModelForm
from .models import Property, Owner, PropertyUnit,Tenant, Lease
from django import forms



class PropertyForm(forms.ModelForm):
	name = forms.CharField(max_length=30, widget=forms.TextInput())
	owner = forms.ModelChoiceField(queryset=Owner.objects.all())

	class Meta:
		model= Property
		fields = ['name', 'owner', 'style', 'bedrooms', 'bathrooms', 'parking', 'sqft', 'address', 'description', 'image']


class PropertyUnitForm(forms.ModelForm):
	property = forms.ModelChoiceField(queryset=Property.objects.all())

	class Meta:
		model = PropertyUnit
		fields = ['property', 'unit_code', 'rental_rate', 'recurrent_charges', 'description']


class LeaseCreationForm(forms.Form):
	
	unit_code = forms.ModelChoiceField(queryset=PropertyUnit.objects.all())
	property = forms.ModelChoiceField(queryset=Property.objects.all())
	tenant_names = forms.ModelChoiceField(queryset=Tenant.objects.all())
	lease_term = forms.IntegerField()
	lease_start = forms.DateField()
	lease_end = forms.DateField()



