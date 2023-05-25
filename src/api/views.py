import uuid

import requests
from allauth.socialaccount.models import SocialApp
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F
from djoser.serializers import UserSerializer

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, mixins
from rest_framework.decorators import api_view, action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet

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
    ResponseSerializer,
    NotificationSerializer,
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
    Response as ResponseTable,
    Notification,
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

    @action(detail=False, methods=["GET"], url_path="get_favorite_actors_by_user_id")
    def get_favorite_actors_by_user_id(self, request):
        user_id = self.request.user.id
        favorites = FavoritesActor.objects.filter(user_id=user_id)
        actor_ids = favorites.values_list("actor_id", flat=True)
        actors = ActorProfile.objects.filter(id__in=actor_ids)
        serializer = self.serializer_class(actors, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        if data["photo"] == "null":
            data.pop("photo")
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["GET"], url_path="get_list_of_actors_to_casting")
    def get_list_of_actors_to_casting(self, request, *args, **kwargs):
        casting_id = kwargs.get("pk")
        if casting_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        queryset = ResponseTable.objects.filter(casting_id=casting_id)
        actor_ids = queryset.values_list("actor_id", flat=True)
        actors = ActorProfile.objects.filter(id__in=actor_ids)
        serializer = self.serializer_class(actors, many=True)
        return Response(serializer.data)


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
        data = request.data.copy()
        data["casting_owner"] = EmployerProfile.objects.get(user_id=request.user.id).id
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["GET"], url_path="get_users_castings")
    def get_users_castings(self, request, *args, **kwargs):
        employer_id = EmployerProfile.objects.get(user_id=request.user.id).id
        casting = self.queryset.filter(casting_owner_id=employer_id)
        serializer = self.serializer_class(casting, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="get_favorite_castings_by_user_id")
    def get_favorite_castings_by_user_id(self, request):
        user_id = self.request.user.id
        favorites = FavoritesCasting.objects.filter(user_id=user_id)
        casting_ids = favorites.values_list("casting_id", flat=True)
        castings = Casting.objects.filter(id__in=casting_ids)
        serializer = self.serializer_class(castings, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"], url_path="get_response_actors_by_user_id")
    def get_response_actors_by_user_id(self, request):
        actor_id = ActorProfile.objects.get(user_id=request.user.id).id
        favorites = ResponseTable.objects.filter(actor_id=actor_id)
        casting_ids = favorites.values_list("casting_id", flat=True)
        castings = Casting.objects.filter(id__in=casting_ids)
        serializer = self.serializer_class(castings, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        data["casting_owner"] = EmployerProfile.objects.get(user_id=request.user.id).id
        if data["photo"] == "null":
            data.pop("photo")
        serializer = self.serializer_class(instance=instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        modified_data = serializer.data.copy()
        casting_owner = modified_data["casting_owner"]
        modified_data["casting_owner"] = EmployerProfile.objects.get(id=casting_owner).user_id
        return Response(modified_data)


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
        queryset = super().get_queryset()
        if user_id:
            queryset = queryset.filter(user=user_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResponseViewSet(ModelViewSet):
    queryset = ResponseTable.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data["actor"] = ActorProfile.objects.get(user_id=request.user.id).id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        actor_id = ActorProfile.objects.get(user_id=self.request.user.id).id
        queryset = super().get_queryset()
        if actor_id:
            queryset = queryset.filter(actor=actor_id)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["GET"], url_path="get_response_by_actor")
    def get_response_by_actor(self, request, *args, **kwargs):
        actor_id = ActorProfile.objects.get(user_id=request.user.id).id
        casting_id = kwargs.get("pk")
        try:
            response = self.queryset.get(actor=actor_id, casting=casting_id)
        except self.queryset.model.DoesNotExist:
            response = None

        if response is not None:
            serializer = self.serializer_class(response)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = super().get_queryset()
        if user_id:
            queryset = queryset.filter(owner=user_id)
        return queryset.order_by(F("created_at").desc())


class UserSettingsViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        current_email = request.data.get("current_email")
        new_email = request.data.get("new_email")
        password = request.data.get("password")

        # Проверка соответствия текущей почты и пароля
        if instance.email == current_email and instance.check_password(password):
            instance.email = new_email
            instance.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view()
# def github_login(request):
#     if request.method == "POST":
#         code = list(request.POST.keys())
#         print('code', code)
#         data = {
#             "client_id": "127209d5c60d083ef3ec",
#             "client_secret": "aa80fbe3d310c115788a1452464ba66cdb0eb37a",
#             "code": code,
#             "redirect_uri": "http://localhost:5173/login_github/",
#         }
#         headers = {"Accept": "application/json"}
#         response = requests.post("https://github.com/login/oauth/access_token", data=data, headers=headers)
#         # access_token = response.json()["access_token"]
#         # headers = {"Authorization": f"Bearer {access_token}"}
#         # userResponse = requests.get("https://api.github.com/user", headers=headers)
#         # email = userResponse.json()["email"]
#         # if email is None:
#         #     login = userResponse.json()["login"]
#         #     email = f"{login}@mail.ru"
#         # password = userResponse.json()["node_id"]
#         # return JsonResponse({"email": email, "password": password})
#     return JsonResponse({"email": "error"})


class GithubLoginViewSet(ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):
        if request.method == "POST":
            code = list(request.POST.keys())
            data = {
                "client_id": "127209d5c60d083ef3ec",
                "client_secret": "aa80fbe3d310c115788a1452464ba66cdb0eb37a",
                "code": code,
                "redirect_uri": "http://localhost:5173/login_github/",
            }
            headers = {"Accept": "application/json"}
            response = requests.post("https://github.com/login/oauth/access_token", data=data, headers=headers)
            access_token = response.json()["access_token"]
            headers = {"Authorization": f"Bearer {access_token}"}
            userResponse = requests.get("https://api.github.com/user", headers=headers)
            email = userResponse.json()["email"]
            if email is None:
                login = userResponse.json()["login"]
                email = f"{login}@mail.ru"
            password = userResponse.json()["node_id"]
            print(email, password)
            return JsonResponse({"email": email, "password": password})
        return JsonResponse({"email": "error"})
