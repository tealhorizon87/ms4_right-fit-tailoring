from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlist, name="wishlist"),
    path("wishlist_add/<item_id>/", views.add_to_wishlist, name="wishlist_add"),
    path("wishlist_remove/<item_id>/", views.remove_from_wishlist, name="wishlist_remove"),
]
