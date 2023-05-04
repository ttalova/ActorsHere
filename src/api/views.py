import time

from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, mixins
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.filters import ActorsFilter
from api.serializers import (
    UserRegistrSerializer,
    ProfileSerializer,
    ActorsSerializer,
    TagSerializer,
    CitySerializer,
)
from authentication.models import User

from api.serializers import StatusSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from core_app.models import ActorProfile, Tag, EmployerProfile, City


class RegistrUserView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrSerializer
    renderer_classes = (JSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


@api_view()
def status_view(request):
    return Response(StatusSerializer({"status": "ok"}).data)


# permission_classes = (ISAuthenticated)
#   serializer_class = LoginSerializer
#   renderer_classes = (TokenAuthentication)


@swagger_auto_schema(method="GET", responses={status.HTTP_200_OK: ProfileSerializer()})
@api_view(["GET"])
def profile_view(request):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data)


class ActorsView(ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ActorsFilter
    permission_classes = (AllowAny,)
    serializer_class = ActorsSerializer
    queryset = ActorProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagsViewSet(mixins.ListModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Tag.objects.all()


class CityViewSet(mixins.ListModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return City.objects.all()
