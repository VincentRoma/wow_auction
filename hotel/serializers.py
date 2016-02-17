from .models import Sell
from rest_framework import serializers

# Serializers define the API representation.
class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
