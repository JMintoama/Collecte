from django.urls import path
from . import views

urlpatterns = [
    path('', views.bilan_home, name='bilan_home'),
    path('documents/', views.doc_list, name='doc_list'),
    path('etablissements/', views.etablishment_list, name='establishment_list'),
]

