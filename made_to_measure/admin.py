from django.contrib import admin
from .models import MtmOrder


class MtmOrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "name",
        "email",
        "product",
        "order_total",
    )

admin.site.register(MtmOrder, MtmOrderAdmin)
