from django.shortcuts import render

# Create your views here.
def recherche_home(request):
    """
    View function for the home page of the Recherche app.
    """
    return render(request, 'recherche/home.html')