from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Client

# Homepage
def home(request):
    """
    View function for the homepage.

    This function renders the 'index.html' template,
    which represents the homepage of the CRM application.
    """
    return render(request, 'clientapp/index.html')

# User Registration
def register(request):
    """
    View function for user registration.

    Renders the registration form for new users.
    If the form is submitted with valid data, it saves the user and redirects to the login page.
    """
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('user-login')
    
    context = {'form':form}
    return render(request, 'clientapp/register.html', context=context)

# User Login
def user_login(request):
    """
    View function for user login.

    Renders the login form for existing users.
    If the form is submitted with valid credentials, it authenticates the user and logs them in.
    """
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('client-dashboard')

    context = {'form':form}
    return render(request, 'clientapp/user-login.html', context=context)

# User Logout
def user_logout(request):
    """
    View function for user logout.

    Logs out the currently logged-in user and redirects to the login page.
    """
    auth.logout(request)
    return redirect('user-login')

# Dashboard
@login_required(login_url='user-login')
def client_dashboard(request):
    """
    View function for rendering the client dashboard page.

    Requires user authentication; redirects to the login page if not authenticated.
    """
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clientapp/client-dashboard.html', context=context)