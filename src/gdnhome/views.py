from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home_view(request):
    return render(request, "pages/home.html", {})
