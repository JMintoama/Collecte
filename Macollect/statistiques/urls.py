from django.urls import path
from . import views

urlpatterns = [
    path('', views.statistiques_home, name='statistiques_home'),
    # Add more URL patterns as needed for the statistiques app
]