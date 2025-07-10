from django import forms
from .models import Collecte

class CollecteForm(forms.ModelForm):
    class Meta:
        model = Collecte
        fields = ['nomrc', 'n_enregistrement']
        labels = {
            'nomrc': 'Nom ',
            'n_enregistrement': 'numéro d\'enregistrement',
            
        }