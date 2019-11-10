from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from store import serializers
from . import models


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    """handles, creating, reading and updating user orders"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()

    def create_order(self, serializer):
        """create order for logged in user"""
        serializer.save(user_profile=self.request.user)
