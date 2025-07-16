from django.urls import path
from . import views

urlpatterns = [
    path('', views.collecte_home, name='collecte_home'),
    path('ajouter/', views.ajouter_collecte, name='ajouter_collecte'),

    # Logins pour chaque sous-partie
    path('periodique/login/', views.login_periodique, name='login_periodique'),
    path('monographie/login/', views.login_monographie, name='login_monographie'),
    path('indexeur/login/', views.login_indexeur, name='login_indexeur'),
    path('indexation/login/', views.login_indexation, name='login_indexation'),
    path('vue/login/', views.login_prisevue, name='login_vue'),
    path('controle/login/', views.login_controle, name='login_controle'),
    # Home protégée
    path('periodique/', views.periodique, name='periodique'),
    path('monographique/', views.monographique, name='monographique'),
    path('indexeur/', views.indexeur, name='indexeur'),
    path('indexation/', views.indexation, name='indexation'),
    path('controle/', views.controle, name='controle'),
    path('vue/', views.vue, name='vue'),
]