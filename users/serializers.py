from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields=['id','username','email','name','password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField()
    password= serializers.CharField(write_only=True)

    def validate(self, data):
        user= authenticate(username= data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid Credentials")
        data['user']=user
        return data
        