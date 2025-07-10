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

