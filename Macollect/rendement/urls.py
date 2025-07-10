from django.urls import path
from . import views

urlpatterns = [
    path('', views.rendement_home, name='rendement_home'),
    # Add more URL patterns as needed for the rendement app
]