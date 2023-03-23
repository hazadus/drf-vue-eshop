from django.urls import path

from .views import LatestProductsList

urlpatterns = [
    path("latest-products/", LatestProductsList.as_view()),
]
