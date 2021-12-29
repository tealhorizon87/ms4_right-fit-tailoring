from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view to display the cart contents """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """ A view to add a quantity of the same item to the cart """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(
                    request,
                    f"Updated quantity of {product.name} with size {size.upper()}")
            else:
                cart[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request,
                    f"Added size {size.upper()} of {product.name} to your cart")
        else:
            cart[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request, f"Added size {size.upper()} of {product.name} to your cart")
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f"Updated the quantity of{product.name}")
        else:
            cart[item_id] = quantity
            messages.success(request, f"Added {product.name} to your cart")

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
            messages.success(request, f"{product.name} in size {size.upper()} updated")
        else:
            del cart[item_id]["items_by_size"][size]
            messages.success(request, f"Removed size {size.upper()} {product.name} from your cart")
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f"{product.name} updated")
        else:
            cart.pop(item_id)
            messages.success(request, f"Removed {product.name} from your cart")

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
        messages.success(request, f"Removed size {size.upper()} {product.name} from your cart")
    else:
        cart.pop(item_id)
        messages.success(request, f"Removed {product.name} from your cart")

    request.session["cart"] = cart
    return redirect(reverse("cart"))
