from django.urls import path
from rest_framework.routers import SimpleRouter

from api.views import (
    RegistrUserView,
    status_view,
    profile_view,
    ActorsView,
    TagsViewSet,
    CityViewSet,
    ClientSet,
    EmployersView,
    ProjectTypeViewSet,
    CastingsView,
)

router = SimpleRouter()
router.register("actors", ActorsView, basename="actors"),
router.register("employers", EmployersView, basename="employers"),
router.register("castings", CastingsView, basename="castings"),
router.register("tags", TagsViewSet, basename="tags"),
router.register("cities", CityViewSet, basename="cities"),
router.register("projecttype", ProjectTypeViewSet, basename="projecttype"),
router.register("clientid", ClientSet, basename="clientid"),

urlpatterns = [
    path("registr/", RegistrUserView.as_view(), name="registr"),
    path("status/", status_view, name="status"),
    path("profile/", profile_view, name="profile"),
] + router.urls
