from django.db import models
from products.models import Product
import uuid


class MtmOrder(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    height = models.CharField(max_length=3, null=True, blank=True)
    neck = models.CharField(max_length=3, null=True, blank=True)
    shoulder = models.CharField(max_length=3, null=True, blank=True)
    chest = models.CharField(max_length=3, null=True, blank=True)
    arm = models.CharField(max_length=3, null=True, blank=True)
    back = models.CharField(max_length=3, null=True, blank=True)
    waist = models.CharField(max_length=3, null=True, blank=True)
    hips = models.CharField(max_length=3, null=True, blank=True)
    leg = models.CharField(max_length=3, null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    garment = models.CharField(max_length=20, null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
