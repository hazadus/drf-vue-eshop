from rest_framework import serializers

from products.serializers import ProductSerializer

from .models import Order, OrderItem


class ListOrderItemSerializer(serializers.ModelSerializer):
    """
    OrderItem serializer for ListOrderSerializer.
    """

    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )


class ListOrderSerializer(serializers.ModelSerializer):
    """
    Order serializer used to LIST existing orders.
    """

    items = ListOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "place",
            "phone",
            "items",
            "paid_amount",
        )


class CreateOrderItemSerializer(serializers.ModelSerializer):
    """
    OrderItem serializer for CreateOrderSerializer.
    """

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )


class CreateOrderSerializer(serializers.ModelSerializer):
    """
    Order serializer used to CREATE new orders.
    """

    items = CreateOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "place",
            "phone",
            "items",
        )

    def create(self, validated_data):
        """
        NB: look how we create OrderItems for the Order, unpacking `item_data` as parameters to `create()`.
        """
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        return order
