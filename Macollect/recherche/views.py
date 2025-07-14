from django.shortcuts import render

# Create your views here.
def recherche_home(request):
    """
    View function for the home page of the Recherche app.
    """
    return render(request, 'recherche/home.html')

def recherche_web(request):
    """
    View function for the web search page of the Recherche app.
    """
    return render(request, 'recherche/web.html')

def recherche_csv(request):
    """
    View function for the CSS search page of the Recherche app.
    """
    return render(request, 'recherche/css.html')
