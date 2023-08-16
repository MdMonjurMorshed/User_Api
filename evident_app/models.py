from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import CustomManager
from .abstract import CommonField

# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100,blank=False)
    user_name=models.CharField(max_length=100,blank=False,unique=True)
    email=models.EmailField(blank=False,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD='user_name'
    REQUIRED_FIELDS=['email']

    objects=CustomManager()


### model for the input values

class InputValue(CommonField):
    timestamp=models.DateTimeField(auto_now_add=True)
    values=models.CharField(max_length=200,blank=False)

