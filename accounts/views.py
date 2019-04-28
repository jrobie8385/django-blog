from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    '''
    The UserCreationForm class is a ModelForm (forms.ModelForm) for creating a new user.  It has three fields:
        username (from the user model),
        password1, and
        password2.
    It verifies that password1 and password2 match, validates the password using validate_password(),
    and sets the user’s password using set_password().
    To view, go to: https://github.com/django/django/blob/master/django/contrib/auth/forms.py
    '''
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")
    #use "reverse_lazy()" when providing a reversed URL as the url attribute of a generic class-based view.
    # The reason is because for all generic classbased views the URLs are not loaded when the file is imported,
    #    so we have to use the lazy form of reverse to load them later when they’re available.
