from django.contrib import admin
from .models import Owner, Property

# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
	pass

class PropertyAdmin(admin.ModelAdmin):
	pass


admin.site.register(Owner, OwnerAdmin)
admin.site.register(Property,PropertyAdmin )