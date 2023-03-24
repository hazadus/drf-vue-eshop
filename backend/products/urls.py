from django.urls import path

from .views import (
    CategoryDetailView,
    LatestProductsList,
    ProductDetailView,
    search_view,
)

urlpatterns = [
    path("products/search/", search_view),
    path("latest-products/", LatestProductsList.as_view()),
    path(
        "products/<slug:category_slug>/<slug:product_slug>/",
        ProductDetailView.as_view(),
    ),
    path("products/<slug:category_slug>/", CategoryDetailView.as_view()),
]
