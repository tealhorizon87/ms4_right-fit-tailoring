from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile


def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        "profile": profile,
    }
    return render(request, "profiles/profile.html", context)
