#django/rest_framework imports.
from rest_framework import serializers

# app level imports
from .models import (
                    LatLongAddress,       
                    )


class LatLongAddressSerializer(serializers.ModelSerializer):
    """
    LatLong Serializer.
    """
    class Meta:
        model = LatLongAddress
        fields = "__all__"
