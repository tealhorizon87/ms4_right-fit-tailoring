from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist, WishlistItem
from products.models import Product


@login_required
def wishlist(request):
    """ A view to display the user's wishlist """

    # Find user's wishlist or create one
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]

    context = {
        "wishlist": wishlist,
    }

    return render(request, "wishlist/wishlist.html", context)


def add_to_wishlist(request, item_id):
    """ a view to add a product to the user's wishlist """

    # Find user's wishlist or create one
    wishlist = Wishlist.objects.get_or_create(user=request.user)
    wishlist = wishlist[0]

    # Find the product and the previous url
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.META.get('HTTP_REFERER')


    # Add to wishlist if not already there
    in_wishlist = WishlistItem.objects.filter(wishlist=wishlist, product=product).exists()
    if in_wishlist:
        messages.info(request, "This item is already in your wishlist")
    else:
        wishlist.items.add(product)
        messages.success(request, "Added product to your wishlist")

    return redirect(redirect_url)
