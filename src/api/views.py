import time

from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.serializers import UserRegistrSerializer, TokenResponseSerializer
from authentication.models import User

from api.serializers import StatusSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class RegistrUserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrSerializer
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        token = Token.objects.create(user=user)
        response_data = {"token": token.key}
        response_serializer = TokenResponseSerializer(response_data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is None:
            raise AuthenticationFailed()
        token, created = Token.objects.get_or_create(user=user)
        response_data = {"token": token.key}
        response_serializer = TokenResponseSerializer(response_data)
        return Response(response_serializer.data)


@api_view()
def status_view(request):
    return Response(StatusSerializer({"status": "ok"}).data)


# permission_classes = (ISAuthenticated)
#   serializer_class = LoginSerializer
#   renderer_classes = (TokenAuthentication)
