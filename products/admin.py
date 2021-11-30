from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "category_name"
    )


class ProductAdmin(admin.ModelAdmin):
    def cat_name(self, obj):
        return obj.category.friendly_name

    list_display = (
        "product_code",
        "name",
        "cat_name",
        "price",
        "image"
    )

    ordering = ("product_code",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
