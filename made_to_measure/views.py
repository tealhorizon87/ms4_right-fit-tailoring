from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product


def made_to_measure(request):
    """ A view to display the made to measure form """
    print(request.GET)
    products = Product.objects.all()
    garment = request.GET["garment"]

    if "category" in request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__category_name__in=categories)

    context = {
        "products": products,
        "garment": garment,
    }

    return render(request, "made_to_measure/made_to_measure.html", context)


def mtm_form(request, product_id):
    """ A view to display and process the made to measure form """

    product = get_object_or_404(Product, pk=product_id)
    mtm_price = product.price * 3

    context = {
        "product": product,
        "mtm_price": mtm_price,
    }

    return render(request, "made_to_measure/mtm_form.html", context)
