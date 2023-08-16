from django.contrib.auth.models import BaseUserManager


class CustomManager(BaseUserManager):
    def create_user(self,user_name,email,password=None,**extra_fields):
        if not user_name:
            raise ValueError('username is required')
        if not email:
            raise ValueError('email is required')
        email=self.normalize_email(email)
        user=self.model(user_name=user_name,email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,user_name,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        extra_fields.setdefault("is_active",True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be true')
        if user_name is None:
            raise ValueError('username is required')
        email=self.normalize_email(email)
        return self.create_user(user_name,email,password,**extra_fields)
