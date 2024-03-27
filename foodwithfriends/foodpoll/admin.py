from django.contrib import admin
from .models import User, Location, Cuisine, Price, Preference

# Register your models here.
admin.site.register(Location)
admin.site.register(Cuisine)
admin.site.register(Price)
admin.site.register(Preference)
admin.site.register(User)