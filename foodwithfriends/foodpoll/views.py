from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q

from .models import User, Cuisine, Location, Price, Preference

# Create your views here.

def index(request):
    if request.method == "GET":
        return render(request, "foodpoll/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "foodpoll/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "foodpoll/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "foodpoll/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "foodpoll/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "foodpoll/register.html")

def set_preferences(request):
    if request.method == "GET":
        # collect all model data to be displayed
        allCuisines = Cuisine.objects.all()
        allLocations = Location.objects.all()
        allPrices = Price.objects.all()
        currentUser = request.user
        userPreference = Preference.objects.filter(owner=currentUser).last()
        return render (request, "foodpoll/setpreferences.html", {
            "locations": allLocations,
            "cuisines": allCuisines,
            "prices": allPrices,
            "preferences": userPreference
        })
    else:
        # get new data from form submission
        location = request.POST["location"]
        pref1 = request.POST["pref1"]
        pref2 = request.POST["pref2"]
        pref3 = request.POST["pref3"]
        price = request.POST["price"]
        # which user?
        currentUser = request.user

        # making queries: https://docs.djangoproject.com/en/4.1/topics/db/queries/ 
        locationData = Location.objects.get(locationName=location)
        pref1Data = Cuisine.objects.get(cuisineName=pref1)
        pref2Data = Cuisine.objects.get(cuisineName=pref2)
        pref3Data = Cuisine.objects.get(cuisineName=pref3)
        priceData = Price.objects.get(priceRange=price)

        # create new user preference
        userPreference = Preference(
            owner=currentUser,
            location=locationData,
            pref1=pref1Data,
            pref2=pref2Data,
            pref3=pref3Data,
            price=priceData
        )
        # insert object in db
        userPreference.save()
        return HttpResponseRedirect(reverse(index))

def search_users(request, *args, **kwargs):
    # reference: https://linuxhint.com/build-a-basic-search-for-a-django/
    results = []
    if request.method == "GET":
        query = request.GET.get('invitedUser')
        if query ==  '':
            query = 'None'
        results = User.objects.filter(username__icontains=query)

    return render(request, 'foodpoll/searchResults.html', {
        'query': query, 
        'results': results
        })

def compare_preferences(request):
    if request.method == 'GET':
        currentUser = request.user
    else:
        invitedUser = request.POST['invitedUser']
        currentUser = request.user

        # get invited users preferene
        invitedUserPreference = Preference.objects.filter(owner=invitedUser).last()

        # get current users preference
        currentUserPreference = Preference.objects.filter(owner=currentUser).last()

        # location compare
        loc1 = invitedUserPreference.location
        loc2 = currentUserPreference.location

        if loc1 == loc2:
            locationMatch = loc1
        else:
            locationMatch = "No match"

        # pref 1
        pref1Invited = invitedUserPreference.pref1
        pref1Current = currentUserPreference.pref1

        # pref 2
        pref2Invited = invitedUserPreference.pref2
        pref2Current = currentUserPreference.pref2

        # pref 3
        pref3Invited = invitedUserPreference.pref3
        pref3Current = currentUserPreference.pref3

        # price - pass as context
        priceInvited = invitedUserPreference.price
        priceCurrent = currentUserPreference.price
        
        # pass as context
        cuisineMatches = []

        # compare the preferences of all 3 options
        if pref1Invited == pref1Current:
            cuisineMatches.append(pref1Invited)
        elif pref1Invited == pref2Current:
            cuisineMatches.append(pref1Invited)
        elif pref1Invited == pref3Current:
            cuisineMatches.append(pref1Invited)

        if pref2Invited == pref1Current:
            cuisineMatches.append(pref2Invited)
        elif pref2Invited == pref2Current:
            cuisineMatches.append(pref2Invited)
        elif pref2Invited == pref3Current:
            cuisineMatches.append(pref2Invited)

        if pref3Invited == pref1Current:
            cuisineMatches.append(pref3Invited)
        elif pref3Invited == pref2Current:
            cuisineMatches.append(pref3Invited)
        elif pref3Invited == pref3Current:
            cuisineMatches.append(pref3Invited)


    return render(request, 'foodpoll/comparePreferences.html', {
        "priceInvited": priceInvited,
        "priceCurrent": priceCurrent,
        "locationMatch": locationMatch,
        "cuisineMatches": cuisineMatches
    })