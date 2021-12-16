from django.urls import path
from . import views

urlpatterns = [
    path("", views.made_to_measure, name="made_to_measure"),
]
