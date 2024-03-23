from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, AddClientForm, UpdateClientForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Client
from django.urls import reverse
from django.contrib import messages

# Homepage
def home(request):
    """
    View function for the homepage.

    This function renders the 'index.html' template,
    which represents the homepage of the CRM application.
    """
    if request.user.is_authenticated:
        return render(request, 'clientapp/index.html', {'logged_in': True})
    return render(request, 'clientapp/index.html', {'logged_in': False})

# User Registration
def register(request):
    """
    View function for user registration.

    Renders the registration form for new users.
    If the form is submitted with valid data, it saves the user and redirects to the login page.
    """
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the index page
        messages.error(request, "Please log out from the current account before creating another account!")
        return redirect('home')
    else:
        # If the user is not logged in, render the registration page
        form = RegistrationForm()

        if request.method == 'POST':
            form = RegistrationForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Your account has been created successfully!")
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
    if request.user.is_authenticated:
        # If the user is already logged in, redirect them to the index page
        messages.error(request, "You are already logged in!")
        return redirect('home')
    else:    
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
    messages.success(request, "You have been logged out successfully!")
    return redirect('user-login')

# Dashboard
@login_required(login_url='user-login')
def client_dashboard(request):
    """
    View function for rendering the client dashboard page.

    Requires user authentication; redirects to the login page if not authenticated.
    """
    clients = Client.objects.filter(user=request.user)
    context = {'clients': clients}
    return render(request, 'clientapp/client-dashboard.html', context=context)

# Add client
@login_required(login_url='user-login')
def add_client(request):
    """
    View function to handle adding a new client.
    
    Requires the user to be logged in. If the request method is POST and the form is valid,
    the client data is saved and the user is redirected to the client dashboard.
    """
    form = AddClientForm()
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user  # Associate the client with the logged-in user
            client.save()
            messages.success(request, "Client info has been added successfully!")
            return redirect('client-dashboard')
        
    context = {'form':form}
    return render(request, 'clientapp/add-client.html', context=context)

# View client details
@login_required(login_url='user-login')
def view_client(request, pk):
    """
    View function to display details of a specific client.
    """
    client = Client.objects.get(id=pk)
    context = {'client':client}
    return render(request, 'clientapp/client-details.html', context=context)

# Update client
@login_required(login_url='user-login')
def update_client(request, pk):
    """
    View function to update client details.

    If the request method is POST and the form is valid, redirects to the client details page.
    Otherwise, renders the update client form template.
    """
    client = Client.objects.get(id=pk)
    form = UpdateClientForm(instance=client)
    if request.method == 'POST':
        form = UpdateClientForm(request.POST, instance=client)
        if form.is_valid:
            client = form.save(commit=False)
            client.user = request.user  # Associate the client with the logged-in user
            client.save()
            messages.success(request, "Client info has been updated successfully!")
            return redirect(reverse('client-details', kwargs={'pk': pk}))
        
    context = {'form':form}
    return render(request, 'clientapp/update-client.html', context=context)

# Delete client
@login_required(login_url='user-login')
def delete_client(request, pk):
    """
    View function to delete client.

    Redirects to the client dashboard after deleting the client.
    """
    client = Client.objects.get(id=pk)

    # Check if the client belongs to the current user
    if client.user != request.user:
        messages.error(request, "You are not authorized to delete this client.")
        return redirect('client-dashboard')
    
    client.delete()
    messages.success(request, "Client info has been deleted successfully!")

    return redirect('client-dashboard')