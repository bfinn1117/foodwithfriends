from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class Cuisine(models.Model):
    cuisineName = models.CharField(max_length=20)

    def __str__(self):
        return self.cuisineName

class Location(models.Model):
    locationName = models.CharField(max_length=20)

    def __str__(self):
        return self.locationName

class Price(models.Model):
    priceRange = models.CharField(max_length=20)

    def __str__(self):
        return self.priceRange

class Preference(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True, related_name="location")
    pref1 = models.ForeignKey(Cuisine, on_delete=models.CASCADE, blank=True, null=True, related_name="pref1")
    pref2 = models.ForeignKey(Cuisine, on_delete=models.CASCADE, blank=True, null=True, related_name="pref2")
    pref3 = models.ForeignKey(Cuisine, on_delete=models.CASCADE, blank=True, null=True, related_name="pref3")
    price = models.ForeignKey(Price, on_delete=models.CASCADE, blank=True, null=True, related_name="price")

    def __str__(self):
        return self.owner
