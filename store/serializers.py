from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=15)
    description = serializers.CharField(max_length=255)
    price = serializers.IntegerField()

    class Meta:
        model = models.Product
        fields = '__all__'