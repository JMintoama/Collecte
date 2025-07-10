from django.shortcuts import render

# Create your views here.
def gestion_home(request):
    """
    View function for the home page of the Bilan app.
    """
    return render(request, 'gestion/home.html')