from .models import Item
from rest_framework import serializers

# Serializers define the API representation.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
