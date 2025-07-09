from django.contrib import admin
from .models import Suivi, Suiveur, Vue

# Register your models here.
admin.site.register(Suivi)
admin.site.register(Suiveur)    
admin.site.register(Vue)