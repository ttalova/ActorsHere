import uuid

from allauth.socialaccount.models import SocialApp
from django_filters.rest_framework import DjangoFilterBackend

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, mixins
from rest_framework.decorators import api_view, action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.email_function import send_forget_password_mail
from api.filters import ActorsFilter
from api.serializers import (
    UserRegistrSerializer,
    ProfileSerializer,
    ActorsSerializer,
    TagSerializer,
    CitySerializer,
    ClientIdSerializer,
    EmployersSerializer,
    ProjectTypeSerializer,
    CastingsSerializer,
    ChangePasswordSerializer,
    FavoritesCastingSerializer,
    FavoritesActorSerializer,
)

from api.serializers import StatusSerializer
from rest_framework.views import APIView

from authentication.models import User
from core_app.models import (
    ActorProfile,
    Tag,
    City,
    EmployerProfile,
    ProjectType,
    Casting,
    Profile,
    FavoritesCasting,
    FavoritesActor,
)


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

    @action(detail=True, methods=["GET"], url_path="get_form_by_user_id")
    def get_actor_by_user_id(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        actor = get_object_or_404(self.queryset, user_id=user_id)
        serializer = self.serializer_class(actor)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ProjectTypeViewSet(mixins.ListModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = ProjectTypeSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return ProjectType.objects.all()


class ClientSet(mixins.ListModelMixin, GenericViewSet):
    pagination_class = None
    serializer_class = ClientIdSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return SocialApp.objects.all()


class EmployersView(ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = ActorsFilter
    permission_classes = (AllowAny,)
    serializer_class = EmployersSerializer
    queryset = EmployerProfile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["GET"], url_path="get_form_by_user_id")
    def get_actor_by_user_id(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        actor = get_object_or_404(self.queryset, user_id=user_id)
        serializer = self.serializer_class(actor)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CastingsView(ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    # filterset_class = ActorsFilter
    permission_classes = (AllowAny,)
    serializer_class = CastingsSerializer
    queryset = Casting.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["GET"], url_path="get_users_castings")
    def get_users_castings(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        casting = self.queryset.filter(casting_owner_id=user_id)
        serializer = self.serializer_class(casting, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def ForgetPassword(request):
#     try:
#         if request.method == 'POST':
#             email = request.POST.get('email')
#             if not User.objects.filter(email=email).first():
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#
#             user_obj = User.obgects.get(email=email)
#             token = str(uuid.uuid4())
#             send_forget_password_mail(user_obj, token)
#             return Response(status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# def ChangePassword(request, token):
#     context = {}
#     try:
#         profile_obj = Profile.objects.get(send_forget_password = token)
#         print(profile_obj)
#         return Response(status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#


class ProfileViewSet(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get("email")
            if not User.objects.filter(email=email).first():
                return Response(status=status.HTTP_404_NOT_FOUND)

            user_obj = User.objects.get(email=email)
            token = str(uuid.uuid4())
            profile_obj, _ = Profile.objects.get_or_create(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj, token)
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdatePasswordViewSet(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ChangePasswordSerializer

    def post(self, request, token=None):
        try:
            profile_obj = Profile.objects.get(forget_password_token=token)
            new_password = request.data.get("password_first")
            new_password_second = request.data.get("password_second")
            if new_password != new_password_second:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            user_id = profile_obj.user_id
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            context = {"user_id": profile_obj.user.id}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class FavoritesCastingViewSet(ModelViewSet):
    queryset = FavoritesCasting.objects.all()
    serializer_class = FavoritesCastingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        user_id = self.request.user.id
        casting_id = self.request.GET.get("casting")
        queryset = super().get_queryset()
        if user_id and casting_id:
            queryset = queryset.filter(user=user_id, casting=casting_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["GET"], url_path="get_like_by_user_and_casting")
    def get_like_by_user_and_casting(self, request, *args, **kwargs):
        user_id = self.request.user.id
        casting_id = kwargs.get("pk")
        try:
            casting = self.queryset.get(user=user_id, casting=casting_id)
        except self.queryset.model.DoesNotExist:
            casting = None

        if casting is not None:
            serializer = self.serializer_class(casting)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class FavoritesActorViewSet(ModelViewSet):
    queryset = FavoritesActor.objects.all()
    serializer_class = FavoritesActorSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"], url_path="get_like_by_user_and_actor")
    def get_like_by_user_and_actor(self, request, *args, **kwargs):
        user_id = self.request.user.id
        actor_id = kwargs.get("pk")
        try:
            actor = self.queryset.get(user=user_id, actor=actor_id)
        except self.queryset.model.DoesNotExist:
            actor = None

        if actor is not None:
            serializer = self.serializer_class(actor)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        user_id = self.request.user.id
        actor_id = self.request.GET.get("actor")
        queryset = super().get_queryset()
        if user_id and actor_id:
            queryset = queryset.filter(user=user_id, actor=actor_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
