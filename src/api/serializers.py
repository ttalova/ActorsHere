from django.contrib.auth.hashers import make_password
from djoser.serializers import UserSerializer
from rest_framework import serializers
from authentication.models import User
from core_app.models import Casting, EmployerProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "role")


class UserRegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


# class EmployerProfileSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = EmployerProfile
#         fields = ('email', 'password')
