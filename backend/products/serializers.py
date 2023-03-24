from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    Note how we serialize `@property` methods from model!
    """

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "image_url",
            "thumbnail_url",
            "get_absolute_url",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for product Category model.
    Includes list of all products in this category.
    """
    # List all the products in the category:
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "get_absolute_url",
            "products",
        ]
