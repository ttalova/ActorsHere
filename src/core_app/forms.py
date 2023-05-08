from django import forms

from core_app.models import Casting


class CastingForm(forms.ModelForm):
    class Meta:
        model = Casting
        fields = "__all__"
