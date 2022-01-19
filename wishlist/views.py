from django.shortcuts import render


def wishlist(request):
    context = {
    
    }
    return render(request, "wishlist/wishlist.html", context)
