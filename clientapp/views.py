from django.shortcuts import render

def home(request):
    """
    View function for the homepage.

    This function renders the 'index.html' template,
    which represents the homepage of the CRM application.
    """
    return render(request, 'clientapp/index.html')
