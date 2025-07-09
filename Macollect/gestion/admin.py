from django.contrib import admin
from .models import Doc, Domaine, Editeur,Edition, Auteur, Ecriture, Depot, Source, Fournit,Admin

# Register your models here.
admin.site.register(Doc)
admin.site.register(Domaine)
admin.site.register(Editeur)
admin.site.register(Edition)
admin.site.register(Auteur)
admin.site.register(Ecriture)
admin.site.register(Depot)
admin.site.register(Source)
admin.site.register(Fournit)
admin.site.register(Admin)