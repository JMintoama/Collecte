from django.shortcuts import render

# Create your views here.
def bilan_home(request):
    """
    View function for the home page of the Bilan app.
    """
    return render(request, 'bilan/home.html')

def doc_list(request):
    """
    View function to list documents.
    """
    # Placeholder for document listing logic
    documents = []  # This should be replaced with actual document retrieval logic
    return render(request, 'bilan/doc_list.html', {'documents': documents})

def etablishment_list(request):
    """
    View function to list establishments.
    """
    # Placeholder for establishment listing logic
    establishments = []  # This should be replaced with actual establishment retrieval logic
    return render(request, 'bilan/establishment_list.html', {'establishments': establishments})
