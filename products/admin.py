from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "category_name"
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "name",
        "category",
        "price",
        "image"
    )

    ordering = ("product_code",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
