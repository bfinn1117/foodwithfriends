from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("setPreferences", views.set_preferences, name="setPreferences"),
    path("searchResults", views.search_users, name="searchResults"),
    path("comparePreferences", views.compare_preferences, name="comparePreferences")
]