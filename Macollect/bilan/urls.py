from django.urls import path
from . import views

urlpatterns = [
    path('', views.bilan_home, name='bilan_home'),
    # Add more URL patterns as needed for the collecte app
]