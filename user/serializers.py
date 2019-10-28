from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    """A serializer for user profile"""

    name = serializers.CharField(max_length=15)
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password',)
        extra_kwargs = {'password':{
            'write_only': True
        }}
    
    def create(self, validated_data):
        """Create and return new user profile"""

        user = models.UserProfile(
            name=validated_data['name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user