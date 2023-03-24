"""
DRF API views for Products and Categories.
"""
from django.db.models import Q
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class LatestProductsList(APIView):
    """
    API endpoint for latest products. Return 4 newest products in the shop.
    """

    @staticmethod
    def get(request: Request) -> Response:
        """
        Return 4 newest products in the shop.
        """
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """
    API endpoint for product details.
    """

    @staticmethod
    def get_object(category_slug: str, product_slug: str) -> Product:
        """
        Return product instance.
        """
        product = Product.objects.filter(
            category__slug=category_slug,
            slug=product_slug,
        )

        if product:
            return product.first()

        raise Http404

    def get(self, request: Request, category_slug: str, product_slug: str) -> Response:
        """
        Return product data by category and product slugs.
        """
        product = self.get_object(
            category_slug=category_slug, product_slug=product_slug
        )
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetailView(APIView):
    """
    Return detail product Category info, including list of all products in this category.
    """

    @staticmethod
    def get_object(category_slug: str) -> Category:
        """
        Return category instance.
        """
        category = Category.objects.filter(
            slug=category_slug,
        )

        if category:
            return category.first()

        raise Http404

    def get(self, request: Request, category_slug: str) -> Response:
        """
        Return category info, including list of all products.
        """
        category = self.get_object(
            category_slug=category_slug,
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(["POST"])
def search_view(request: Request):
    """
    Return Product serialized QuerySet filtered by `query`.
    Post {"query":"searched text"} to get the results.
    """
    query = request.data.get("query", "")

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) & Q(description__icontains=query)
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
