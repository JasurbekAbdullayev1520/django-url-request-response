from django.urls import path

from .views import calculators_view

urlpatterns = [
    path("", calculators_view, name="calculator"),
    path("calculator/", calculators_view, name="calculator_alt"),
]