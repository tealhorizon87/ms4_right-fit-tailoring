from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


def made_to_measure(request):
    """ A view to display the made to measure form """

    products = Product.objects.all()

    if "category" in request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__category_name__in=categories)

    context = {
        "products": products,
    }

    return render(request, "made_to_measure/made_to_measure.html", context)
