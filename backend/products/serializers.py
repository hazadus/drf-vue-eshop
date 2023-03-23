from rest_framework import serializers

from .models import Product


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
