from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Food
        fields = ('id', 'name', 'calories')
        read_only_fields = ('date_created', 'date_modified')
