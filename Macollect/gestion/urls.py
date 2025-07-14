from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestion_home, name='gestion_home'),
    path('index_doc/', views.index_doc, name='index_doc'),
    path('ajouter_source/', views.ajouter_source, name='ajouter_source'),
    path('supprimer_source/', views.supprimer_source, name='supprimer_source'),
    path('ajouter_domaine/', views.ajouter_domaine, name='ajouter_domaine'),
    path('supprimer_domaine/', views.supprimer_domaine, name='supprimer_domaine'),
]