"""
DRF API views for Products.
"""
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


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
    def get_object(category_slug: str, product_slug: str):
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
