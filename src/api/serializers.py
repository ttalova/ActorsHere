from rest_framework import serializers
from authentication.models import User


class UserRegistrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data["email"],
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user


class StatusSerializer(serializers.Serializer):
    status = serializers.CharField()
