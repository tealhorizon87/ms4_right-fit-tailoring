from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product, Category
from django.contrib import messages
from .forms import MtmForm
from .models import MtmOrder


def made_to_measure(request):
    """ A view to display the made to measure form """

    products = Product.objects.all()
    garment = request.GET["garment"]

    if "category" in request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__category_name__in=categories)

    context = {
        "products": products,
        "garment": garment,
    }

    return render(request, "made_to_measure/made_to_measure.html", context)


def mtm_form(request, product_id):
    """ A view to display and process the made to measure form """

    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        
        mtm_price = request.POST.get("mtm_price")
        form_data = {
            "order_total": mtm_price,
        }
        for entry in request.POST:
            if entry == "product":
                form_data["product"] = product
            elif entry != "csrfmiddlewaretoken":
                form_data[entry] = request.POST[entry]

        form = MtmForm(form_data)
        form.save()
        messages.success(request, f"""
            Your order has been submitted.
            One of our team will contact you shortly""")

        return redirect(reverse("products"))
    else:
        garment = request.GET["garment"]
        form = MtmForm()
        tops = ["Shirts", "Jackets", "Coats", "Waistcoats"]
        bottoms = ["Trousers", "Shorts"]

        if garment in tops:
            required_measurements = "tops"
            mtm_price = (product.price * 3) + 20
        elif garment in bottoms:
            required_measurements = "bottoms"
            mtm_price = (product.price * 4) + 30
        else:
            required_measurements = "both"
            mtm_price = (product.price * 5) + 60

    context = {
        "product": product,
        "mtm_price": mtm_price,
        "garment": garment,
        "form": form,
        "required_measurements": required_measurements,
    }

    return render(request, "made_to_measure/mtm_form.html", context)
