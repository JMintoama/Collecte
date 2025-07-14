from django.urls import path
from . import views

urlpatterns = [
    path('', views.rendement_home, name='rendement_home'),
    path('controle/', views.controle_rendement, name='controle_rendement'),
    path('comparaison/', views.comparaison_rendement, name='comparaison_rendement'),
]