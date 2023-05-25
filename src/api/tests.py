import unittest


from allauth.socialaccount.models import SocialApp

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APIClient, APIRequestFactory
from api.serializers import (
    UserRegistrSerializer,
    FavoritesCastingSerializer,
    FavoritesActorSerializer,
    StatusSerializer,
    ProfileSerializer,
)
from api.views import (
    RegistrUserView,
    ActorsView,
    TagsViewSet,
    CityViewSet,
    ProjectTypeViewSet,
    ClientSet,
    EmployersView,
    CastingsView,
    ProfileViewSet,
    status_view,
    profile_view,
)
from authentication.models import User
from core_app.models import (
    ActorProfile,
    City,
    Tag,
    ProjectType,
    EmployerProfile,
    Casting,
    FavoritesCasting,
    FavoritesActor,
    Response as ResponseTable,
    Profile,
)


class RegistrUserViewTestCase(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_data = {
            "email": "testuser",
            "password": "testpassword",
        }

    def test_invalid_data(self):
        invalid_data = {
            "email": "",
            "password": "testpassword",
            # Add other invalid data here
        }
        response = self.client.post("/api/registr/", data=invalid_data)
        self.assertEqual(response.status_code, 400)
        # Add more assertions to validate the response if necessary

    def test_serializer_class(self):
        serializer = UserRegistrSerializer()
        self.assertEqual(serializer.Meta.model, User)
        # Add more assertions to validate the serializer if necessary

    def test_permission_classes(self):
        view = RegistrUserView()
        self.assertTrue(AllowAny in view.permission_classes)
        # Add more assertions to validate the permission classes if necessary

    def test_renderer_classes(self):
        view = RegistrUserView()
        self.assertIn(JSONRenderer, view.renderer_classes)
        # Add more assertions to validate the renderer classes if necessary


class ActorsViewTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ActorsView.as_view({"get": "list", "post": "create"})
        user = User.objects.get(id=12)
        self.actor = ActorProfile.objects.get(user=user)
        self.valid_data = {
            "full_name": "Brad Pitt",
            "height": "1",
            "weight": "1",
            "clothing_size": "1",
            "shoe_size": "1",
            "birthdate": "2023-05-09",
            "figure_parameters": "1",
            "eye_color": "green",
            "voice_timbre": "high",
            "skin_color": "swarthy",
            "body_type": "average",
            "sex": "female",
            "city": 1,
            "tattoo": "exist",
            "face_type": "round",
            "hair_color": "dark_blonde",
            "piercing": "exist",
            "hair_length": "short",
            "education": "1",
            "tag": 5,
            "willing_to_relocate": False,
            "language_proficiency": "3day2",
            "skills": "1234",
            "international_passport": False,
            "driver_license": True,
            "phone_number": "11",
            "email": "hg@gmail.com",
            "social_network": "121",
            "user": 100,
        }
        self.invalid_data = {"full_name": "", "height": "1", "weight": "1", "clothing_size": "1", "user": 100}

    def test_permission_classes(self):
        view = ActorsView()
        self.assertTrue(AllowAny in view.permission_classes)

    def test_get_list_of_actors(self):
        request = self.factory.get("/api/actors/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_actor_with_invalid_data(self):
        request = self.factory.post("/api/actors/", self.invalid_data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_actor_by_user_id(self):
        request = self.factory.get("/api/actors/1/get_form_by_user_id/")
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_of_actors_to_casting(self):
        casting_id = 1
        request = self.factory.get("/api/actors/1/get_list_of_actors_to_casting/")
        response = self.view(request, pk=casting_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TagsViewSetTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TagsViewSet.as_view({"get": "list"})
        self.tag = Tag.objects.get(id=1)

    def test_get_list_of_tags(self):
        request = self.factory.get("/api/tags/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CityViewSetTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CityViewSet.as_view({"get": "list"})
        self.city = City.objects.get(name="Казань")

    def test_get_list_of_cities(self):
        request = self.factory.get("/api/cities/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProjectTypeViewSetTest(unittest.TestCase):
    def test_permission_classes(self):
        view = ProfileViewSet()
        self.assertTrue(AllowAny in view.permission_classes)

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ProjectTypeViewSet.as_view({"get": "list"})
        self.project_type = ProjectType.objects.get(id=1)

    def test_get_list_of_project_types(self):
        request = self.factory.get("/api/project-types/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ClientSetTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ClientSet.as_view({"get": "list"})
        self.client = SocialApp.objects.get(provider="google")

    def test_get_list_of_clients(self):
        request = self.factory.get("/api/clients/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EmployersViewTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = EmployersView.as_view({"get": "list", "post": "create"})
        user = User.objects.get(id=12)
        city = City.objects.get(id=1)
        self.employer = EmployerProfile.objects.get(id=5)
        self.valid_data = {
            "company_name": "string",
            "company_specialization": "acting_agency",
            "description": "string",
            "approximate_location": "string",
            "phone_number": "string",
            "additional_phone_number": "string",
            "webside": "http://127.0.0.1:8000/swagger/",
            "email": "user@example.com",
            "social_network": "string",
            "user": 1,
            "city": 1,
        }
        self.invalid_data = {"company_name": "", "user_id": 1}

    def test_permission_classes(self):
        view = EmployersView()
        self.assertTrue(AllowAny in view.permission_classes)

    def test_get_list_of_employers(self):
        request = self.factory.get("/api/employers/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employer_with_valid_data(self):
        request = self.factory.post("/api/employers/", self.valid_data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_employer_with_invalid_data(self):
        request = self.factory.post("/api/employers/", self.invalid_data)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_employer_by_user_id(self):
        request = self.factory.get("/api/employers/1/get_form_by_user_id/")
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CastingsViewTest(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CastingsView.as_view({"get": "list", "post": "create"})
        self.casting = Casting.objects.get(id=3)
        self.valid_data = {
            "header": "string",
            "fee": "string",
            "description": "string",
            "sex": "male",
            "experience": "string",
            "contact_email": "user@example.com",
            "social_network": "string",
            "actor_type_description": "string",
            "min_actor_age": 2147483647,
            "max_actor_age": 2147483647,
            "end_of_application": "2023-05-25",
            "date_of_event": "2023-05-25",
            "phone_number": "string",
            "casting_owner": 1,
            "project_type": 1,
            "city": 1,
            "tag": 1,
        }
        self.invalid_data = {"header": "", "casting_owner": 1}

    def test_permission_classes(self):
        view = CastingsView()
        self.assertTrue(AllowAny in view.permission_classes)

    def test_get_list_of_castings(self):
        request = self.factory.get("/api/castings/")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FavoritesCastingViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(id=1)
        self.client.force_authenticate(user=self.user)

    def test_create_favorite_casting(self):
        data = {"user": 1, "casting": 3}
        response = self.client.post("/api/favorite-casting/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        favorite_casting = FavoritesCasting.objects.get(id=response.data["id"])
        self.assertEqual(favorite_casting.user, self.user)

    def test_create_favorite_casting_with_invalid_data(self):
        data = {"casting": "invalid_data"}
        response = self.client.post("/api/favorite-casting/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_favorite_casting_by_user_and_casting_with_invalid_pk(self):
        response = self.client.get("/api/favorite-casting/1000000/get_like_by_user_and_casting/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FavoritesActorViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(id=1)
        self.client.force_authenticate(user=self.user)

    def test_create_favorite_actor(self):
        data = {"user": 1, "actor": 20}
        response = self.client.post("/api/favorite-actor/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        favorite_actor = FavoritesActor.objects.get(id=response.data["id"])
        self.assertEqual(favorite_actor.user, self.user)

    def test_create_favorite_actor_with_invalid_data(self):
        data = {"actor": "invalid_data"}
        response = self.client.post("/api/favorite-actor/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_favorite_actor_list(self):
        response = self.client.get("/api/favorite-actor/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #
    def test_delete_favorite_actor(self):
        actor = ActorProfile.objects.get(id=20)
        favorite_actor = FavoritesActor.objects.create(user=self.user, actor=actor)
        response = self.client.delete(f"/api/favorite-actor/{favorite_actor.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FavoritesActor.objects.filter(id=favorite_actor.id).exists())

    def test_get_favorite_actor_by_user_and_actor_with_invalid_pk(self):
        response = self.client.get("/api/favorite-actor/1000/get_like_by_user_and_actor/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ResponseViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(id=12)
        self.actor = ActorProfile.objects.get(id=19)
        self.casting = Casting.objects.get(id=3)
        self.client.force_authenticate(user=self.user)

    def test_get_response_list_without_responses(self):
        response = self.client.get("/api/response/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_response(self):
        response_obj = ResponseTable.objects.create(actor=self.actor, casting=self.casting)
        response = self.client.delete(f"/api/response/{response_obj.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(ResponseTable.objects.filter(id=response_obj.id).exists())

    def test_get_response_by_actor_with_invalid_pk(self):
        response = self.client.get("/api/response/1000/get_response_by_actor/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class StatusViewTestCase(unittest.TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(id=1)
        self.client.force_authenticate(user=self.user)
        self.factory = APIRequestFactory()

    def test_status_view(self):
        request = self.factory.get("/api/status/")
        response = status_view(request)
        serializer = StatusSerializer({"status": "ok"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProfileViewTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.get(id=1)

    def test_profile_view(self):
        request = self.factory.get("/api/profile/")
        request.user = self.user
        response = profile_view(request)
        serializer = ProfileSerializer(self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class ProfileViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_forget_password_email_not_found(self):
        request = self.factory.post("/api/forget_password/", data={"email": "nonexistent@example.com"})
        response = ProfileViewSet.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
