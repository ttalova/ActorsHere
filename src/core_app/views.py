from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from core_app.forms import CastingForm
from core_app.models import Casting, ActorProfile, EmployerProfile


class CastingMixin:
    template_name = "main.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_queryset(self):
        return Casting.objects.all()


class NoteCreateFormView(CastingMixin, CreateView):
    form_class = CastingForm
