from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

"""

I adjusted the user model:
    - I added a new field called "email" to the user model.
    - I changed the USERNAME_FIELD to "email".
    
    - Need to make some adjustments to views.py to reflect the changes to the user model.
        from django.contrib.auth import get_user_model
        User = get_user_model()
        
        This will give us the active user model.

"""

from django.contrib.auth import get_user_model

User = get_user_model()


def logout_view(request):
    pass


def login_view(request):
    """login_view

    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            ...
            request.session['username'] = email
    """
    pass
