from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import serializers
from . import models
from . import permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    API view for creating,
    reading and updating profiles
     """
    serializer_class = serializers.UserSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """checks email and password and returns aouth token"""
    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Creates auth token from user credentials"""
        return ObtainAuthToken().post(request)
