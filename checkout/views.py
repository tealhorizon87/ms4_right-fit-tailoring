from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    context = {
        "cart": cart,
    }

    return render(request, "checkout/checkout.html", context)
