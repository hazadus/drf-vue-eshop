from django.urls import path

from .views import LatestProductsList, ProductDetailView

urlpatterns = [
    path("latest-products/", LatestProductsList.as_view()),
    path(
        "products/<slug:category_slug>/<slug:product_slug>/",
        ProductDetailView.as_view(),
    ),
]
