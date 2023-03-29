from rest_framework import authentication, permissions, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import CreateOrderSerializer, ListOrderSerializer


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request: Request) -> Response:
    """
    Proceed payment and place the order if succeeded.
    """
    serializer = CreateOrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(
            item.get("quantity") * item.get("product").price
            for item in serializer.validated_data["items"]
        )

        # Proceed payment here!
        serializer.save(user=request.user, paid_amount=paid_amount)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    """
    List all user's orders.
    """

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(self, request: Request) -> Response:
        """
        Return all user's orders.
        """
        orders = Order.objects.filter(user=request.user)
        serializer = ListOrderSerializer(orders, many=True)
        return Response(serializer.data)
