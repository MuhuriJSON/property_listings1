from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from property_agency.models import Owner, Property,PropertyUnit, Tenant, Lease
from .forms import PropertyForm, PropertyUnitForm, LeaseCreationForm


# Create your views here.
def CreateOwnerView(request):
	if request.method == "POST":
		user_id = request.user.id
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		trading_name = request.POST['trading_name']
		email = request.POST['email']
		phone = request.POST['phone']
		address = request.POST['address']
		
		new_owner = Owner(user_id=user_id, first_name=first_name, last_name=last_name, trading_name=trading_name, email=email, phone=phone,\
			address=address)
		new_owner.save()
		return redirect(reverse('owners'))

	return render(request, 'property_agency/owner_form.html')	


def OwnersListView(request):
	owners = Owner.objects.filter(user_id=request.user.id)
	context = {
		'owners': owners
	}
	return render(request, 'property_agency/owner_list.html', context=context)

def OwnerDetailView(request, owner_id,*args, **kwargs):
	owner = Owner.objects.get(pk=owner_id)
	properties = Property.objects.filter(owner=owner)
	context = {
		'owner': owner,
		'properties': properties
	}
	return render(request, 'property_agency/owner_detail.html', context=context)


def CreatePropertyView(request, owner_id, *args, **kwargs):
	owner = Owner.objects.get(pk=owner_id)
	if request.method == "POST":
		name = request.POST['name']
		style = request.POST['style']
		bedrooms = request.POST['bedrooms']
		bathrooms = request.POST['bathrooms']
		sqft = request.POST['sqft']
		address = request.POST['address']
		description = request.POST['description']
		image = request.FILES['image']

		new_property = Property(owner=owner, name=name, style=style, bedrooms=bedrooms, bathrooms=bathrooms,\
			sqft=sqft, address=address, description=description, image=image)
		new_property.save()
		return redirect(reverse_lazy('owner_detail', kwargs={'owner_id': owner_id}))

	context = {
		'owner': owner,
	}	
	return render(request, 'property_agency/property_form.html',context=context)



def PropertyDetailView(request, property_id, *args, **kwargs):
	property = Property.objects.get(pk=property_id)
	units = PropertyUnit.objects.filter(property_name=property)
	context = {
		'property': property,
		'units': units
	}
	return render(request, 'property_agency/property_detail.html', context=context)
	

def CreateUnitView(request, property_id, *args, **kwargs):
	property = Property.objects.get(pk=property_id)	
	if request.method == "POST":
		unit_code = request.POST.get('unit_code')
		property_name = request.POST.get('property_name')
		rental_rate = request.POST.get('rental_rate')
		recurrent_charges = request.POST.get('recurrent_charges')
		description = request.POST.get('description')

		new_unit = PropertyUnit(unit_code=unit_code,property_name=property.name, rental_rate=rental_rate, recurrent_charges=recurrent_charges, description=description)
		new_unit.save()
		return redirect(reverse_lazy('property_detail',kwargs={'property_id': property_id}))

	
	context = {
				'form': PropertyUnitForm(),
				'property': property,
			  }

	return render(request, 'property_agency/unit_form.html', context=context)


def UnitDetailView(request, unit_id, *args, **kwargs):
	unit = PropertyUnit.objects.get(pk=unit_id)
	leases = Lease.objects.filter(unit_code=unit.unit_code)
	context = {
		'unit': unit,
		'leases': leases
	}
	return render(request, 'property_agency/unit_detail.html', context=context)



def CreateTenantView(request):
	if request.method == "POST":
		user_id = request.user.id
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		tenant = Tenant.objects.create(user_id=user_id,first_name=first_name, last_name=last_name, email=email, phone=phone)
		tenant.save()
		return redirect(reverse('tenants'))
	return render(request, 'property_agency/tenant_form.html')



def TenantListView(request):
	tenants = Tenant.objects.filter(user_id=request.user.id)
	context = {
		'tenants': tenants,
		}
	return render(request, 'property_agency/tenant_list.html', context=context)


def TenantDetailView(request, tenant_id, *args, **kwargs):
	tenant = Tenant.objects.get(pk=tenant_id)
	print(tenant)
	context = {
		'tenant': tenant,
	}

	return render(request, 'property_agency/tenant_detail.html', context=context)


def CreateUnitLeaseView(request, unit_id, *args, **kwargs):
	unit = PropertyUnit.objects.get(pk=unit_id)
	tenants = Tenant.objects.all()
	properties = Property.objects.all()
	leases = Lease.objects.all()
	if request.method == "POST":
		
		unit_code = request.POST['unit_code']
		property_name = request.POST.get('property_name')
		tenant_names = request.POST.get('tenant_names')
		lease_term = request.POST['lease_term']
		lease_start = request.POST.get('lease_start')
		lease_end = request.POST.get('lease_end')
		lease = Lease.objects.create(unit_code=unit_code, tenant_names=tenant_names, lease_term=lease_term,lease_start=lease_start, lease_end=lease_end)
		lease.save()
		
		unit.lease_status = True
		unit.save()

		return redirect(reverse('unit_detail' ,kwargs={'unit_id': unit_id}))

	context = {
				'unit': unit, 
				'tenants': tenants, 
				'leases': leases,
				'properties': properties,

				}	
	return render(request, 'property_agency/lease_form.html', context=context)