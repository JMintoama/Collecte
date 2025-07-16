from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render, redirect
from gestion.models import Admin
from .utils import admin_required

# === Login views ===

def login_view(request, destination):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            admin_user = Admin.objects.get(login=username, pass_field=password, destination=destination)
            request.session['admin_logged_in'] = True
            request.session['destination'] = destination
            return redirect(f'/collecte/{destination.lower()}/')
        except Admin.DoesNotExist:
            error = "Identifiants incorrects ou accès non autorisé."

    return render(request, 'collecte/login.html', {'error': error, 'destination': destination})

def login_periodique(request):
    return login_view(request, 'Periodique')

def login_monographie(request):
    return login_view(request, 'Monographie')

def login_indexeur(request):
    return login_view(request, 'Indexeur')

from django.shortcuts import render, redirect
from gestion.models import Admin
from django.utils import admin_required

# === Login views ===

def login_view(request, destination):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            admin_user = Admin.objects.get(login=username, pass_field=password, destination=destination)
            request.session['admin_logged_in'] = True
            request.session['destination'] = destination
            return redirect(f'/collecte/{destination.lower()}/')
        except Admin.DoesNotExist:
            error = "Identifiants incorrects ou accès non autorisé."

    return render(request, 'collecte/login.html', {'error': error, 'destination': destination})

def login_periodique(request):
    return login_view(request, 'Periodique')

def login_monographie(request):
    return login_view(request, 'Monographie')

def login_indexeur(request):
    return login_view(request, 'Indexeur')

def login_indexation(request):
    return login_view(request, 'Indexation')

def login_controle(request):
    return login_view(request, 'Controle')

def login_prisevue(request):
    return login_view(request, 'vue')

# === Protected home views ===

@admin_required('Periodique')
def periodique(request):
    return render(request, 'collecte/periodique.html')

@admin_required('Monographie')
def monographie(request):
    return render(request, 'collecte/monographie.html')

@admin_required('Indexeur')
def indexeur(request):
    return render(request, 'collecte/indexeur.html')

@admin_required('Controle')
def indexation(request):
    return render(request, 'collecte/indexation.html')

@admin_required('vue')
def prisevue(request):
    return render(request, 'collecte/vue.html')

def login_prisevue(request):
    return login_view(request, 'vue')

# === Protected home views ===

@admin_required('Periodique')
def periodique(request):
    return render(request, 'collecte/periodique.html')

@admin_required('Monographie')
def monographie(request):
    return render(request, 'collecte/monographie.html')

@admin_required('Indexeur')
def indexeur(request):
    return render(request, 'collecte/indexeur.html')

@admin_required('Indexation')
def indexation(request):
    return render(request, 'collecte/indexation.html')

@admin_required('vue')
def prisevue(request):
    return render(request, 'collecte/vue.html')


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