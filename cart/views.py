from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view to display the cart contents """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """ A view to add a quantity of the same item to the cart """

    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    cart = request.session.get("cart", {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]["items_by_size"].keys():
                cart[item_id]["items_by_size"][size] += quantity
            else:
                cart[item_id]["items_by_size"][size] = quantity
        else:
            cart[item_id] = {"items_by_size": {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session["cart"] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ A view to update the quantity of the same item to the cart """

    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    cart = request.session.get("cart", {})

    if size:
        if quantity > 0:
            cart[item_id]["items_by_size"][size] = quantity
            messages.success(request, "Item updated")
        else:
            del cart[item_id]["items_by_size"][size]
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, "Item updated")
        else:
            cart.pop(item_id)

    request.session["cart"] = cart
    return redirect(reverse("cart"))


def remove_from_cart(request, item_id):
    """ A view to remove the entire item from the cart """

    product = get_object_or_404(Product, pk=item_id)
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    cart = request.session.get("cart", {})

    if size:
        del cart[item_id]["items_by_size"][size]
    else:
        cart.pop(item_id)

    request.session["cart"] = cart
    return redirect(reverse("cart"))
