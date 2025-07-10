from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def collecte_home(request):
    """
    View function for the home page of the Collecte app.
    """
    return render(request, 'collecte/home.html')

