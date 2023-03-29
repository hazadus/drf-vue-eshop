from django.urls import path

from .views import OrdersList, checkout

urlpatterns = [
    path("checkout/", checkout),
    path("orders/", OrdersList.as_view()),
]
