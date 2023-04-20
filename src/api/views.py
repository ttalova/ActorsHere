import time

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.serializers import UserRegistrSerializer
from authentication.models import User

from api.serializers import StatusSerializer


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer = UserRegistrSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data)


@api_view()
def status_view(request):
    return Response(StatusSerializer({"status": "ok"}).data)
