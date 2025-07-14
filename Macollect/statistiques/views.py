from django.shortcuts import render

# Create your views here.
def statistiques_home(request):
    """
    View function for the home page of the Statistiques app.
    """
    return render(request, 'statistiques/home.html')

def statistiques(request):
    """
    View function for the statistiques page.
    """
    return render(request, 'statistiques/statistiques.html')