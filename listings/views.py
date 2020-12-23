from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.core.files.storage import FileSystemStorage
from .models import Listing
from .forms import ListingCreationForm
from realtors.models import Realtor
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, town_choices


# Create your views here.


def all_listings(request):
    listings = Listing.objects.order_by('-listing_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'town_choices':town_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing=get_object_or_404(Listing, pk=listing_id)

    context={
        'listing':listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list=Listing.objects.order_by('-listing_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
        
   #Address
    if 'address' in request.GET:
        address = request.GET['address']
        if address:
            queryset_list=queryset_list.filter(address__icontains = address)

    #Town
    if 'town' in request.GET:
        town = request.GET['town']
        if town:
            queryset_list=queryset_list.filter(town__icontains = town)
    
    
     # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__iexact=bedrooms)
        
     # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price__lte=int(price))
                
    context={
        'town_choices':town_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET,
    }

    return render(request, 'listings/search.html', context)


def CreateListingView(request, realtor_id, *args, **kwargs):
    realtor = Realtor.objects.get(pk=realtor_id)

    if request.method == "POST":

        user_id = request.user.id
        title = request.POST.get('title')
        rent_or_sale = request.POST.get('rent_or_sale')
        town = request.POST.get('town')
        sqft = request.POST.get('sqft')
        bathrooms = request.POST.get('bathrooms')
        bedrooms = request.POST.get('bedrooms')
        address = request.POST.get('address')
        description = request.POST.get('description')
        price = request.POST.get('price')
        photo_main = request.FILES['photo_main']


        listing = Listing(user_id=user_id, realtor=realtor, title=title,town=town, sqft=sqft, bathrooms=bathrooms, bedrooms=bedrooms, address=address, description=description,\
            photo_main=photo_main, price=price, rent_or_sale=rent_or_sale)
        listing.save()
        
        return redirect(reverse_lazy('realtor_detail', kwargs={'realtor_id': realtor_id}))

    context = {
        'realtor': realtor,

    }    
    return render(request, 'listings/listing_form.html', context=context)


def UserListings(request, *args, **kwargs):
    user_listings = Listing.objects.filter(user_id=request.user.id)
    context = {
        'user_listings': user_listings
    }
    return render(request, 'listings/user_listings.html', context=context)  