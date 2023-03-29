from rest_framework import serializers

from products.serializers import ProductSerializer

from .models import Order, OrderItem


class ListOrderItemSerializer(serializers.ModelSerializer):
    """
    OrderItem serializer for ListOrderSerializer.
    The difference with `CreateOrderItemSerializer` is thar we want full infofor `product`, not only `id`.
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
    Here we use `ListOrderItemSerializer` to have full info on products in `items`.
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
    The difference with `ListOrderSerializer` is that we only want `id` for `product`.
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
    Here we use `CreateOrderItemSerializer` with only product `id`s, and overrite `create()` method
    to properly create all `OrderItem`s in DB.
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
