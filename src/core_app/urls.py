from django.urls import path
from core_app.views import NoteCreateFormView

urlpatterns = [
    path("main/", NoteCreateFormView.as_view(), name="main"),
]
