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

    wishlist_items = list(wishlist.items.all())
    print(wishlist_items)
    context = {
        "wishlist": wishlist,
        "wishlist_items": wishlist_items
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
    in_wishlist = WishlistItem.objects.filter(wishlist=wishlist,
                                              product=product).exists()
    if in_wishlist:
        messages.info(request, "This item is already in your wishlist")
    else:
        wishlist.items.add(product)
        messages.info(request, "Added product to your wishlist")

    return redirect(redirect_url)


@login_required
def remove_from_wishlist(request, item_id):
    wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=item_id)

    wishlist.items.remove(product)

    messages.info(request, "Item succeffully removed from wishlist")

    return redirect(reverse("wishlist"))
