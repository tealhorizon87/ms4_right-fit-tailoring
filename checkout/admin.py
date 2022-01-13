from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ("order_number", "date", "grand_total",
                       "original_cart", "stripe_pid")

    fields = ("order_number", "date", "full_name", "email",
              "phone_number", "address_line_1", "address_line_2",
              "city", "county", "postcode", "country",
              "grand_total", "original_cart", "stripe_pid")

    list_display = ("order_number", "date", "full_name", "grand_total")

    ordering = ("-date",)

admin.site.register(Order, OrderAdmin)
