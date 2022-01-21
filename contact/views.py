from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        subject = request.POST["subject"]
        body = f"""
            {request.POST['name']} has sent you a contact query:
            {request.POST['query']}"""
        return_email = request.POST["email"]

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [return_email],
        )

        messages.info(request, "Your query has been sent")
        return redirect(reverse("products"))

    return render(request, "contact/contact.html")


def alterations(request):
    if request.method == "POST":
        subject = f"Alteration Request: {request.POST['alteration']}"
        body = f"""{request.POST['name']} has sent you an alteration request:
            {request.POST['query']}"""
        return_email = request.POST["email"]

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [return_email],
        )

        messages.info(request, "Your alteration request has been sent")
        return redirect(reverse("products"))

    return render(request, "contact/alterations.html")
