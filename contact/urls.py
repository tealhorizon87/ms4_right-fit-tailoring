from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path("alterations/", views.alterations, name="alterations"),
]
