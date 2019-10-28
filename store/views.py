from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
