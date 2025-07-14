from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.decorators import login_required

# Create your views here.
def collecte_home(request):
    """
    View function for the home page of the Collecte app.
    """
    return render(request, 'collecte/home.html')


from .forms import CollecteForm
def ajouter_collecte(request):
    """
    View function to handle the collection of data.
    """
    if request.method == 'POST':
        form = CollecteForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            return redirect('collecte_home')  # Redirect to the home page after saving
    else:
        form = CollecteForm()
    
    return render(request, 'collecte/ajouter.html', {'form': form})

def periodique(request):
    """
    View function to handle periodic data collection.
    """
    # Logic for periodic data collection can be added here
    return render(request, 'collecte/periodique.html')

def monographique(request):
    """
    View function to handle monographic data collection.
    """
    # Logic for monographic data collection can be added here
    return render(request, 'collecte/monographique.html')

def indexeur(request):
    """
    View function to handle indexing of data.
    """
    # Logic for indexing data can be added here
    return render(request, 'collecte/indexeur.html')

def indexation(request):
    """
    View function to handle the indexing of collected data.
    """
    # Logic for indexing collected data can be added here
    return render(request, 'collecte/indexation.html')

def controle(request):
    """
    View function to handle the control of collected data.
    """
    # Logic for controlling collected data can be added here
    return render(request, 'collecte/controle.html')

def vue(request):
    """
    View function to handle the view of collected data.
    """
    # Logic for viewing collected data can be added here
    return render(request, 'collecte/vue.html')

