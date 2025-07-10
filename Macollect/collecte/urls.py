from django.urls import path
from . import views

urlpatterns = [
    path('', views.collecte_home, name='collecte_home'),
    # Add more URL patterns as needed for the collecte app
]