from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product


class Wishlist(models.Model):
    user = models.OneToOneField(User, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name="wishlist")
    items = models.ManyToManyField(Product, through="WishlistItem",
                                   related_name="wishlist_items")

    def __str__(self):
        return f"{self.user}'s wishlist"


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False,
                                 on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
