from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def all_products(request):
    """ A view to return all products page """

    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products_main.html", context)


def product_detail(request, product_id):
    """ A view to render the product details page """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product
    }

    return render(request, "products/product_detail.html", context)
