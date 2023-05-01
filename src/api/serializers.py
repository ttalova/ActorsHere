from django.contrib.auth.hashers import make_password
from djoser.serializers import UserSerializer
from rest_framework import serializers
from authentication.models import User
from core_app.models import EmployerProfile, ActorProfile, Tag, City


class ProfileSerializer(serializers.ModelSerializer):
    type_of_profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "email", "role", "type_of_profile")

    def get_type_of_profile(self, obj):
        user_actor = ActorProfile.objects.filter(user__email=obj)
        user_employer = EmployerProfile.objects.filter(user__email=obj)
        if user_employer:
            return "employer"
        elif user_actor:
            return "actor"
        else:
            return None


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


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorProfile
        fields = "__all__"
        read_only_fields = (
            "form_active",
            "rating",
        )

    def create(self, validated_data):
        return ActorProfile.objects.create(**validated_data)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")
