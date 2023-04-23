from django.contrib.auth.hashers import make_password
from djoser.serializers import UserSerializer
from rest_framework import serializers
from authentication.models import User
from core_app.models import Casting, EmployerProfile


class UserRegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_password(self, value: str) -> str:
        return make_password(value)


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


class EmployerProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = "__all__"
