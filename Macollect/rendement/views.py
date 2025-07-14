from django.shortcuts import render

# Create your views here.
def rendement_home(request):
    """
    View function for the home page of the Rendement app.
    """
    return render(request, 'rendement/home.html')  

def controle_rendement(request):
    """
    View function for the control rendement page.
    """
    return render(request, 'rendement/control_rendement.html')

def comparaison_rendement(request):
    """
    View function for the comparison rendement page.
    """
    return render(request, 'rendement/comparison_rendement.html')
