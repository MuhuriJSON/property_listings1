from django.urls import path
from . import views
# listings
urlpatterns = [
    path('', views.all_listings, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('user_listings/', views.UserListings, name='my_listings'),
]
