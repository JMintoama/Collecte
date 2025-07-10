from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion_home, name='gestion_home'),
    # Add more URL patterns as needed for the collecte app
]