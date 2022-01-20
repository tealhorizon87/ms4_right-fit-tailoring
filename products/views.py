from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to return all products page """

    products = Product.objects.all()
    query = None
    sort = None
    direction = None
    product_heading = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "category":
                sortkey = "category__category_name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, """
                    Please enter a word or phrase to search for""")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

            if not products:
                messages.error(request, """
                    Sorry, there are no products matching your search""")
                return redirect(reverse("products"))

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(
                category__category_name__in=categories)

            if len(categories) == 2:
                product_heading = f"""
                    {categories[0].title()} & {categories[1].title()}"""
            elif len(categories) == 1:
                product_heading = categories[0].title()
            else:
                product_heading = "All Products"

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_sorting": current_sorting,
        "product_heading": product_heading,
    }

    return render(request, "products/products_main.html", context)


def product_detail(request, product_id):
    """ A view to render the product details page """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product
    }

    return render(request, "products/product_detail.html", context)
