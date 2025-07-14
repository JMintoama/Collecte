from django.shortcuts import render

# Create your views here.
def gestion_home(request):
    """
    View function for the home page of the Bilan app.
    """
    return render(request, 'gestion/home.html')

def index_doc(request):
    """
    View function for the document index page.
    """
    return render(request, 'gestion/index_doc.html')

def ajouter_source(request):
    """
    View function for adding an orgin.
    """
    return render(request, 'gestion/ajouter_source.html')

def supprimer_source(request):
    """
    View function for deleting an orgin.
    """
    return render(request, 'gestion/supprimer_source.html')

def ajouter_domaine(request):
    """
    View function for adding a domain.
    """
    return render(request, 'gestion/ajouter_domaine.html')

def supprimer_domaine(request):
    """
    View function for deleting a domain.
    """
    return render(request, 'gestion/supprimer_domaine.html')
