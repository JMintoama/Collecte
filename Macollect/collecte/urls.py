from django.urls import path
from . import views

urlpatterns = [
    path('', views.collecte_home, name='collecte_home'),
    path('ajouter/', views.ajouter_collecte, name='ajouter_collecte'),
    path('periodique/', views.periodique, name='periodique'),
    path('monographique/', views.monographique, name='monographique'),
    path('indexeur/', views.indexeur, name='indexeur'),
    path('indexation/', views.indexation, name='indexation'),
    path('controle/', views.controle, name='controle'),
    path('vue/', views.vue, name='vue'),
]