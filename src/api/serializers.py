from rest_framework import serializers
from authentication.models import User


class UserRegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
