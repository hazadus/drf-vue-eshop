from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class LatestProductsList(APIView):
    """
    View for latest products. Return 4 newest products in the shop.
    """

    @staticmethod
    def get(request: Request) -> Response:
        """
        Return 4 newest products in the shop.
        """
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data)
