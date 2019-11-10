from rest_framework import serializers
from . import models
from order import models as order_model


class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=15)
    description = serializers.CharField(max_length=255)
    selling_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buying_price = serializers.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = models.Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    """Order items serializer"""

    class Meta:
        model = order_model.Order
        fields = '__all__'
