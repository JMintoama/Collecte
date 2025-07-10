from django.urls import path
from . import views

urlpatterns = [
    path('', views.recherche_home, name='recherche_home'),
    # Add more URL patterns as needed for the recherche app
]