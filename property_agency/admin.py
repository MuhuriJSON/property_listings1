from django.contrib import admin
from .models import Owner, Property, PropertyUnit, Tenant

# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
	pass

class PropertyAdmin(admin.ModelAdmin):
	pass


class TenantAdmin(admin.ModelAdmin):
	pass

class PropertyUnitAdmin(admin.ModelAdmin):
	pass

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(Tenant,TenantAdmin)
admin.site.register(PropertyUnit, PropertyUnitAdmin)