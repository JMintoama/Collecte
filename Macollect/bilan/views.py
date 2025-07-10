from django.shortcuts import render

# Create your views here.
def bilan_home(request):
    """
    View function for the home page of the Bilan app.
    """
    return render(request, 'bilan/home.html')