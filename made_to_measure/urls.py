from django.urls import path
from . import views

urlpatterns = [
    path("", views.made_to_measure, name="made_to_measure"),
    path("mtm_form/<int:product_id>/", views.mtm_form, name="mtm_form"),
]
