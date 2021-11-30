from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    category_name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.category_name


    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    product_code = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField()
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name
