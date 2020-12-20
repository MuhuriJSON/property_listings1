"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from property_agency.views import CreateOwnerView, OwnersListView,OwnerDetailView, CreatePropertyView,\
                                    CreateTenantView, TenantListView
from realtors import views as realtor_views 
from property_agency import views as agency_views
from listings import views as listing_views


urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('', include('pages.urls')),

    path('listings/', include('listings.urls')),

    path('accounts/', include('accounts.urls')),

    path('contacts/', include('contacts.urls')),

    #owners urls
    path('owners/', agency_views.OwnersListView, name='owners'),
    path('owners/create_owner/', agency_views.CreateOwnerView, name='create_owner'),
    path('owners/<int:owner_id>/', agency_views.OwnerDetailView, name='owner_detail'),
    path('owners/<int:owner_id>/create_property/', agency_views.CreatePropertyView, name='create_property'),
    
    #properties urls
    path('properties/<int:property_id>/', agency_views.PropertyDetailView, name='property_detail'),


    #units urls
    path('properties/property_detail/create_unit/<int:property_id>/', agency_views.CreateUnitView, name='create_unit'),
    path('properties/property_detail/<int:unit_id>/', agency_views.UnitDetailView, name='unit_detail'),
    path('properties/property_detail/unit_detail/lease_unit/<int:unit_id>/', agency_views.CreateUnitLeaseView, name='lease_unit'),
    
    #tenants urls
    path('tenants/', agency_views.TenantListView, name='tenants'),
    path('tenants/create_tenant/', agency_views.CreateTenantView, name='create_tenant'),
    path('tenants/<int:tenant_id>/', agency_views.TenantDetailView, name='tenant_detail'),
    
    #realtors urls
    path('realtors/', realtor_views.RealtorsListView, name='realtors'),
    path('realtors/create_realtor/', realtor_views.RealtorCreateView, name='create_realtor'),
    path('realtors/<int:realtor_id>/', realtor_views.RealtorDetailView, name='realtor_detail'),
    path('realtors/<int:realtor_id>/create_listing/', listing_views.CreateListingView, name='create_listing'),

] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)