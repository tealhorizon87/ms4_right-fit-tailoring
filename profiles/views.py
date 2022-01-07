from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order


def profile(request):
    return render(request, "profiles/profile.html")
