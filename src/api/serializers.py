from allauth.socialaccount.models import SocialApp
from django.contrib.auth.hashers import make_password
from djoser.serializers import UserSerializer
from rest_framework import serializers
from authentication.models import User
from core_app.models import (
    EmployerProfile,
    ActorProfile,
    Tag,
    City,
    ProjectType,
    Casting,
    Profile,
    FavoritesCasting,
    FavoritesActor,
)


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
            return False


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

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class EmployersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = "__all__"
        read_only_fields = ("rating",)

    def create(self, validated_data):
        return EmployerProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "title")


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = ("id", "type_of_project")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name")


class ClientIdSerializer(serializers.ModelSerializer):
    client_id = serializers.CharField()
    provider = serializers.CharField()

    class Meta:
        model = SocialApp
        fields = ("client_id", "provider")


class CastingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casting
        fields = "__all__"
        read_only_fields = ("moderation",)

    def create(self, validated_data):
        return Casting.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class FavoritesCastingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritesCasting
        fields = "__all__"


class FavoritesActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritesActor
        fields = "__all__"
