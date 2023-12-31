from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        password=validated_data.pop('password')
        user=CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user   

class LoginSerializer(serializers.Serializer):
    user_name=serializers.CharField()
    password=serializers.CharField()    
    
class ValueSerializer(serializers.ModelSerializer ):
    class Meta:
        model=InputValue
        fields="__all__"    