from django.shortcuts import render

# Create your views here.
def rendement_home(request):
    """
    View function for the home page of the Rendement app.
    """
    return render(request, 'rendement/home.html')  