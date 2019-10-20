from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers
from . import models

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API view for creating,
    reading and updating profiles
     """
    serializer_class = serializers.UserSerializer
    queryset = models.UserProfile.objects.all()

    