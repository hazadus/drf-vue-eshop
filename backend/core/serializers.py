from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    More detailed User model serializer for "/users/me/" Djoser endpoint.
    More info here: https://djoser.readthedocs.io/en/latest/settings.html?highlight=users%2Fme#serializers
    """

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        )
