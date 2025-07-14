from django.urls import path
from . import views

urlpatterns = [
    path('', views.statistiques_home, name='statistiques_home'),
    path('statistiques/', views.statistiques, name='statistiques'),
]