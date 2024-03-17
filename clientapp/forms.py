from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Custom registration form that inherits from UserCreationForm
class RegistrationForm(UserCreationForm):
    class Meta:
        # Specify the model for the form, which is the built-in User model
        model = User
        # Define the fields to be included in the form
        fields = ['username', 'password1', 'password2']

# Custom login form that inherits from AuthenticationForm
class LoginForm(AuthenticationForm):
    # Customize the fields to use widgets
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())