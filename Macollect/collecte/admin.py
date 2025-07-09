from django.contrib import admin
from .models import Collecte, Indexation, Indexeur

# Register your models here.
admin.site.register(Collecte)  
admin.site.register(Indexation)
admin.site.register(Indexeur)