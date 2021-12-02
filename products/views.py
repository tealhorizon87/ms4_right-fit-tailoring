from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    """ A view to return all products page """

    products = Product.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Please enter a word or phrase to search for")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__category_name__in=categories)

    context = {
        "products": products,
        "search_term": query,
    }

    return render(request, "products/products_main.html", context)


def product_detail(request, product_id):
    """ A view to render the product details page """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product
    }

    return render(request, "products/product_detail.html", context)
