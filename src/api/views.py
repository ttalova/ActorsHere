import time

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.serializers import UserRegistrSerializer, TokenResponseSerializer
from authentication.models import User

from api.serializers import StatusSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token as this_token


class RegistrUserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrSerializer
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        print("7654674", request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        user = serializer.create(serializer.validated_data)
        token = this_token.objects.create(user=user)
        response_data = {"token": token.key}
        response_serializer = TokenResponseSerializer(response_data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        #
        # serializer = UserRegistrSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(status.HTTP_201_CREATED)
        # else:
        #     data = serializer.errors
        #     return Response(data)


@api_view()
def status_view(request):
    return Response(StatusSerializer({"status": "ok"}).data)
