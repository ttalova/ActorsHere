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
    TokenResponseSerializer,
    ProfileSerializer,
    ActorsSerializer,
    TagSerializer,
)
from authentication.models import User

from api.serializers import StatusSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

from core_app.models import ActorProfile, Tag, EmployerProfile


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

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)
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


class TagsViewSet(mixins.ListModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Tag.objects.all()
