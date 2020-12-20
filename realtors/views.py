from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from listings.models import  Listing
from .forms import CreateRealtorForm
from . models import Realtor


def RealtorCreateView(request):
	if request.method == 'POST':
		user_id = request.user.id
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		description = request.POST['description']
		photo = request.FILES['photo']
		realtor = Realtor(user_id=user_id,name=name, email=email, phone=phone, description=description, photo=photo)
		realtor.save()
		return redirect(reverse('realtors'))
	return render(request, 'realtors/realtor_form.html')


def RealtorsListView(request):
	realtors = Realtor.objects.filter(user_id=request.user.id)

	context = {
		'realtors': realtors,
		}

	return render(request, 'realtors/realtor_list.html', context=context)


def RealtorDetailView(request, realtor_id, *args, **kwargs):
	realtor = Realtor.objects.get(pk=realtor_id)
	listings = Listing.objects.filter(realtor=realtor)
	context = {
		'realtor': realtor,
		'listings': listings,

	}

	return render(request, 'realtors/realtor_detail.html', context=context)


