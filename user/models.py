from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileMananger(BaseUserManager):
    """help work with custom model"""

    def create_user(self,email, name, password=None):
        """create new user object"""

        if not email:
            raise valueError("Please provide an email address.")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name
            )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email, name, password):
        """Creates and saves superuser"""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represent user profile outside the system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileMananger()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """
        used to get user full name
        """
        return self.name

    def get_short_name(self):
        """
        used to get user short name
        """
        return self.name

    def __str__(self):
        """
        Used to convert an object to string
        """
        return self.email



