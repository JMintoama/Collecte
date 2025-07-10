from django.urls import path
from . import views

urlpatterns = [
    path('', views.collecte_home, name='collecte_home'),
    path('ajouter/', views.ajouter_collecte, name='ajouter_collecte'),
]