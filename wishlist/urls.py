from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlist, name="wishlist"),
    path("wishlist_add/<item_id>/", views.add_to_wishlist, name="wishlist_add"),
]
